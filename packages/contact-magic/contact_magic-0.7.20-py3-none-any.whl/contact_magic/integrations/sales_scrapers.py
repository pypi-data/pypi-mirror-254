import asyncio
import logging

import httpx

from contact_magic.conf.settings import SETTINGS
from contact_magic.dict_utils import get_first_level_items
from contact_magic.logger import logger
from contact_magic.utils import fix_website

logging.getLogger("httpx").setLevel(logging.WARNING)

base_url = "https://salesscrapers.dev/api/"


async def make_sales_scraper_request(endpoint, data: dict, max_retries=3):
    if not SETTINGS.SALES_SCRAPERS_API_KEY:
        return None
    headers = {
        "Accept": "application/json",
        "X-API-Key": SETTINGS.SALES_SCRAPERS_API_KEY,
    }

    url = f"{base_url}{endpoint}"
    try:
        retries = 0
        params = get_first_level_items(data)
        while retries < max_retries:
            res = await poll_until_job_complete(url, headers, params)
            if not res:
                return {}
            # authorization error so can break
            if res.get("job_status_code") == 401:
                logger.warning("sales_scraper_error", message=res.get("job_data"))
                break
            if res.get("job_status_code") == 400:
                logger.warning("proxy_error", message=res.get("job_data"))
            if res.get("job_status_code") == 200:
                return res.get("job_data")
            if res.get("job_status_code") == 422:
                validation_errors = res.get("job_data").get("detail")
                for error in validation_errors:
                    if error.get("type") == "value_error.url.scheme":
                        error_key = error.get("loc")[1]
                        if error_key in data:
                            params[error_key] = fix_website(data[error_key])
            retries += 1
        return None
    except Exception:
        return None


async def poll_until_job_complete(url, headers, params) -> dict:
    new_job = await create_new_job(url, headers, params)
    # raise auth error from SS or validation error
    if new_job.status_code == 422:
        return {"job_status_code": new_job.status_code, "job_data": new_job.json()}
    if new_job.status_code != 200:
        return {"job_status_code": new_job.status_code, "job_data": new_job.text}
    new_job_id = new_job.json().get("job_id")
    job_is_pending = True
    count_sleep = 0
    max_wait_rotations = 150
    while job_is_pending:
        if count_sleep >= max_wait_rotations:
            return {}
        job_status = await get_job_status(new_job_id, headers)
        if job_status.get("job_status") == "SUCCESS":
            return job_status
        await asyncio.sleep(15)
        count_sleep += 1
    return {}


async def create_new_job(url, headers, params):
    """
    Create new job in Salescrapers. This returns
    {
      "job_id": "f41ecfb9-78b2-4214-b503-444634550ec4",
      "job_status": "SUCCESS",
      "job_status_code": 200,
      "job_data": {}
      }
    :param url:
    :param headers:
    :param params:
    :return:
    """
    async with httpx.AsyncClient(timeout=httpx.Timeout(300.0)) as session:
        res = await session.request(
            method="get", url=url, headers=headers, params=params
        )
        return res


async def get_job_status(job_id, headers) -> dict:
    """
    Get job status in Salescrapers. This returns
    {
      "job_id": "f41ecfb9-78b2-4214-b503-444634550ec4",
      "job_status": "SUCCESS",
      "job_status_code": 200,
      "job_data": {}
      }
    """
    async with httpx.AsyncClient(timeout=httpx.Timeout(300.0)) as session:
        res = await session.request(
            method="get", url=f"{base_url}job-status/{job_id}", headers=headers
        )
        return res.json()


async def get_custom_scrapers():
    async with httpx.AsyncClient(timeout=httpx.Timeout(300.0)) as session:
        headers = {
            "Accept": "application/json",
            "X-API-Key": SETTINGS.SALES_SCRAPERS_API_KEY,
        }
        res = await session.request(
            method="get", url=base_url + "custom-scrapers", headers=headers
        )
        return res.json()
