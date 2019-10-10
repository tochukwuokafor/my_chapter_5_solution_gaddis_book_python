def is_prime(number):
    counter = 0
    if number <= 1:
        return False
    for idx in range(1, number + 1):
        if number % idx == 0:
            counter += 1
            if counter > 2:
                return False
    return True

"""def main():
    my_number = int(input('Enter a number: '))
    result = is_prime(my_number)
    print('Is the number a prime number?', result)

main()"""
