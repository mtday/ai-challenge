
from botocore import UNSIGNED
from botocore.client import Config
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
        self.client = boto3.client('s3', config=Config(signature_version=UNSIGNED))

    def download_day(self, day: date):
        prefix: str = f'{day.year}/{day.month:02d}/{day.day:02d}/{self.station}'

        key: str = ''
        done: bool = False
        while not done:
            summaries: dict = self.client.list_objects_v2(
                    Bucket=self.bucket, Prefix=prefix, StartAfter=key, MaxKeys=25)
            if summaries['KeyCount'] > 0:
                with ThreadPoolExecutor(max_workers=8) as executor:
                    for summary in summaries['Contents']:
                        key = summary['Key']
                        if key.endswith('_V06'):
                            executor.submit(self.download_file, summary)
                        elif not key.endswith('_V06_MDM'):
                            print(f'Skipping unrecognized key {key}')
            # stop once the batch is not truncated
            done = not summaries['IsTruncated']

    def download_file(self, summary: dict):
        key: str = summary['Key']
        filename: str = key.split('/')[-1]
        output_path: Path = self.archive_dir / filename

        # if the file already exists, we don't attempt to download it again
        if not output_path.is_file():
            s3_object: dict = self.client.get_object(Bucket=self.bucket, Key=key)
            with output_path.open('wb') as out_file:
                out_file.write(s3_object['Body'].read())
            print(f'Downloaded {output_path}')

