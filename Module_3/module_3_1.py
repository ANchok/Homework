calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    tuple_ = (len(string), string.upper(), string.lower())
    count_calls()
    return tuple_


def is_contains(string, list_to_search):
    count_calls()
    list_lower = []
    for i in list_to_search:
        list_lower.append(i.lower())
    if string.lower() in list_lower:
        return True
    else:
        return False


print(string_info('Spider-man'))
print(string_info('KateBakket'))
print(is_contains('kate', ['Kate', 'Richard', 'Skye']))
print(is_contains('Jonny', ['Kate', 'Richard', 'Skye']))
print(calls)