# 세션 유지 > 세션 안에서 reuqest를 통해 데이터 긁어오기
import aiohttp
import time
import asyncio


async def fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


# fetcher는 해당하는 세션에 url을 보내고, 데이터를 가져옴

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)  # 2.5
