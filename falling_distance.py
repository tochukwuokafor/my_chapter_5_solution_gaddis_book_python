g = 9.8

def falling_distance(time):
    distance = 0.5 * g * (time ** 2)
    return distance

def main():
    for idx in range(1, 11):
        value = falling_distance(idx)
        print(value)

main()