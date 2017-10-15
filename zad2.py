from PatternGenerator import PatternGenerator
from PIL import Image


def paste_pattern(image_string, pattern_name):
    image = Image.open(image_string)
    width, height = image.size
    generator = PatternGenerator(width, height)
    # INTERFACE BLOCK
    pattern_image = generator.generate_pattern_image(pattern_name).load()
    final_image = Image.new("RGB", (width, height), "white")
    final_image_pix = final_image.load()
    im_1 = image.load()
    for x in range(width):
        for y in range(height):
            final_image_pix[x, y] = merge_pixel(im_1[x, y], pattern_image[x, y])
    final_image.save(pattern_name + ".jpg")
    final_image.show()


def merge_pixel(image_tuple, pattern_tuple):
    return tuple([max(0, image_tuple[i] - pattern_tuple[i]) for i in range(3)])


paste_pattern("palac.jpg", "blurred_rings")

paste_pattern("palac.jpg", "grid")
