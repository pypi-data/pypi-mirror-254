from typing import Callable, Any, Optional

import notion_client
import pandas as pd
from loguru import logger
from notion_client import Client
from pinjected import injected, instances, providers
from returns.result import safe, Result
from tqdm import tqdm

from pinjected_notion.notion_db_util import Prop, setup_db_properties, NotionDB, NPage, parse_page, create_properties, \
    get_s3_client

"""
        body = {
            "parent": {
                "type": "page_id",
                "page_id": page_id
            },
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": title,
                        "link": None
                    }
                }
            ],
            "properties": properties.result
        }
"""


@injected
def notion_find_db_by_name(
        notion_client: notion_client.Client,
        /,
        db_name: str
) -> str:
    try:
        res = notion_client.search(
            query=db_name,
            filter=dict(
                value="database",
                property="object",
            )
        )
    except Exception as e:
        logger.warning(f"search for db {db_name} failed with {e}")
        raise e
    # logger.info(f"search for db {db_name} returned \n{pformat(res)}")
    for entry in res['results']:
        match entry:
            case {'title': [
                {'text': {'content': _db_name}}
            ]} if _db_name == db_name:
                return entry['id']
    raise Exception(f"could not find db with name {db_name}")
    # ['results'][0]['id']


test_search_db = notion_find_db_by_name(
    db_name="test_page_for_db_creation"
)


@injected
def notion_create_db(
        notion_client: notion_client.Client,
        notion_key_value_to_property: Callable[[str, Any], Prop],
        notion_root_page: str,
        /,
        df: pd.DataFrame,
        page_name
) -> dict:
    """This works! phew! so let's ditch notion_database for calling it..
    let's just use that for property creation.
    """
    logger.info(f"creating db with name {page_name}")
    properties = {k: notion_key_value_to_property(k, v) for k, v in df.iloc[0].to_dict().items()}
    props: dict = setup_db_properties(properties).result

    return notion_client.databases.create(
        parent={"type": "page_id", "page_id": notion_root_page},
        title=[{"type": "text", "text": {"content": page_name, "link": None}}],
        properties=props
    )['id']


test_create_db = notion_create_db(
    db_id=injected("notion_root_page"),
    df=pd.DataFrame([dict(title="a", b=1, c=2)]),
    page_name="test_page_for_db_creation"
)


@injected
def notion_add_missing_properties(
        notion_token: str,
        notion_client: notion_client.Client,
        notion_key_value_to_property: Callable[[str, Any], Prop],
        /,
        db_id: str,
        df: pd.DataFrame,
):
    logger.info(f"adding missing properties")
    columns = df.columns
    db = NotionDB(notion_token, db_id)
    missing_props = set(columns) - set(db.props.keys())
    properties = {k: notion_key_value_to_property(k, v) for k, v in df.iloc[0].to_dict().items() if k in missing_props}
    properties = setup_db_properties(properties).result
    return notion_client.databases.update(
        db_id,
        properties=properties
    )


@injected
def notion_get_pages(
        notion_client: Client,
        /,
        db_id) -> list[NPage]:
    res = notion_client.databases.query(db_id)
    pages = [parse_page(d) for d in res["results"]]
    return pages


@injected
def notion_sync_page_for_row(
        notion_client: Client,
        notion_key_value_to_property: Callable[[str, Any], Prop],
        /,
        db_id,
        row,
        columns,
        page_id: Optional[str] = None
):
    required_props = set(columns)
    page_prop = create_properties(notion_key_value_to_property, required_props, row).result
    if page_id is None:
        return notion_client.pages.create(
            parent={"database_id": db_id},
            properties=page_prop
        )
    if page_id is not None:
        return notion_client.pages.update(
            page_id,
            properties=page_prop
        )


@injected
def notion_sync_database(
        notion_get_pages: Callable[[str], list[NPage]],
        notion_add_missing_properties: Callable[[str, pd.DataFrame], dict],
        notion_create_db: Callable[[pd.DataFrame, str], dict],
        notion_find_db_by_name: Callable[[str], str],
        notion_sync_page_for_row: Callable[[str, Any, list[str], Optional[str]], None],
        /,
        title: str,
        df: pd.DataFrame,
):
    # found_db_id = safe(notion_find_db_by_name)(title)
    # assert is_successful(found_db_id), f"could not find db with name {title}"
    assert 'title' in df.columns, "df must have a title column to be used in notion"
    db_id: Result[str] = safe(notion_find_db_by_name)(title).lash(
        lambda _: safe(notion_create_db)(df, title)
    ).unwrap()
    logger.info(f"syncing db_id: {db_id}")
    logger.info(f"db:{df}")
    notion_add_missing_properties(db_id, df)
    existing_pages = notion_get_pages(db_id)
    page_by_title = {p.title: p.id for p in existing_pages}
    for idx, row in tqdm(df.iterrows(), desc="Filling DB", total=len(df)):
        matching_page_id = page_by_title.get(row['title'])
        page_res = notion_sync_page_for_row(db_id, row, df.columns, matching_page_id)
        logger.info(f"page_res: {page_res}")


test_notion_sync_db = notion_sync_database(
    title="test_page_for_db_creation_v2",
    df=pd.DataFrame([dict(title="a", b=1, c=2)]),
)

__meta_design__ = instances(
    overrides=providers(
        get_s3_client=get_s3_client
    )
)
