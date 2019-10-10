def fat_cal(some_fat):
    cal_from_fat = some_fat * 9
    return cal_from_fat

def carb_cal(some_carb):
    cal_from_carb = some_carb * 4
    return cal_from_carb

def main():
    fat_gram = float(input('Enter the number of fat grams: '))
    carb_gram = float(input('Enter the number of carb grams: '))
    your_fat_cal = fat_cal(fat_gram)
    your_carb_cal = carb_cal(carb_gram)
    print('Your calories from fat is', your_fat_cal, 'and your calories from carb is', your_carb_cal)

main()