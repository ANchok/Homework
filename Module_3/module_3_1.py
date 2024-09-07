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
    if string in list_to_search:
        return True
    else:
        return False


string_info('Произвольные слова где-то')
string_info('Kate Bakket')
is_contains('Kate', ['Kate', 'Richard', 'Skye'])
is_contains('Jonny', ['Kate', 'Richard', 'Skye'])
print(calls)