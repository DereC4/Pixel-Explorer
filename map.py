# import noise
# import random
# from PIL import Image

from pynoise.noisemodule import *
from pynoise.noiseutil import *

width, height = 512, 512
perlin = Perlin()
noise_map = noise_map_plane(width, height, 2, 6, 1, 5, perlin)
gradient = grayscale_gradient()

render = RenderImage()
render.render(noise_map, width, height, 'perlin.png', gradient)