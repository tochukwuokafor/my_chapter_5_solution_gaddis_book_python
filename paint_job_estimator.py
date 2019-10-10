BASE_FEET = 112
BASE_HOUR = 8
LABOR = 35

def number_of_gallon(square_feet):
    gallon_quant = square_feet / BASE_FEET
    return gallon_quant

def get_hour(square_feet):
    hour_of_labor = square_feet * BASE_HOUR / BASE_FEET
    return hour_of_labor

def get_paint_cost(square_feet, paint_per_gallon):
    cost_of_paint = square_feet / BASE_FEET * paint_per_gallon
    return cost_of_paint

def get_labor_charge(square_feet):
    labor_charge = square_feet * (BASE_HOUR / BASE_FEET) * LABOR
    return labor_charge

def main():
    square_feet = int(input('Enter the square feet of wall space to be painted: '))
    paint_per_gallon = float(input('Enter the price of paint per gallon: '))
    print('The number of gallons of paint required is $', number_of_gallon(square_feet), sep = '')
    print('The number of hours of labor required is $', get_hour(square_feet), sep = '')
    print('The cost of the paint is $', get_paint_cost(square_feet, paint_per_gallon), sep = '')
    print('The labor charges is $', get_labor_charge(square_feet), sep = '')
    print('The total cost of the paint job is $', get_labor_charge(square_feet) + get_paint_cost(square_feet, paint_per_gallon), sep = '')

main()