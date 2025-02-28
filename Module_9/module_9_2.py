first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(string) for string in first_strings if len(string) >= 5]
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]

third_string = first_strings + second_strings
third_result = {string: len(string) for string in third_string if not len(string) % 2}

print(first_result)
print(second_result)
print(third_result)