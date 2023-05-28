#Elias Caceres
#cacer019
#CSCI 1133 Homework 3 Problem A
#RGB to CMYK

import math

def RGB_to_CMYK(r, g, b):										
	rr = r/255
	gg = g/255
	bb = b/255
	rgb = [rr, gg, bb]
	if (max(rgb) <= 0):
		k = 100
		c = 0
		m = 0
		y = 0
		cmyk = [c, m, y, k]
		return cmyk
	else:
		k = round((1 - max(rgb))*100)
		kk = (1 - max(rgb))
		c = round(((1 - rr - kk)/(1 - kk))*100)
		m = round(((1 - gg - kk)/(1 - kk))*100)
		y = round(((1 - bb - kk)/(1 - kk))*100)
		cmyk = [c, m, y, k]
		return cmyk



def main():
	r = float(input("Please enter the Red value: "))
	g = float(input("Please enter the Green value: "))
	b = float(input("Please enter the Blue value: "))
	conversion = RGB_to_CMYK(r, g, b)
	print("Red component: ", int(r))
	print("Green component: ", int(g))
	print("Blue component: ", int(b))
	print("CMYK representation: ", conversion[0], conversion[1], conversion[2], conversion[3])





if __name__ == "__main__":
    main()

	







