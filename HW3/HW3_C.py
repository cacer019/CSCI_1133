#Elias Caceres
#cacer019
#CSCI 1133 Homework 3 Problem C
#Face Value & Monthly Payment on Installment Loans

def V_and_MP_on_IL(Principle, Interest_Rate, Term):
	interest = (Principle * (Interest_Rate/100) * Term)
	fv = (Principle + interest)
	number_of_months = (Term * 12)
	monthly_payments = (fv/number_of_months)
	money = [(fv), (monthly_payments), int(number_of_months)]
	return money
	
def main():

	print("Welcome to the installment loan evaluation program.")

	Principle = float(input("Please input the amount of money you will be borrowing: "))

	Interest_Rate = float(input("Please input the interest rate: "))

	Term = float(input("Please input the term for the loan (in years): "))

	if (Principle < 100):

		p_error = "Error: The loan amount is too low, the minimum amount is $100."

		print(p_error)

	if (Principle > 10000):

		p_error = "Error: The laon amount is too high, the maximum amount is $10000."

		print(p_error)

	if (Interest_Rate <= 0):

		i_error = "Error: The interest rate is either 0 or a negative number, the interest rate should be grater than zero and less than 15."

		print(i_error)

	if (Interest_Rate > 15):

		i_error = "Error: The interest rate is too high, the maximum interest rate value is 15."

		print(i_error)

	if (Term <= 0):

		t_error = "Error: The term amount entered is too short. The term should be greater than or equal to one year and less than or equal to 10 years."

		print(t_error)

	if (Term > 10):

		t_error = "Error: The term amount entered is too long. The term should be less than or equal to 10 years."

		print(t_error)

	if (Principle >= 100) and (Principle <= 10000) and (Interest_Rate > 0) and (Interest_Rate <= 15) and (Term > 0) and (Term <= 10):
		result = V_and_MP_on_IL(Principle, Interest_Rate, Term)

		sentence = 'The face value of the loan is: ${:.2f}'.format(result[0])
		sentance_2 = 'Your monthly payment each month for {} months is: ${:.2f}'.format(result[2], result[1])
		
		print(sentence)
		print(sentance_2)

if __name__ == "__main__":
    main()








