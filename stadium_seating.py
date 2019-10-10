def class_a(A_ticket):
    money_A = A_ticket * 20
    return money_A

def class_b(B_ticket):
    money_B = B_ticket * 15
    return money_B

def class_c(C_ticket):
    money_C = C_ticket * 10
    return money_C

def main():
    A_ticket = int(input('How many tickets of Class A seats were sold? '))
    B_ticket = int(input('How many tickets of Class B seats were sold? '))
    C_ticket = int(input('How many tickets of Class C seats were sold? '))
    income_A = class_a(A_ticket)
    income_B = class_b(B_ticket)
    income_C = class_c(C_ticket)
    total = income_A + income_B + income_C
    print('The amount of income generated from ticket sales is ${:.2f}'.format(total))

main()