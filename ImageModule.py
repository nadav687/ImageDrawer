from math import sqrt
from tkinter import *
import numpy as np
from PIL import Image, ImageDraw

from CrossoverPool import Pool
from RandomImage import ImageCanvas

def get_target_image_array(path):
    img = Image.open(path)
    img.load()

    pixel_values = list(img.getdata())
    return convert_to_touple(np.array(pixel_values).reshape((img.height, img.width, 3)))

def convert_to_touple(array3d):
    new_arr = []
    for outer_arr in array3d:
        # Create a new sublist to hold the tuple elements
        inner_arr = []
        # Iterate over the outer array
        for inner in outer_arr:
            # Convert the inner array to a tuple and append it to the inner sublist
            inner_arr.append(tuple(inner))
        # Append the inner sublist to the new array
        new_arr.append(inner_arr)
    return new_arr



path = "C:/BGU/Mini/input3.png"
mona_lisa = get_target_image_array(path)

height = len(mona_lisa)
width = len(mona_lisa[0])

print("height: ", height)
print("width: ",width)


random_images = []

for i in range(1000):
    img_canvas = ImageCanvas(height, width, mona_lisa)
    random_images.append(img_canvas)



gen_number = 0
pool = Pool(random_images, gen_number)

while pool.gen_number < 1000:
    best_ones = pool.get_best_ones(0.2)
    pairs = pool.get_random_pairs(best_ones)
    pool.create_next_gen(pairs)
    if pool.gen_number % 50 == 0:
        best_ones[0].print_image()

    gen_avg_score = 0
    for i in range(pool.population_size):
        gen_avg_score += pool.population[i].avg_pixels_dist
    gen_avg_score /= pool.population_size
    print("gen: ",pool.gen_number, "  avg score: ", gen_avg_score)


exit()




