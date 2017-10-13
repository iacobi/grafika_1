from PatternGenerator import PatternGenerator


# def paste_pattern(self, image, pattern_name):
#     pattern_image = sefl.generate_pattern_image(pattern_name)
#
#
# def present_patterns(self, image):
#     for pattern_name in self.pattern_dictionary.keys():
#         modified_image = self.paste_pattern(image, pattern_name)
#         # save modified image


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


# def paste_pattern(base_image, pattern_name):
    # get width/height from base image
    # print('paster')
    # PatternGenerator


p_generator = PatternGenerator(500, 500)

p_generator.generate_pattern_image('shards').show()
p_generator.generate_pattern_image('blurred_rings').show()
p_generator.generate_pattern_image('chessboard').show()
p_generator.generate_pattern_image('chessboard_45').show()
p_generator.generate_pattern_image('grid').show()
p_generator.generate_pattern_image('dots').show()
p_generator.generate_pattern_image('ring_grid').show()
p_generator.generate_pattern_image('concentric').show()
