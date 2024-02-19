import datetime
from dataclasses import dataclass
from threading import Lock
from typing import Dict, List, Callable, Any, Union

import PIL
import boto3
import notion_client
import numpy as np
import pandas as pd
from IPython import embed
from botocore.exceptions import ClientError
# from llama_index.response.schema import Response
from loguru import logger
from notion_database.database import Database
from notion_database.page import Page
from notion_database.properties import Properties
from pinjected import injected_function, Injected, injected
from proboscis_image_rules.auto_image import AutoImage
from returns.result import safe, Failure, Success
from tqdm import tqdm


# from davinci.paper_index_sandbox import NOTION_TOKEN, df, iccvs, ROOT_PAGE


@dataclass
class Prop:
    type: str
    value: object

    @property
    def pure_value(self):
        def unwrap(data: object):
            match data:
                case None:
                    return None
                case str():
                    return data
                case float() | int():
                    return data
                case {'value': v}:
                    return unwrap(v)
                case {'select': v}:
                    return unwrap(v)
                case {'name': v}:
                    return unwrap(v)
                case _:
                    raise ValueError(f"unknown type: {type(data)} for data:{data}")

        return unwrap(self.value)


@dataclass
class NPage:
    id: str
    properties: Dict[str, Prop]

    def __post_init__(self):
        assert isinstance(self.properties, dict), "properties must be dict"
        self.title = None
        for k, p in self.properties.items():
            if p.type == "title":
                self.title = p.value
        # assert self.title is not None, f"title is required.{self.properties}"


@dataclass
class Select:
    value: object


@dataclass
class NotionAPI:
    token: str

    def create_page_for_row(self, db_id, row, columns, kv_to_prop):
        pages = {p.title: p for p in find_pages(self.token, db_id)}
        title = row["title"]
        # lets find out which properties are missing.
        page_data = safe(pages.__getitem__)(title)
        required_props = set(columns)

        logger.info(f"name match:{page_data.map(lambda p: p.title == title)}")
        page_prop = create_properties(kv_to_prop, required_props, row)

        page = Page(self.token)
        logger.info(f"updating page with {page_prop.result}")
        match page_data:
            case Failure():
                page.create_page(db_id, page_prop)
            case Success(p):
                try:
                    page.update_page(p.id, page_prop)
                except Exception as e:
                    # error parsing json body???
                    logger.error(f"page update with title:{title} failed with result:{page.result}")
                    embed()
                    raise e
            case _:
                raise Exception("should not happen")

    def get_child_blocks(self, id):
        url = f"https://api.notion.com/v1/blocks/{id}/children?page_size=100"
        notion = notion_client.Client(auth=self.token)
        return notion.request(url, method="GET")["results"]

    def create_db(self, db_id,
                  df, page_name: str, kv_to_prop):
        db = Database(self)
        sample = df.iloc[0].to_dict()
        properties = {k: kv_to_prop(k, v) for k, v in sample.items()}
        properties = setup_db_properties(properties)
        db.create_database(db_id, page_name,
                           properties=properties
                           )
        if 'id' not in db.result:
            logger.error(f"failed to create database: {db.result}")
            raise RuntimeError(f"failed to create database: {db.result}")

        return db.result['id']

    def add_missing_properties(self, df, db_id, kv_to_prop) -> dict:
        logger.info(f"adding missing properties")
        columns = df.columns
        db = NotionDB(self.token, db_id)
        missing_props = set(columns) - set(db.props.keys())
        properties = {k: kv_to_prop(k, v) for k, v in df.iloc[0].to_dict().items() if k in missing_props}
        properties = setup_db_properties(properties)
        db = Database(self.token)
        db.update_database(db_id, add_properties=properties)
        logger.info(f"added missing properties: {missing_props}")
        return db.result

    def check_properties(self, db_id):
        db = NotionDB(self.token, db_id)
        return db.props


@injected
def upload_image_to_s3(
        get_s3_client: boto3.client,
        logger,
        /,
        image: Union[AutoImage],
        s3_bucket_name: str,
        image_path: str,
        overwrite=False
) -> str:
    assert isinstance(s3_bucket_name,
                      str), f"Expected s3_bucket_name to be of type 'str', got {type(s3_bucket_name).__name__}"

    assert isinstance(image_path, str), f"Expected image_path to be of type 'str', got {type(image_path).__name__}"

    assert isinstance(overwrite, bool), f"Expected overwrite to be of type 'bool', got {type(overwrite).__name__}"

    assert isinstance(image, AutoImage), f"Expected image to be of type 'AutoImage', got {type(image).__name__}"

    # first check if the image is present on s3
    s3_client = get_s3_client()

    # beware that s3 client is not thread safe so we need each per a thread.

    try:
        if not overwrite:
            s3_client.head_object(Bucket=s3_bucket_name, Key=image_path)
            logger.info(f"Image already present on s3://{s3_bucket_name}/{image_path}")
            http_addr = f"https://s3.amazonaws.com/{s3_bucket_name}/{image_path}"
            return http_addr
    except ClientError:
        pass

    logger.info(f"Uploading image to s3://{s3_bucket_name}/{image_path}")

    s3_client.put_object(
        Bucket=s3_bucket_name,
        Key=image_path,
        Body=image.to("png_bytes"),
        ContentType="image/png",
    )

    logger.info(f"Finished uploading image to s3://{s3_bucket_name}/{image_path}")

    http_addr = f"https://s3.amazonaws.com/{s3_bucket_name}/{image_path}"
    logger.info(f"the address is: {http_addr}")

    return http_addr


@injected
def ensured_s3_bucket_for_notion(
        s3_bucket_for_notion: str,
        ensure_bucket_exists,
        /,
):
    ensure_bucket_exists(s3_bucket_for_notion)
    return True


@injected
def get_aws_client(
        aws_access_key_id: str,
        aws_secret_access_key: str,
        region_name: str,
        boto3_lock: Lock,
        /,
        client_type,
        **kwargs
):
    # something is preventing pickling due to open file...

    # logger.info(f"creating boto3 client {client_type} with region {_region_name} and kwargs {kwargs}")
    with boto3_lock:
        session = boto3.Session()
        return session.client(
            client_type,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
            **kwargs
        )


get_s3_client = Injected.bind(
    get_aws_client,
    aws_access_key_id=Injected.by_name("aws_access_key_id_for_s3"),
    aws_secret_access_key=Injected.by_name("aws_secret_access_key_for_s3"),
).map(lambda factory: lambda: factory("s3"))


@injected
def ensure_bucket_exists(get_s3_client, /, bucket_name):
    s3 = get_s3_client()

    # Check if the bucket exists
    try:
        s3.head_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} exists")
    except:
        print(f"Bucket {bucket_name} does not exist. Creating now...")

        # If not, create the bucket
        s3.create_bucket(Bucket=bucket_name)

        print(f"Bucket {bucket_name} created")


@injected_function
def upload_image_for_notion(
        upload_image_to_s3,
        s3_bucket_for_notion: str,
        ensured_s3_bucket_for_notion,  # required for initialization
        /,
        image: Union[AutoImage],
        name: str
):
    """
    :param upload_image_to_s3:
    :param s3_bucket_for_notion:
    :param image:
    :param name: any.png
    :return:
    """
    assert ensured_s3_bucket_for_notion
    return upload_image_to_s3(
        image,
        s3_bucket_for_notion,
        name,
    )


@injected_function
def default_kv_to_prop(
        upload_image_for_notion,
        /,
        key, value):
    match (key, value):
        case ("title", _):
            return Prop("title", value)
        case (_, bool()):
            return Prop("checkbox", value)

        case (_, Select(value)):
            return Prop("select", str(value))
        case (_, Success(int() as v) |
                 Success(float() as v) |
                 (int() as v) |
                 (float() as v)
              ) if not np.isnan(v):
            return Prop("number", v)
        case (_, (float() as v)) if np.isnan(value):
            return None
        case (k, _) if k in ["keywords", "abbr", "tasks", "conf_abbr"]:
            return Prop("multi_select", [t.strip() for t in value.split(",") if len(t) < 100])
        case (_, str() as s) if s.startswith("http"):
            return Prop("url", value)
        case (_, str()):
            return Prop('rich_text', value)
        case (_, {'start': datetime.date() as start, 'end': datetime.date() as end}):
            return Prop("date", dict(start=str(start), end=str(end), time_zone='Asia/Tokyo'))
        case (_, {'start': datetime.datetime() as start, 'end': datetime.datetime() as end}):
            return Prop("date", dict(start=str(start), end=str(end), time_zone='Asia/Tokyo'))
        case (k, [*items]) if all(isinstance(item, int) for item in items):
            return Prop('rich_text', str(items))
        case (k, [*items]) if all(isinstance(item, str) and len(item) < 100 for item in items):
            return Prop("multi_select", items)
        case (_, {'start': str(), 'end': str()}):
            logger.warning(f"invalid date range:{value} for key:{key}")
            return None
        case (_, img) if isinstance(img, PIL.Image.Image):
            img = AutoImage.identify(img)
            name = img.image_hash() + ".png"
            url = upload_image_for_notion(img, name)
            return Prop("files", dict(external=dict(url=url)))
        case (str(), _):
            return Prop("rich_text", str(value))
        case (_, _):
            raise ValueError(f"unknown type: {type(value)} for key:{key}")


@injected_function
def notion_create_page_for_row(notion_api: NotionAPI, /, db_id, row, columns, kv_to_prop):
    return notion_api.create_page_for_row(db_id, row, columns, kv_to_prop)


def setup_properties(properties: Dict[str, Prop]):
    page_prop = Properties()
    for key, prop in properties.items():
        value = prop.value
        match prop.type:
            case "title":
                assert isinstance(value, str)
                page_prop.set_title(key, value)
            case 'checkbox':
                assert isinstance(value, bool)
                page_prop.set_checkbox(key, value)
            case "number":
                assert isinstance(value, int) or isinstance(value, float)
                page_prop.set_number(key, value)
            case "multi_select":
                assert isinstance(value, list)
                page_prop.set_multi_select(key, value)
            case "select":
                assert isinstance(value, str)
                page_prop.set_select(key, value)
            case "rich_text":
                assert isinstance(value, str)
                page_prop.set_rich_text(key, value)
            case "date":
                assert isinstance(value, dict)
                start = value.get('start', None)
                end = value.get('end', None)
                page_prop.set_date(key, start=start, end=end)
            case "files":
                assert isinstance(value, dict)
                external = value.get('external', None)
                assert isinstance(external, dict)
                url = external.get('url', None)
                assert isinstance(url, str)
                page_prop.set_files(key, [url])
            case "url":
                assert isinstance(value, str)
                page_prop.set_url(key, value)
            case _:
                raise ValueError(f"unknown type: {prop.type}")
    return page_prop


def create_properties(kv_to_prop, target_prop_names, row):
    properties = {col: kv_to_prop(col, row[col]) for col in target_prop_names}
    properties = {k: v for k, v in properties.items() if v is not None}
    properties = setup_properties(properties)
    return properties


def parse_page(data):
    props = data["properties"]
    res = {}
    for k, v in props.items():
        res[k] = parse_property(v)
    return NPage(data["id"], res)


def parse_property(prop):
    match prop:
        case {"type": "title", "title": [{"type": 'text', "text": {"content": title_str}}]}:
            return Prop("title", title_str)
        case {"type": "title", "title": []}:
            return Prop("title", None)
        case {"type": "rich_text", "rich_text": [{"type": 'text', "text": {"content": text_str}}]}:
            return Prop("text", text_str)
        case {"type": "rich_text", "rich_text": []}:
            return Prop("text", None)
        case {"type": "checkbox", "checkbox": bool_val}:
            return Prop("checkbox", bool_val)
        case {"type": 'number', "number": number}:
            return Prop("number", number)
        case {'type': 'multi_select', 'multi_select': elems}:
            return Prop("multi_select", parse_multi_select_elems(elems))
        case unknown:
            return Prop("unknown", unknown)


def parse_multi_select_elems(elems):
    result = []
    for item in elems:
        match item:
            case {"name": name}:
                result.append(name)
    if not result:
        return None
    return result


def find_pages(token, db_id) -> List[NPage]:
    db = Database(token)
    db.find_all_page(db_id)
    return [parse_page(d) for d in db.result["results"]]


def find_title_col(token, db_id) -> str:
    db = Database(token)
    db.retrieve_database(db_id, get_properties=True)
    props = db.result["properties"]
    for k, v in props.items():
        match v:
            case {"id": 'title', "type": "title", 'name': name}:
                return name
    raise RuntimeError("title column not found")


@dataclass
class NotionDB:
    _notion_token: str
    db_id: str

    def __post_init__(self):
        assert isinstance(self.db_id, str)

    @property
    def props(self):
        db = Database(self._notion_token)
        db.retrieve_database(self.db_id, get_properties=True)
        return db.result["properties"]

    @property
    def pages(self) -> List[NPage]:
        db = Database(self._notion_token)
        db.find_all_page(self.db_id)
        return parse_notion_json(db.result)

    def to_df(self):
        pages = self.pages
        values = [{k: v.pure_value for k, v in p.properties.items()} for p in pages]
        return pd.DataFrame(values)


def parse_notion_json(data: dict):
    match data:
        case {"object": 'list'}:
            return [parse_notion_json(d) for d in data["results"]]
        case {"object": 'page'}:
            return parse_page(data)
        case _:
            raise ValueError(f"unknown data type {data}")


@injected_function
def get_db_by_name(
        notion_root_page,
        notion_api: NotionAPI,
        to_notion_db,
        /,
        db_name: str
) -> NotionDB:
    blocks = notion_api.get_child_blocks(notion_root_page)
    dbs = list(find_database(blocks))
    logger.info(dbs)
    match [db for db in dbs if db["title"] == db_name]:
        case [{"id": db_id}]:
            return to_notion_db(db_id)
        case [*rest]:
            raise ValueError(f"multiple dbs or no dbs found. {rest}")


def setup_db_properties(properties: Dict[str, Prop]):
    page_prop = Properties()
    for key, prop in properties.items():
        match prop.type:
            case "title":
                page_prop.set_title(key)
            case "number":
                page_prop.set_number(key)
            case "multi_select":
                page_prop.set_multi_select(key)
            case "rich_text":
                page_prop.set_rich_text(key)
            case "date":
                page_prop.set_date(key)
            case "files":
                page_prop.set_files(key)
            case "url":
                page_prop.set_url(key)
            case "checkbox":
                page_prop.set_checkbox(key)
            case _:
                raise ValueError(f"unknown type: {prop.type}")
    return page_prop


@injected_function
def notion_fill_database(
        notion_api: NotionAPI,
        /, df, db_id, kv_to_prop: Callable[[str, Any], Prop]):
    add_result = notion_api.add_missing_properties(df, db_id, kv_to_prop)
    logger.warning(f"adding missing properties result: {add_result}")
    for idx, row in tqdm(df.iterrows(), desc="Filling DB", total=len(df)):
        try:
            notion_api.create_page_for_row(db_id, row, df.columns, kv_to_prop)
        except Exception as e:
            logger.error(e)
            raise e


def find_database(blocks):
    for block in tqdm(blocks, f"searching for databases"):
        match block:
            case {"child_database": {'title': db_title}, "id": db_id}:
                yield dict(id=db_id, title=db_title)


@injected_function
def notion_fill_or_create_db(
        notion_api: NotionAPI,
        notion_fill_database,
        notion_root_page,
        /, df, title: str, kv_to_prop):
    blocks = notion_api.get_child_blocks(notion_root_page)
    dbs = list(find_database(blocks))
    logger.info(dbs)
    match [db for db in dbs if db["title"] == title]:
        case []:
            logger.info(f"db not found. creating")
            db_id = notion_api.create_db(notion_root_page, df, title, kv_to_prop)
            notion_fill_database(df, db_id, kv_to_prop)
        case [{"id": db_id}]:
            logger.info(f"db found. filling")
            notion_fill_database(df, db_id, kv_to_prop=kv_to_prop)
        case [*rest]:
            raise ValueError(f"multiple dbs found. {rest}")


@injected_function
def fill_notion_with_df(
        notion_fill_or_create_db,
        notion_key_value_to_property,
        /,
        df,
        title
):
    assert 'title' in df.columns, "title column must be present"
    notion_fill_or_create_db(
        df,
        title,
        kv_to_prop=notion_key_value_to_property
    )


db_property: Injected = get_db_by_name("CVPR2023 - vector graphics").props
