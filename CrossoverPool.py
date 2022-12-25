import random

from ChildImage import ChildImage
from RandomImage import ImageCanvas


class Pool:
    def __init__(self, population, gen_number):
        self.population = population
        self.population_size = len(population)
        self.gen_number = gen_number

    def get_best_ones(self, percent):
        size = round(len(self.population) * percent)
        print("size of best ones : ", size)
        sorted_instances = sorted(self.population, key=lambda x: x.avg_pixels_dist, reverse=False)
        return sorted_instances[:size]

    def get_random_pairs(self, elements):
        tuples = []
        for element in elements:
            neighbors = random.sample(elements, k=5)  # select 4 random neighbors
            for neighbor in neighbors:
                tuples.append((element, neighbor))  # create a tuple for each element and its neighbor
        return tuples

    def create_child(self, img1, img2):
        pixels = []
        score = 0

        for i in range(img1.height):
            row = []
            for j in range(img1.width):
                coin_toss = random.random()
                if coin_toss < 0.5:
                    element = img1.pixel_array[i][j]
                else:
                    element = img2.pixel_array[i][j]

                row.append(element)
            pixels.append(row)

        return ChildImage(pixels)

    def create_next_gen(self, best_ones_pairs):
        next_gen = []

        for pair in best_ones_pairs:
            next_gen.append(self.create_child(pair[0], pair[1]))
        self.gen_number += 1
        self.population = next_gen


