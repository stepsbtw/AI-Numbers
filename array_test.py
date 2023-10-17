import numpy
from PIL import Image
import crop_data

images_list = crop_data.images_list()
image = images_list[0][0]

image.show()

print(numpy.array(image))
Image.fromarray(numpy.array(image)).show()
