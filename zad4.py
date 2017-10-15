from PatternGenerator import PatternGenerator
from PIL import Image


pattern_dictionary = ['dots', 'shards', 'blurred_rings', 'grid',
                      'chessboard', 'chessboard_45', 'ring_grid', 'concentric']


def merge_images(image_1_path, image_2_path, pattern_name):
    image_1 = Image.open(image_1_path)
    image_2 = Image.open(image_2_path)
    width, height = image_1.size
    generator = PatternGenerator(width, height)
    # INTERFACE BLOCK
    pattern_image = generator.generate_pattern_image(pattern_name).load()
    final_image = Image.new("RGB", (width, height), "white")
    final_image_pix = final_image.load()
    im_1 = image_1.load()
    im_2 = image_2.load()
    for x in range(width):
        for y in range(height):
            final_image_pix[x, y] = merge_pixel(im_1[x, y], im_2[x, y], pattern_image[x, y])
    final_image.show()


def merge_pixel(image_1_tuple, image_2_tuple, pattern_tuple):
    # bierzemy tylko pod uwage czerwony bo zakladamy, ze pattern jest w skali szarosci
    pattern = float(pattern_tuple[0]) / 255
    return tuple([int(pattern * image_1_tuple[i] + (1 - pattern) * image_2_tuple[i]) for i in range(3)])


for pattern in pattern_dictionary:
    merge_images("palac.jpg", "palac2.jpg", pattern)
