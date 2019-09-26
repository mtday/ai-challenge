
from nexrad_archive import NexradArchive
from nexrad_image import NexradImage
from datetime import date
from matplotlib import pyplot as plt
from pathlib import Path
from pyart.core import Radar
from pyart.graph import RadarDisplay
from pyart.io import read_nexrad_archive


archive_dir: Path = Path('/opt/nexrad-archive')
station: str = 'KHTX'
nexrad_archive: NexradArchive = NexradArchive(archive_dir, station)

#day: date = date(2019, 1, 1)
#nexrad_archive.download_day(day)
nexrad_file: Path = Path('/opt/nexrad-archive/KHTX20190101_000336_V06')
image_file: Path = Path('/tmp/nexrad.png')
NexradImage.create_image_file(nexrad_file, image_file)

#paths: list = nexrad_archive.get_paths()
#if len(paths) > 0:
#    path: Path = paths[0]
#    radar: Radar = read_nexrad_archive(str(path))
#    display: RadarDisplay = RadarDisplay(radar)
#    fig = plt.figure(figsize=(6, 5))
#
#    # plot super resolution reflectivity
#    ax = fig.add_subplot(111)
#    display.plot('reflectivity', 0, title='NEXRAD Reflectivity',
#                 vmin=-32, vmax=64, colorbar_label='', ax=ax)
#    display.plot_range_ring(radar.range['data'][-1]/1000., ax=ax)
#    display.set_limits(xlim=(-500, 500), ylim=(-500, 500), ax=ax)
#    plt.savefig('nexrad.png')
#
