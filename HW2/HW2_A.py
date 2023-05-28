#CSCI 1133
#HW2 Problem A
#Elias Caceres cacer019

def poiseuille(length, radius, viscosity):
    import math
    flow = ((8 * viscosity * length))/((math.pi)*(radius**4))
    return flow

def main():
    length = float(input("Please enter the length: "))
    radius = float(input("Please enter the radius: "))
    viscosity = float(input("Please enter the viscosity: "))
    if (length <= 0) or (radius <= 0) or (viscosity <= 0):
        print("Failed due to input error. Please make sure your inputs are all positive. Exiting Program.")
    else:
        print("The resistance is: ", poiseuille(length, radius, viscosity))
    
if __name__ == "__main__":
    main()





