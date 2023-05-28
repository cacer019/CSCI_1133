print("This program gives the temperature in fahrenheit with windchill in effect given the temperature in fahrenheit and velocity of the wind.")
t = float(input("Please enter the temperature in fahrenheit:"))
v = float(input("Please enter the wind velocity in miles per hour:"))
windchill = 35.74 + (0.6215*t) - (35.75*(v**0.16)) + (0.4275*t)*v**0.16

print("The temperature with windchill is:", windchill , "degrees fahrenheit.")

