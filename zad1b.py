from PatternGenerator import PatternGenerator

print ("Podaj pierwszy kolor format: (r,g,b):")
color_tuple_1 = input()
print ("Podaj drugi kolor format: (r,g,b):")
color_tuple_2 = input()

print ("Podaj odleglosc x")
x = input()
print ("Podaj odleglosc y")
y = input()

print ("Podaj grubosc kraty")
step = input()

gen = PatternGenerator(800,500)
gen.set_colors(color_tuple_1, color_tuple_2)
gen.set_x_y_step(x,y,step)
gen.generate_pattern_image("grid").show()