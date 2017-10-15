from PatternGenerator import PatternGenerator
from PIL import Image


# def merge_images(image_1, image_2, pattern_name="shards"):
def merge_images(pattern_name="blurred_rings"):
    width = 100
    height = 500

    # reading images
#     image_1 = Image.new("RGB", (width, height), "red")
#     image_2 = Image.new("RGB", (width, height), "green")
    image_1 = Image.open("palac.jpg")
    image_2 = Image.open("palac2.jpg")
    width, height = image_1.size
    pattern_image = PatternGenerator(width, height).generate_pattern_image(pattern_name).load()
    final_image = Image.new("RGB", (width, height), "white")
    final_image_pix = final_image.load()
    im_1 = image_1.load()
    im_2 = image_2.load()
    for x in range(width):
        for y in range(height):
            final_image_pix[x, y] = merge_pixel(im_1[x, y], im_2[x, y], pattern_image[x, y])
    final_image.show()


def paste_pattern(image_string, pattern_name):
    image = Image.open(image_string)
    width, height = image.size

    pattern_image = PatternGenerator(width, height).generate_pattern_image(pattern_name).load()
    final_image = Image.new("RGB", (width, height), "white")
    final_image_pix = final_image.load()
    im_1 = image.load()
    for x in range(width):
        for y in range(height):
            final_image_pix[x, y] = merge_pixel(im_1[x, y], pattern_image[x, y], pattern_image[x, y])
    final_image.show()


def merge_pixel(image_1_tuple, image_2_tuple, pattern_tuple):
    # bierzemy tylko pod uwage czerwony bo zakladamy, ze pattern jest w skali szarosci
    pattern = float(pattern_tuple[0]) / 255
    return tuple([int(pattern * image_1_tuple[i] + (1 - pattern) * image_2_tuple[i]) for i in range(3)])


def check(start, length, index):
    if index >= (length + start):
        return check(start + length, length * 2, index)
    else:
        if index >= ((length / 2 + start)):
            return True
        else:
            return False

# p_generator = PatternGenerator(500, 500)
#
# p_generator.generate_pattern_image('shards').show()
# p_generator.generate_pattern_image('blurred_rings').show()
# p_generator.generate_pattern_image('chessboard').show()
# p_generator.generate_pattern_image('chessboard_45').show()
# p_generator.generate_pattern_image('grid').show()
# p_generator.generate_pattern_image('dots').show()
# p_generator.generate_pattern_image('ring_grid').show()
# p_generator.generate_pattern_image('concentric').show()

# merge_images(pattern_name="chessboard_45")

# paste_pattern(image_string="palac.jpg", pattern_name="blurred_rings")
# merge_images()
PatternGenerator(500, 500).generate_pattern_image("concentric").show()
