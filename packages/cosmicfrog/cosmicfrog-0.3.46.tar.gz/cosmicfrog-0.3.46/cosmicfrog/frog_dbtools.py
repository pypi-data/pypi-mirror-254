"""
    Wrap platform calls related to model database
"""
import os
import httpx
from .sync_wrapper import sync_wrapper

ATLAS_API_BASE_URL = os.getenv("ATLAS_API_BASE_URL")


async def query_storage_async(app_key: str, storage_name: str):
    assert ATLAS_API_BASE_URL

    url = ATLAS_API_BASE_URL.strip("/")
    url = f"{url}/storage/{storage_name}/connection-string"

    async with httpx.AsyncClient() as client:
        # Call the API to check the status of the job
        headers = {"X-App-KEY": app_key}
        result = await client.get(url, headers=headers, timeout=10)

        if result.status_code != 200:
            return None

        return result.json()


query_storage = sync_wrapper(query_storage_async)


async def get_db_id_async(app_key: str, storage_name: str):
    result = await query_storage_async(app_key, storage_name)

    return result["raw"]["dbname"]


get_db_id = sync_wrapper(get_db_id_async)
