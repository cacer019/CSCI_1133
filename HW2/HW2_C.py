#CSCI 1133
#HW2 Problem C
#Elias Caceres cacer019

def calories_short(age, heart_rate, weight, time, height):
	calories_burned = int(((age * 0.074)+(heart_rate * 0.4472)-(weight * 0.05741)-20.4022) * time/4.184)
	return calories_burned 

def calories_tall(age, heart_rate, weight, time, height):
	calories_burned = int(((age * 0.2017)+(heart_rate * 0.6309)-(weight * 0.09036)-55.0969) * time/4.184)
	return calories_burned

h = float(input("Please input the height of the person(for example, 5.6 means 5 feet 6 inches): "))
w = float(input("Please input the body weight of person, in pounds: "))
hr = float(input("Please input the average heart rate of the person during the workout, in beats per minute: "))
a = float(input("Please input the age of the person, in years: "))
t = float(input("Please input the duration of the workout of the person, in minutes: "))

def main():
	if h > 5.6:
		print("You entered the following information: ")
		print("Height: ", h)
		print("Body Weight: ", int(w))
		print("Average heart rate: ", int(hr))
		print("Age: ", int(a))
		print("Duration of workout: ", int(t))
		print("The number of calories burned for this tall person is", calories_tall(a, hr, w, t, h), "calories.")
	elif h <= 5.6:
		print("You entered the following information: ")
		print("Height: ", h)
		print("Body Weight: ", int(w))
		print("Average heart rate: ", int(hr))
		print("Age: ", int(a))
		print("Duration of workout: ", int(t))
		print("The number of calories burned for this short person is", calories_short(a, hr, w, t, h), "calories.")

if __name__ == "__main__":
	main()









