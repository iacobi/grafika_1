from PIL import Image
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class PatternGenerator:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pattern_x_center = 250
        self.pattern_y_center = 250

        self.ring_width = 10
        self.ring_blur = 30
        self.total_ring_width = self.ring_width + self.ring_blur
        self.blur_step = int(255 / self.ring_blur)

        self.arg_x = 90
        self.arg_y = 90

        self.step = 20

        self.primary_color = GREEN
        self.secondary_color = BLACK

        self.pattern_dictionary = {'dots': self.dots,
                                   'shards': self.shards,
                                   'blurred_rings': self.blurred_rings,
                                   'grid': self.grid,
                                   'chessboard': self.chessboard,
                                   'chessboard_45': self.chessboard_45,
                                   'ring_grid': self.ring_grid,
                                   'concentric': self.concentric}

    def generate_pattern_image(self, pattern_name):
        im = Image.new("RGB", (self.width, self.height), "white")
        pix = im.load()
        for i in range(0, self.width):
            for j in range(0, self.height):
                pix[i, j] = self.pattern_dictionary[pattern_name](x=i, y=j)
        return im

    def distance_from(self, x, y, x_c, y_c):
        return math.sqrt((x - x_c) * (x - x_c) + (y - y_c) * (y - y_c))

    def blurred_rings(self, x, y):
        dist = self.distance_from(
            x=x, y=y, x_c=self.pattern_x_center, y_c=self.pattern_y_center)

        ring_index = int(dist / self.total_ring_width)
        ring_mod = int(dist % self.total_ring_width)

        color_value = 0

        if ring_index % 2 == 0:
            if ring_mod < self.ring_width:
                color_value = 0
            else:
                color_value = int(
                    min(0 + (ring_mod - self.ring_width) * self.blur_step, 255))
        else:
            if ring_mod < self.ring_width:
                color_value = 255
            else:
                color_value = int(
                    max(255 - (ring_mod - self.ring_width) * self.blur_step, 0))

        return (color_value, color_value, color_value)

    def grid(self, x, y):
        "step: border width , arg_x: x distance between fields, arg_y: y distance between fields"
        box_x = self.arg_x - self.step
        box_y = self.arg_y - self.step
        # przesuwamy srodek na krawedz pola kratki
        x_c = self.width / 2 - self.arg_x / 2
        y_c = self.height / 2 - self.arg_y / 2

        d = x_c - x
        if d > 0:
            if d % self.arg_x >= box_x:
                return self.secondary_color
        else:
            d = -1 * d
            if d % self.arg_x < self.step:
                return self.secondary_color

        d = y_c - y
        if d > 0:
            if d % self.arg_y >= box_y:
                return self.secondary_color
        else:
            d = -1 * d
            if d % self.arg_y < self.step:
                return self.secondary_color

        return self.primary_color

    def chessboard(self, x, y):
        "arg_x: field width, arg_y: field_height"
        x_d = int((x + self.width) / self.arg_x)
        y_d = int((y + self.height) / self.arg_y)
        if x_d % 2 == y_d % 2:
            return self.primary_color
        else:
            return self.secondary_color

    def chessboard_45(self, x, y):
        return self.chessboard(x * 0.525 - y * 0.525, x * 0.525 + y * 0.525)

    def dots(self, x, y):
        # uses arg_x twice
        x_d = int(abs((x - self.pattern_x_center) % self.arg_x * 2))
        y_d = int(abs((y - self.pattern_x_center) % self.arg_x * 2))
        dist = self.distance_from(x_d, y_d, self.arg_x, self.arg_y)
        if (dist < self.arg_x - self.step):
            return self.primary_color
        else:
            return self.secondary_color

    def ring_grid(self, x, y):
        # uses arg_x twice
        x_d = int(abs((x - self.pattern_x_center) % self.arg_x * 2))
        y_d = int(abs((y - self.pattern_x_center) % self.arg_x * 2))
        dist = self.distance_from(x_d, y_d, self.arg_x, self.arg_y)
        if (int(dist) / int(self.arg_x / 5)) % 2 == 0:
            return self.primary_color
        else:
            return self.secondary_color

    def shards(self, x, y):
        theta = math.atan2(self.pattern_y_center - y,
                           self.pattern_x_center - x)
        # theta += math.pi/2
        angle = int(math.degrees(theta))

        if (angle < 360):
            angle = angle + 360

        if (angle / self.step) % 2 == 0:
            return self.primary_color
        else:
            return self.secondary_color

    def concentric(self, x, y):
        # FIX THIS PROMPTLY !!!!
        dist = self.distance_from(
            x=x, y=y, x_c=self.pattern_x_center, y_c=self.pattern_y_center)
        w = int(0.05 * dist) + 1
        if dist == 0:
            w = 1
        r = int(dist) / w

        if r % 2 == 0:
            return self.primary_color
        else:
            return self.secondary_color

    def main(self):
        # self.generate_pattern_image('shards').show()
        # self.generate_pattern_image('blurred_rings').show()
        # self.generate_pattern_image('chessboard').show()
        # self.generate_pattern_image('chessboard_45').show()
        # self.generate_pattern_image('grid').show()
        # self.generate_pattern_image('dots').show()
        # self.generate_pattern_image('ring_grid').show()
        # self.generate_pattern_image('concentric').show()
        print('LOGGER: CORRECT')


p_generator = PatternGenerator(500, 500)
p_generator.main()
p_generator.generate_pattern_image('grid').show()
