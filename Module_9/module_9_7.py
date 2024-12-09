def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        if result > 1:
            is_pr = True
            for j in range(2, result):
                if result % j == 0:
                    is_pr = False
                    break
            if not is_pr:
                print('Составное')
            else:
                print('Простое')
        return result

    return wrapper


@is_prime
def sum_three(a: int, b: int, c: int):
    return a + b + c


x = sum_three(2, 3, 6)
print(x)