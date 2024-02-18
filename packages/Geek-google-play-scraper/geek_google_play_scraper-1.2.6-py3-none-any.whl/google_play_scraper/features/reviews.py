import json
import aiohttp
import asyncio
from typing import List, Optional, Tuple

from google_play_scraper import Sort
from google_play_scraper.constants.element import ElementSpecs
from google_play_scraper.constants.regex import Regex
from google_play_scraper.constants.request import Formats

MAX_COUNT_EACH_FETCH = 199


class _ContinuationToken:
    __slots__ = "token", "lang", "country", "sort", "count", "filter_score_with"

    def __init__(self, token, lang, country, sort, count, filter_score_with):
        self.token = token
        self.lang = lang
        self.country = country
        self.sort = sort
        self.count = count
        self.filter_score_with = filter_score_with


async def _fetch_review_items(
    session: aiohttp.ClientSession,
    url: str,
    app_id: str,
    sort: int,
    count: int,
    filter_score_with: Optional[int],
    pagination_token: Optional[str],
):
    async with session.post(
        url,
        data=Formats.Reviews.build_body(
            app_id,
            sort,
            count,
            "null" if filter_score_with is None else filter_score_with,
            pagination_token,
        ),
        headers={"content-type": "application/x-www-form-urlencoded"},
    ) as resp:
        dom = await resp.text()

    match = json.loads(Regex.REVIEWS.findall(dom)[0])

    return json.loads(match[0][2])[0], json.loads(match[0][2])[-1][-1]


async def reviews(
    session: aiohttp.ClientSession,
    app_id: str,
    lang: str = "en",
    country: str = "us",
    sort: Sort = Sort.NEWEST,
    count: int = 100,
    filter_score_with: int = None,
    continuation_token: _ContinuationToken = None,
) -> Tuple[List[dict], _ContinuationToken]:
    if continuation_token is not None:
        token = continuation_token.token

        if token is None:
            return (
                [],
                continuation_token,
            )

        lang = continuation_token.lang
        country = continuation_token.country
        sort = continuation_token.sort
        count = continuation_token.count
        filter_score_with = continuation_token.filter_score_with
    else:
        token = None

    url = Formats.Reviews.build(lang=lang, country=country)

    _fetch_count = count

    result = []

    while True:
        if _fetch_count == 0:
            break

        if _fetch_count > MAX_COUNT_EACH_FETCH:
            _fetch_count = MAX_COUNT_EACH_FETCH

        try:
            review_items, token = await _fetch_review_items(
                session, url, app_id, sort, _fetch_count, filter_score_with, token
            )
        except (TypeError, IndexError):
            token = None
            break

        for review in review_items:
            result.append(
                {
                    k: spec.extract_content(review)
                    for k, spec in ElementSpecs.Review.items()
                }
            )

        _fetch_count = count - len(result)

        if isinstance(token, list):
            token = None
            break

    return (
        result,
        _ContinuationToken(token, lang, country, sort, count, filter_score_with),
    )


async def reviews_all(app_id: str, sleep_milliseconds: int = 0, **kwargs) -> list:
    kwargs.pop("count", None)
    kwargs.pop("continuation_token", None)

    continuation_token = None

    result = []

    async with aiohttp.ClientSession() as session:
        while True:
            _result, continuation_token = await reviews(
                session,
                app_id,
                count=MAX_COUNT_EACH_FETCH,
                continuation_token=continuation_token,
                **kwargs
            )

            result += _result

            if continuation_token.token is None:
                break

            if sleep_milliseconds:
                await asyncio.sleep(sleep_milliseconds / 1000)

    return result
