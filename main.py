from PIL import Image
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Graf_1:

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.primary_color = WHITE
		self.secondary_color = BLACK


	def painter(self, pattern_function):
		im = Image.new("RGB", (self.height, self.width), "white")
 		pix = im.load()
 		for i in range(0, self.height):
 			for j in range(0, self.width):
 				pix[i,j] = pattern_function(x=i,y=j)
 		im.show()


	def pattern(self, x,y, color_1=BLACK, color_2=WHITE):
		if x < 20 or y < 20:
			return self.primary_color
		else:
			return self.secondary_color


	def main(self):
		self.painter(self.pattern)
	

graf = Graf_1(300,600)
graf.main()