RATE = 0.6

def tax(some_value):
    assessment_value = RATE * some_value
    property_tax = assessment_value * 0.72 / 100
    return assessment_value, property_tax

def main():
    actual_value = int(input('Enter the actual value of a piece of property: '))
    assess_value, prop_tax = tax(actual_value)
    print('The assessment value is ${:.2f} and the property tax is ${:.2f}'.format(assess_value, prop_tax), sep = '')

main()