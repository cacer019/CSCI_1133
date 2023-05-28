#CSCI 1133, Lab Section 002, HW 1 Elias Caceres, Problem 1A


import math
incidentAngle = float (input("Input incident angle in degrees: "))
incidentAngle = math.radians(incidentAngle)
n1 = float (input("Input index of refraction of first medium: "))
n2 = float (input("Input index of refraction of second medium: "))
angleOfRefraction = math.asin(math.sin(incidentAngle) * n1/n2)
print("Angle of Refraction: ", math.degrees(angleOfRefraction), 'degrees')
