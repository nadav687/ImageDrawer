import random
from math import sqrt
from PIL import Image, ImageDraw

from Pixel import Pixel


class ImageCanvas:
    pixel_array = []

    def get_pixel_distance(self, p1, p2):
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

    def get_random_pixel(self, i, j):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        curr_pixel = (r, g, b)
        target_corresponding_pixel = self.target[i][j]

        pixel_dist = self.get_pixel_distance(curr_pixel, target_corresponding_pixel)
        return Pixel(curr_pixel, pixel_dist)



    def __init__(self, height, width, target):
        self.height = height
        self.width = width
        self.target = target
        self.score = 0

        self.pixel_array = self.create_random_array()

        self.avg_pixels_dist = self.get_avg_pixels_dist(self.pixel_array)


    def create_random_array(self):
        pixel_array = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for i, row in enumerate(pixel_array):
            for j, element in enumerate(row):
                pixel_array[i][j] = self.get_random_pixel(i, j)
        return pixel_array

    def get_img_score(self, target):
        count = 0
        for i in range(self.height):
            for j in range(self.width):
                    p1 = self.pixel_array[i][j]
                    p2 = target[i][j]
                    dist = self.get_pixel_distance(p1, p2)

                    if dist < 50 :
                        count += 1
        return count

    def print_image(self):
        img = Image.new("RGB", (self.width, self.height))
        drawer = ImageDraw.Draw(img)

        for y, row in enumerate(self.pixel_array):
            for x, pixel in enumerate(row):
                drawer.point((x, y), fill=pixel.rgb)

        img.show()


    def get_avg_pixels_dist(self, pixel_array):
        sum_dists = 0
        num_of_pixels = len(pixel_array)*len(pixel_array[0])

        for i in range(len(pixel_array)):
            row = []
            for j in range(len(pixel_array[0])):
                sum_dists += pixel_array[i][j].dist

        return sum_dists/num_of_pixels