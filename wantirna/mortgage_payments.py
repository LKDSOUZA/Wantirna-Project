""" 
A program that calculates the monthly payments of a mortgage.
"""

def mortgage_payments(interest_rate, loan_amount, loan_period):
    """ Calculates the monthly payments of a mortgage. """
    # Calculate the monthly payment.
    monthly_payment = (loan_amount * (interest_rate / 1200)) / \
                      (1 - (1 + (interest_rate / 1200)) ** (-loan_period * 12))

    # Display the monthly payment.
    print("The monthly payment is $", format(monthly_payment, ",.2f"), sep="")

def main():
    """ The main function. """
    # Get the loan amount, interest rate, and loan period.
    loan_amount = float(input("Enter the loan amount: "))
    interest_rate = float(input("Enter the interest rate: "))
    loan_period = int(input("Enter the loan period (in years): "))

    # Call the mortgage_payments function.
    mortgage_payments(interest_rate, loan_amount, loan_period)

if __name__ == "__main__":

    # run the main function
    # to calculate the monthly payments of a mortgage
    main()
