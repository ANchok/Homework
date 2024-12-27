from multiprocessing import Pool
from time import time


def read_info(file_name: str):
    all_data = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            if line:
                all_data.append(line)
            else:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов

start_time = time()
for name in filenames:
    read_info(name)
end_time = time()
all_time = end_time - start_time
print(all_time)


# мультипроцессный вызов

if __name__ == '__main__':
    with Pool(4) as p:
        start_time = time()
        p.map(read_info, filenames)
        end_time = time()
        all_time = end_time - start_time
        print(all_time)

# 4.7563179 (линейный)
# 1.7461748 (многопроцессный)
