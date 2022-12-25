from PIL import Image, ImageDraw


class ChildImage:
    pixel_array = []

    def __init__(self, pixels):
        self.pixel_array = pixels
        self.height = len(pixels)
        self.width = len(pixels[0])
        self.avg_pixels_dist = self.get_avg_pixels_dist(pixels)

    def print_image(self):
        img = Image.new("RGB", (self.width, self.height))
        drawer = ImageDraw.Draw(img)

        for y, row in enumerate(self.pixel_array):
            for x, pixel in enumerate(row):
                drawer.point((x, y), fill=pixel.rgb)

        img.show()

    def get_avg_pixels_dist(self, pixel_array):
        sum_dists = 0
        num_of_pixels = len(pixel_array) * len(pixel_array[0])

        for i in range(len(pixel_array)):
            for j in range(len(pixel_array[0])):
                sum_dists += pixel_array[i][j].dist

        return sum_dists / num_of_pixels