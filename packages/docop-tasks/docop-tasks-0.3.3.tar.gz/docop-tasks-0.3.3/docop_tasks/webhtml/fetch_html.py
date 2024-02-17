"""fetch and store HTML from source URLs.
input: a source with some resources
output: documents with 'reference', 'title', 'html' and 'uuid' fields
"""

import asyncio
import uuid
import hashlib
from urllib.parse import urlparse
from playwright.async_api import async_playwright
from rich import print
from rich.progress import track
from yamlstore import Document


if not source:
   raise Exception("no source given")

if not source["resources"]:
   raise Exception("no resources given")


async def main():

    urls = source["resources"]

    async with async_playwright() as pw:

        browser = await pw.webkit.launch()
        page = await browser.new_page()
        titles = []
        
        for url in track(urls, description=f" ↳ fetching, rendering and extracting HTML from {len(urls)} urls", transient=True):
            await page.goto(url)
            title = await page.title()
            titles.append(title)
            html = await page.content()
            doc = Document(title=title)
            doc["reference"] = url
            doc["title"] = title
            doc["type"] = "html"
            doc["html"] = html
            baseurl = urlparse(url).netloc
            namespace = uuid.UUID(hashlib.md5(baseurl.encode('utf-8')).hexdigest())
            doc["uuid"] = str(uuid.uuid5(namespace, url))
            global collection
            collection += doc

        for title in titles:
            print(f" ↳ '{title}' ✅")

    await browser.close()

asyncio.run(main())
