from PIL import Image

#TODO: add more chars
ASCII = (' ', ',' , '.', '~', '!', '+', ':', 'v', 'c', 'I', 'o', 'w', '0', 'X', 'P', '$', '#', '*', 'R', 'B', '@')

def togray(c):
	r,g,b = c[0], c[1], c[2]
	gray = int((0.3 * r) + (0.59 * g) + (0.11 * b))
	return (gray, gray, gray)

im = Image.open('input.png')
pixels = im.load()
im.close()
WIDTH, HEIGHT = im.size[0], im.size[1]

div = 40
sq_size = int(WIDTH / div)

file = open("output.txt", 'w')

for y in range(0, HEIGHT, sq_size):
	for x in range(0, WIDTH, sq_size):
		R, G, B = 0, 0, 0
		for dx in range(sq_size):
			for dy in range(sq_size):
				if x + dx < WIDTH and y + dy < HEIGHT:
					pix = pixels[x + dx, y + dy]
					R += pix[0]
					G += pix[1]
					B += pix[2]
		sq2 = sq_size * sq_size
		R = int(R / sq2)
		G = int(G / sq2)
		B = int(B / sq2)
		gray = togray((R, G, B))
		g = gray[0]
		char = ASCII[int(g / len(ASCII))]
		file.write(char+char)
	file.write('\n')
file.close()
