import prime_numbers as pn

if __name__ == '__main__':
    for idx in range(1, 101):
        if pn.is_prime(idx):
            print(idx, end = ' ')
