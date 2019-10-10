COUNTY_TAX_RATE = 2.5
STATE_TAX_RATE = 5

def get_county_sales_tax(sales):
    county_tax = COUNTY_TAX_RATE / 100 * sales
    return county_tax

def get_state_sales_tax(sales):
    state_tax = STATE_TAX_RATE / 100 * sales
    return state_tax

def main():
    total_sales = float(input('Enter the total sales for the month: '))
    county_sales_tax = get_county_sales_tax(total_sales)
    state_sales_tax = get_state_sales_tax(total_sales)
    total = county_sales_tax + state_sales_tax
    print('The amount of county sales tax is $', county_sales_tax, sep = '')
    print('The amount of state sales tax is $', state_sales_tax, sep = '')
    print('The total sales tax (county plus state) is $', total, sep = '')

main()