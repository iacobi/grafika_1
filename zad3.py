from PatternGenerator import PatternGenerator

gen = PatternGenerator(500, 500)

for pattern in gen.pattern_dictionary.keys():
    gen.generate_pattern_image(pattern).show()
