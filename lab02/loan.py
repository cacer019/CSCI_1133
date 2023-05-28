print("This program computes the monthly payment needed to pay off a loan for an indicated loan duration given the loan amount, and annual interest rate.")
la = float(input("Please enter the loan amount:")) #la stands for loan ammount
air = float(input("Please enter the loan's annual interest rate:")) #air stands for Annual Interest Rate
ld = float(input("Please enter the duration of the loan in a number of months:"))
r = air/12
payment = (r*(la))/1-(1+r)**-ld
print("The monthly amount needed to pay for this loan in ",ld, "months is:", payment,"dollars.")
