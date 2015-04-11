import indicoio
import skimage.io
indicoio.config.api_key = "5daca1bb2437922364bfae1c7d733109"
import os
path = os.path.abspath('kevin.png')
pixel_array = skimage.io.imread(path).tolist()
from indicoio import fer, batch_fer, image_features
print(fer(pixel_array))
#print(image_features(pixel_array))