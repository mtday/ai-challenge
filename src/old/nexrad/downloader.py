
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from pathlib import Path
import urllib.error
import urllib.request


class NexradDownloader(object):
    @staticmethod
    def download(download_dir: str, begin_time: datetime, end_time: datetime, overwrite: bool = False):
        download_path = Path(download_dir).expanduser()
        download_path.mkdir(parents=True, exist_ok=True)
        with ThreadPoolExecutor() as executor:
            time: datetime = begin_time
            futures = []
            while time.timestamp() <= end_time.timestamp():
                output_file = download_path / f"nexrad-{time.isoformat()}.png"
                futures.append(executor.submit(NexradDownloader._download, output_file, time))
                time += timedelta(minutes=5)
            [future.result() for future in futures]

    """
    Example URL:
    https://mesonet.agron.iastate.edu/archive/data/2019/01/01/GIS/uscomp/n0q_201901010000.png
    """
    @staticmethod
    def _download(output_file: Path, time: datetime, overwrite: bool = False):
        if output_file.is_file() and not overwrite:
            return 0  # Skipped downloading of existing file
        day: str = f'{time.year}/{time.month:02d}/{time.day:02d}'
        file_name: str = f'{time.year}{time.month:02d}{time.day:02d}{time.hour:02d}{time.minute:02d}.png'
        url: str = f'https://mesonet.agron.iastate.edu/archive/data/{day}/GIS/uscomp/n0q_{file_name}'
        try:
            with urllib.request.urlopen(url) as response, output_file.open('wb') as out_file:
                out_file.write(response.read())
                print(f'Downloaded: {url} => {output_file}')
                return 200
        except urllib.error.HTTPError as error:
            print(f'Failed: {url} => {error.code}')
            return error.code

