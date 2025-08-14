import asyncio
from crawl4ai import AsyncWebCrawler

async def run_crawler(target_url: str):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=target_url)
        return {
            "url": target_url,
            "content": result.markdown,
            "success": True,
            "error": None
        }
