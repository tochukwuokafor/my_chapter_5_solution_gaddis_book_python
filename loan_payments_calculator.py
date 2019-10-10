def monthly_payment(amount, rate, number_months):
    pay_per_month = (rate * amount) / (1 - ((1 + rate) ** (-number_months)))
    return pay_per_month

def main():
    loan_amount = float(input('Enter the loan amount: '))
    interest_rate = float(input('Enter monthly interest rate as a percentage: '))
    interest_rate /= 100
    months = int(input('Enter the desired number of months: '))
    month_payment = monthly_payment(loan_amount, interest_rate, months)
    print('The monthly amount payment necessary is ${:.2f}'.format(month_payment))

main()