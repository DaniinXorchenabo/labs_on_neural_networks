from aiostream import stream, pipe
import aiohttp
import asyncio
import aiofiles


async def fetch(session, url: tuple[str, str]):
    url, file_path = url
    async with session.get(url) as resp:
        print(resp.status)
        if 200 <= resp.status < 300:
            async with aiofiles.open(file_path, 'w+b') as f:
                async for chunk in resp.content.iter_chunked(1000):
                    await f.write(chunk)

            return 'ok'
        else:
            return resp.status


async def process(data):
    print(data)


async def download_files(urls: list[tuple[str, str]]):
    if bool(urls):
        async with aiohttp.ClientSession() as session:
            await (stream.repeat(session)
                   | pipe.zip(stream.iterate(urls))
                   | pipe.starmap(fetch, ordered=False, task_limit=10)
                   | pipe.map(process))



if __name__ == '__main__':
    asyncio.new_event_loop().run_until_complete(download_files(
        [
            ('https://raw.githubusercontent.com/kafvtpnz/DeepNN/master/lab1_perceptron/data.csv', "data.csv"),
            ('https://raw.githubusercontent.com/kafvtpnz/DeepNN/master/lab1_perceptron/data_err.csv', "data_err.csv")
        ]
    ))
