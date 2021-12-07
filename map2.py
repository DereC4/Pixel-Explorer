import noise
import random
from PIL import Image

octaves = 4
frequency = 100*octaves
seed = random.uniform(-10000,10000)
img = Image.new( 'RGB', (1000,1000), "black")
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        height = int(noise.snoise3(i/frequency, j/frequency, seed, octaves) * 127 + 128)
        if height < 150: #water
            pixels[i,j] = (0, 0, 128)

img.show()