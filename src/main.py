
from nexrad_archive import NexradArchive
from datetime import date
from pathlib import Path


archive_dir: Path = Path('/opt/nexrad-archive')
station: str = 'KHTX'
nexrad_archive: NexradArchive = NexradArchive(archive_dir, station)

day = date(2019, 1, 1)
nexrad_archive.download_day(day)

