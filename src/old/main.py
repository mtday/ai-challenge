
from nexrad import NexradDownloader
from datetime import datetime


class Main(object):
    @staticmethod
    def download_nexrad_images():
        download_dir: str = '/tmp'
        begin_time = datetime.strptime('2019-01-01 00:00', '%Y-%m-%d %H:%M')
        end_time = datetime.strptime('2019-01-01 00:05', '%Y-%m-%d %H:%M')
        NexradDownloader.download(download_dir, begin_time, end_time)


if __name__ == "__main__":
    Main.download_nexrad_images()

