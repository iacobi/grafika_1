from PatternGenerator import PatternGenerator

print("Podaj szerokosc obrazu:")
width = input()

print("Podaj wysokosc obrazu:")
height = input()

print("Podaj rozmiar x")
x = input()

gen = PatternGenerator(width, height)
gen.set_x_y_step(x,x,x)
gen.generate_pattern_image("chessboard").show()
x = int(0.75*x)
gen.set_x_y_step(x,x,x)
gen.generate_pattern_image("chessboard_45").show()
