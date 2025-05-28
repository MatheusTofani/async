import asyncio
import httpx


async def http_call_async( request ):
    for num in range(1, 11):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)
