def max(a, b):
    if a > b:
        return a
    return b

def main():
    int1 = int(input('Enter the first integer value: '))
    int2 = int(input('Enter the second integer value: '))
    result = max(int1, int2)
    print('The greater of the two integers is', result)

main()