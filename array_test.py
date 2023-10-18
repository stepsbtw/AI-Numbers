import numpy
from PIL import Image
import old_crop_data

images_list = old_crop_data.images_list()
image = images_list[0][0].convert('L')

print(numpy.asfortranarray(image))
