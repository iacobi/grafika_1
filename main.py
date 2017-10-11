from PIL import Image
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Graf_1:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pattern_x_center = 100
        self.pattern_y_center = 200

        self.shards_step = 20

        self.ring_width = 10
        self.ring_blur = 30
        self.total_ring_width = self.ring_width + self.ring_blur
        self.blur_step = int(255 / self.ring_blur)

        self.arg_x = 20
        self.arg_y = 40

        self.primary_color = WHITE
        self.secondary_color = BLACK

        self.pattern_dictionary = {'dots': self.dots,
                                   'shards': self.shards,
                                   'blurred_rings': self.blurred_rings,
                                   'chessboard': self.chessboard,
                                   'chessboard_45': self.chessboard_45}

    def draw_pattern(self, pattern_name):
        im = Image.new("RGB", (self.width, self.height), "white")
        pix = im.load()
        for i in range(0, self.width):
            for j in range(0, self.height):
                pix[i, j] = self.pattern_dictionary[pattern_name](x=i, y=j)
        im.show()

    def distance_from_center(self, x, y):
        return math.sqrt((x - self.pattern_x_center) * (x - self.pattern_x_center) +
                         (y - self.pattern_y_center) * (y - self.pattern_y_center))

    def dots(self, x, y):
        if x < 20 or y < 20:
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

        if (angle / self.shards_step) % 2 == 0:
            return self.primary_color
        else:
            return self.secondary_color

    def blurred_rings(self, x, y):
        dist = self.distance_from_center(x, y)

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

    def chessboard(self, x, y):
        x_d = int((x + self.width) / self.arg_x)
        y_d = int((y + self.height) / self.arg_y)
        if x_d % 2 == y_d % 2:
            return self.primary_color
        else:
            return self.secondary_color

    def chessboard_45(self, x, y):
        return self.chessboard(x * 0.525 - y * 0.525, x * 0.525 + y * 0.525)
#        x_angle = x * 0.525 - y * 0.525
#        y_angle = x * 0.525 + y * 0.525
#        x_d = int((x_angle + self.width) / self.arg_x)
#        y_d = int((y_angle + self.height) / self.arg_y)
#        if x_d % 2 == y_d % 2:
#            return self.primary_color
#        else:
#            return self.secondary_color

    def main(self):
        # self.draw_pattern('shards')
        # self.draw_pattern('blurred_rings')
        self.draw_pattern('chessboard')
        self.draw_pattern('chessboard_45')


graf = Graf_1(500, 500)
graf.main()
