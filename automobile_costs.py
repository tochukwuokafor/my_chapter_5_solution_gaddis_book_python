def cost():
    years = int(input('Enter the number of years for which you will like to enter expenses: '))
    for year in range(1, years + 1):
        running_total = 0
        for month in range(1, 13):
            print()
            print('For year #', year, ', month #', month, ', enter the following expenses:', sep = '')
            loan_payment = float(input('Enter loan payment: '))
            insurance = float(input('Enter insurance: '))
            gas = float(input('Enter gas: '))
            oil = float(input('Enter oil: '))
            tires = float(input('Enter tires: '))
            maintenance = float(input('Enter maintenance: '))
            total = loan_payment + insurance + gas + oil + tires + maintenance
            running_total += total
            print('The total monthly expense is ${:.2f}'.format(total))
            print()
        print('The total annual cost for year #' + str(year) + ' is ${:.2f}'.format(running_total))

cost()