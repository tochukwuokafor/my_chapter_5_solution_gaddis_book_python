"""def calc_average(test1, test2, test3, test4, test5):
    total = test1 + test2 + test3 + test4 + test5
    average = total / 5
    return average

def determine_grade(test1, test2, test3, test4, test5):
    my_test_list = [test1, test2, test3, test4, test5]
    print()
    print('Score\tLetterGrade')
    print('------------------')
    for score in my_test_list:
        if 90 <= score <= 100:
            print(score, '\t', 'A', sep = '')
        elif 80 <= score <= 89:
            print(score, '\t', 'B', sep = '')
        elif 70 <= score <= 79:
            print(score, '\t', 'C', sep = '')
        elif 60 <= score <= 69:
            print(score, '\t', 'D', sep = '')
        elif score < 60:
            print(score, '\t', 'F', sep = '')

def main():
    record = []
    for test in range(1, 6):
        print('Enter test #', test, ' score: ', sep = '', end = '')
        score = float(input())
        record.append(score)
    test1, test2, test3, test4, test5 = record
    test_average = calc_average(test1, test2, test3, test4, test5)
    determine_grade(test1, test2, test3, test4, test5)
    print()
    print('Average', '\t', test_average, sep = '')

main()"""

#The commented out code above is one solution. Here's another solution below

def calc_average(*tests):
    average = sum(tests) / len(tests)
    return average

def determine_grade(*tests):
    print()
    print('Score\tLetterGrade')
    print('------------------')
    for score in tests:
        if 90 <= score <= 100:
            print(score, '\t', 'A', sep = '')
        elif 80 <= score <= 89:
            print(score, '\t', 'B', sep = '')
        elif 70 <= score <= 79:
            print(score, '\t', 'C', sep = '')
        elif 60 <= score <= 69:
            print(score, '\t', 'D', sep = '')
        elif score < 60:
            print(score, '\t', 'F', sep = '')

def main():
    record = []
    for test in range(1, 6):
        print('Enter test #', test, ' score: ', sep = '', end = '')
        score = float(input())
        record.append(score)
    *tests ,= record
    test_average = calc_average(*tests)
    determine_grade(*tests)
    print()
    print('Average', '\t', test_average, sep = '')

main()