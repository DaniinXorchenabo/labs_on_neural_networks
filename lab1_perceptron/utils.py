from os.path import dirname, join, split, isdir
from os import makedirs
import asyncio

from download_data import download_files


async def download_files_for_lab1():
    base_file_path = join(dirname(dirname(__file__)), 'data', 'lab1')
    if not isdir(base_file_path):
        makedirs(base_file_path)
    filenames = ["data.csv", "data_err.csv"]
    await download_files(
        _p := [(f'https://raw.githubusercontent.com/kafvtpnz/DeepNN/master/lab1_perceptron/{i}',
                join(base_file_path, i)) for i in filenames]
    )
    print(*_p, sep='\n')


if __name__ == '__main__':
    asyncio.new_event_loop().run_until_complete(download_files_for_lab1())
