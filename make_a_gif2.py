from pathlib import Path
import imageio.v3 as iio

base_dir = Path(__file__).resolve().parent
filenames = [base_dir / 'gif6.jpg', base_dir / 'gif5.jpg']
images = [iio.imread(filename) for filename in filenames]

iio.imwrite(base_dir / 'meyip.gif', images, duration=500, loop=0)
print(f'GIF saved to: {base_dir / "meyip.gif"}')