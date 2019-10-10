import random

def random_gen():
    even_counter = 0
    odd_counter = 0
    my_rand_list = [random.randint(1, 100) for rand_num in range(1, 101)]
    for number in my_rand_list:
        if number % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
    print('There are', even_counter, 'even numbers and', odd_counter, 'odd numbers')
    print('Just for fun, here is the random number list:', my_rand_list)

random_gen()