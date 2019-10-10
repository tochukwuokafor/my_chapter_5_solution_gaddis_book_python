def insurance(replacement_cost):
    min_insurance = 0.8 * replacement_cost
    return min_insurance

def main():
    replacement_cost = float(input('Enter the replacement cost of a building: '))
    my_insurance = insurance(replacement_cost)
    print('The minimum amount of insurance you should buy for the property is', my_insurance)

main()