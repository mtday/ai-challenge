
from functools import reduce
from pathlib import Path

image_dir = Path('/home/mday/Source/ai-challenge/nexrad-archive')
size_and_count = ((path.stat().st_size, 1) for path in image_dir.iterdir())
total_size, total_count = reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]), size_and_count)
average_image_size = total_size / total_count
print(f'Average image size: {average_image_size} (bytes)')

images_per_hour = 60 / 5  # one every 5 minutes
images_per_day = images_per_hour * 24
images_per_month = images_per_day * 30
images_per_year = images_per_day * 365
size_per_month_gigs = images_per_month * average_image_size / 1024 / 1024 / 1024
print(f'Size needed for 1 month: {size_per_month_gigs:.02f} (gb)')
size_per_year_gigs = images_per_year * average_image_size / 1024 / 1024 / 1024
print(f'Size needed for 1 year: {size_per_year_gigs:.02f} (gb)')

