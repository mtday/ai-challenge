
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta
from pathlib import Path
import boto3
import urllib.error
import urllib.request


class NexradArchive(object):
    def __init__(self, archive_dir: Path, station: str):
        self.archive_dir: Path = archive_dir
        self.station: str = station
        self.bucket: str = 'noaa-nexrad-level2'
        self.client = boto3.client('s3')

    def download_day(self, day: date):
        prefix = f'{day.year}/{day.month:02d}/{day.day:02d}/{self.station}'
        summaries: dict = self.client.list_objects_v2(
            Bucket=self.bucket,
            Prefix=prefix,
            MaxKeys=200
        )

        print(f'Key count: {summaries["KeyCount"]}')
        if summaries['KeyCount'] > 0:
            with ThreadPoolExecutor(max_workers=8) as executor:
                for summary in summaries['Contents']:
                    key: str = summary['Key']
                    if not key.endswith('_V06'):
                        print(f'Skipping unrecognized key {key}')
                        continue
                    executor.submit(self._download, summary)

    def _download(self, summary: dict):
        key: str = summary['Key']
        output_path: Path = self.archive_dir / key

        # if the file already exists, we don't attempt to download it again
        if output_path.is_file():
            print(f'{output_path} skipped, already exists locally')

        s3_object = self.client.get_object(
            Bucket=self.bucket,
            Key=key
        )
        with output_path.open('wb') as out_file:
            out_file.write(s3_object.read())

