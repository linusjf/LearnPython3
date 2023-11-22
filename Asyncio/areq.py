#!/usr/bin/env python
"""
Areq.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : areq
# @created     : Wednesday Nov 22, 2023 06:04:41 IST
# @description : Asynchronously get links embedded in multiple pages' HMTL.
# -*- coding: utf-8 -*-'
######################################################################
"""
# areq.py
import pathlib
import sys
import asyncio
import logging
import re
from typing import IO
import urllib.error
import urllib.parse
import aiofiles
import aiohttp
from aiohttp import ClientSession


logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)
logger = logging.getLogger("areq")
logging.getLogger("chardet.charsetprober").disabled = True

HREF_RE = re.compile(r'href="(.*?)"')


async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
    """GET request wrapper to fetch page HTML.

    kwargs are passed to `session.request()`.
    """

    resp = await session.request(method="GET", url=url, **kwargs)
    resp.raise_for_status()
    logger.info("Got response [%s] for URL: %s", resp.status, url)
    html = await resp.text()
    return html


async def parse(url: str, session: ClientSession, **kwargs) -> set:
    """Find HREFs in the HTML of `url`."""
    found = set()
    try:
        html = await fetch_html(url=url, session=session, **kwargs)
    except (
        aiohttp.ClientError,
        aiohttp.http_exceptions.HttpProcessingError,
    ) as exc:
        logger.error(
            "aiohttp exception for %s [%s]: %s",
            url,
            getattr(exc, "status", None),
            getattr(exc, "message", None),
        )
        return found
    except Exception as exc:  # pylint: disable=broad-except
        logger.exception(
            "Non-aiohttp exception occured:  %s", getattr(exc, "__dict__", {})
        )
        return found
    else:
        for link in HREF_RE.findall(html):
            try:
                abslink = urllib.parse.urljoin(url, link)
            except (urllib.error.URLError, ValueError):
                logger.exception("Error parsing URL: %s", link)
            else:
                found.add(abslink)
        logger.info("Found %d links for %s", len(found), url)
        return found


async def write_one(file: IO, url: str, **kwargs) -> None:
    """Write the found HREFs from `url` to `file`."""
    res = await parse(url=url, **kwargs)
    if not res:
        return None
    async with aiofiles.open(file, 'a', encoding="UTF-8") as openfile:
        for _ in res:
            await openfile.write(f"{url}\t{_}\n")
        logger.info("Wrote results for source URL: %s", url)


async def bulk_crawl_and_write(file: IO, _urls: set, **kwargs) -> None:
    """Crawl & write concurrently to `file` for multiple `urls`."""
    async with ClientSession() as session:
        tasks = []
        for url in _urls:
            tasks.append(
                write_one(file=file, url=url, session=session, **kwargs)
            )
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    assert sys.version_info >= (3, 7), "Script requires Python 3.7+."
    here = pathlib.Path(__file__).parent

    with open(here.joinpath("urls.txt"), encoding='UTF-8') as infile:
        urls = set(map(str.strip, infile))

    outpath = here.joinpath("foundurls.txt")
    with open(outpath, "w", encoding="UTF-8") as outfile:
        outfile.write("source_url\tparsed_url\n")

    asyncio.run(bulk_crawl_and_write(file=outpath, _urls=urls))
