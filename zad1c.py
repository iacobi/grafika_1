from PatternGenerator import PatternGenerator

print("Podaj szerokosc obrazu:")
width = input()

print("Podaj wysokosc obrazu:")
height = input()

print("Podaj rozmiar x")
x = input()

print("Podaj rozmiar y")
y = input()

gen = PatternGenerator(width, height)
gen.set_x_y_step(x,y,0)
gen.generate_pattern_image("chessboard").show()
gen.set_x_y_step(int(0.75*x),int(0.75*y),0)
gen.generate_pattern_image("chessboard_45").show()
