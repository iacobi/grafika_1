from PatternGenerator import PatternGenerator

print ("Szerokosc Pierscienia:")
ring = input()
print ("Szerkosc Strefy rozmycia")
blur = input()

gen = PatternGenerator(800,500)
gen.set_ring_blur(ring,blur)
gen.generate_pattern_image("blurred_rings").show()