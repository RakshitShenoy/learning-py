from pathlib import Path#import that helps with the path of the image that we choose
import imageio.v3 as iio #starting import that helps with importing screenshots aka jpg files from ur own device

base_dir = Path(__file__).resolve().parent
filenames = [base_dir / 'gif6.jpg', base_dir / 'gif5.jpg']
images = [iio.imread(filename) for filename in filenames]

iio.imwrite(base_dir / 'meyip.gif', images, duration=500, loop=0)#this line shows the duration and how long and how will the imgaes change
print(f'GIF saved to: {base_dir / "meyip.gif"}')#end
