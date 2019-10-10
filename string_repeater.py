def repeat(a_string, an_integer):
    empty_string = ''
    for idx in range(an_integer):
        empty_string += a_string
    return empty_string

result = repeat('Tochukwu', 3)
print(result)