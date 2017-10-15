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
        self.pattern_x_center = int(width / 2)
        self.pattern_y_center = int(height / 2)

        self.ring_width = 10
        self.ring_blur = 30
        self.total_ring_width = self.ring_width + self.ring_blur
        self.blur_step = int(255 / self.ring_blur)

        self.arg_x = 90
        self.arg_y = 90

        self.step = 20

        self.primary_color = BLACK
        self.secondary_color = WHITE

        self.pattern_dictionary = {'dots': self.dots,
                                   'shards': self.shards,
                                   'blurred_rings': self.blurred_rings,
                                   'grid': self.grid,
                                   'chessboard': self.chessboard,
                                   'chessboard_45': self.chessboard_45,
                                   'ring_grid': self.ring_grid,
                                   'concentric': self.concentric}

    def set_x_y_step(self, x, y, step):
        self.arg_x = x
        self.arg_y = y
        self.step = step

    def set_colors(self, primary=BLACK, secondary=WHITE):
        self.primary_color = primary
        self.secondary_color = secondary

    def set_ring_blur(self, width, blur):
        self.ring_width = width
        self.ring_blur = blur
        self.total_ring_width = self.ring_width + self.ring_blur
        self.blur_step = int(255 / self.ring_blur)

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
                return self.primary_color
        else:
            d = -1 * d
            if d % self.arg_x < self.step:
                return self.primary_color

        d = y_c - y
        if d > 0:
            if d % self.arg_y >= box_y:
                return self.primary_color
        else:
            d = -1 * d
            if d % self.arg_y < self.step:
                return self.primary_color

        return self.secondary_color

    def chessboard(self, x, y):
        "arg_x: field width, arg_y: field_height"
        x_d = int((x + 2*self.width) / self.arg_x)
        y_d = int((y + 2*self.height) / self.arg_y)
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
        dist = self.distance_from(
            x=x, y=y, x_c=self.pattern_x_center, y_c=self.pattern_y_center)
        radius = 1

        r_index = int(dist) / radius

        if self.check(0, 2, int(dist)):
            return self.primary_color
        else:
            return self.secondary_color

    def check(self, start, length, index):
        if index >= (length + start):
            return self.check(start + length, length + 2, index)
        else:
            if index >= (length / 2 + start):
                return True
            else:
                return False
