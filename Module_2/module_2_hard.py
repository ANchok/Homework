n = int(input('Введите число от 3 до 20: '))
result = ''

# функция: находим максимальное первое число для пар (от 1 до n), для которого есть смысл искать пару: k + (k + 1) <= n,
# где k - искомое максимальное первое число для пар
def max_first_number(n):
    if n % 2 == 0:
        number = int(n / 2) - 1
        return number
    else:
        number = int((n - 1) / 2)
        return number


for i in range(1, max_first_number(n) + 1):
    for j in range(i + 1, n - i + 1):
        if n % (i + j) == 0:
            result += f'{i}{j}'
print(result)