#CSCI 1133
#HW2 Problem B
#Elias Caceres cacer019

import turtle
def fourSidedStar(lengthOfSide):
	length = lengthOfSide
	wn = turtle.Screen()
	tur = turtle.Turtle()
	tur.left(75)
	tur.forward(length)
	tur.right(60)
	tur.forward(length)
	tur.left(150)
	tur.forward(length)
	tur.right(60)
	tur.forward(length)
	tur.left(150)
	tur.forward(length)
	tur.right(60)
	tur.forward(length)
	tur.left(150)
	tur.forward(length)
	tur.right(60)
	tur.forward(length)
	turtle.mainloop()

def main():
	sides = float(input("Please enter side lengths: "))
	fourSidedStar(sides)
	
if __name__ == "__main__":
	main()







