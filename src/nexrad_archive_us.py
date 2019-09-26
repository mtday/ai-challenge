
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from pathlib import Path
import urllib.error
import urllib.request


class NexradArchive(object):
    def __init__(self):
        self.archive_dir: Path = Path('/opt/nexrad-archive')
        self.archive_dir.mkdir(parents=True, exist_ok=True)

    """
    Delete all images in the archive.
    """
    def clear(self):
        for image_file in self.archive_dir.iterdir():
            image_file.delete()

    """
    Download a batch of images files from [begin_time, end_time] inclusive.
    """
    def download_batch(self, begin_time: datetime, end_time: datetime):
        with ThreadPoolExecutor(max_workers=8) as executor:
            time: datetime = begin_time
            while time.timestamp() <= end_time.timestamp():
                file_name: str = f'{time.year}{time.month:02d}{time.day:02d}{time.hour:02d}{time.minute:02d}.png'
                output_file: Path = self.archive_dir / file_name
                executor.submit(self._download, output_file, time)
                time += timedelta(minutes=5)

    """
    Downloads a single file from the online archive.
    Example URL: https://mesonet.agron.iastate.edu/archive/data/2019/01/01/GIS/uscomp/n0q_201901010000.png
    """
    def _download(self, output_file: Path, time: datetime):
        # if the file already exists, we don't attempt to download it again
        if output_file.is_file():
            print(f'{output_file} skipped, already exists locally')
            return 0
        day: str = f'{time.year}/{time.month:02d}/{time.day:02d}'
        image: str = f'{time.year}{time.month:02d}{time.day:02d}{time.hour:02d}{time.minute:02d}.png'
        url: str = f'https://mesonet.agron.iastate.edu/archive/data/{day}/GIS/uscomp/n0q_{image}'
        try:
            with urllib.request.urlopen(url) as response, output_file.open('wb') as out_file:
                out_file.write(response.read())
                print(f'{output_file} downloaded')
                return 200
        except urllib.error.HTTPError as error:
            print(f'Failed: {url} => {error.code}')
            return error.code

