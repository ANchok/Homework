import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter

# numpy
# два одномерных массива
arr1 = np.array([1, 3, 2])
arr2 = np.array([2, 3, 1])

# обычные операции
print(f'arr2 - arr1: {arr2 - arr1}')
print(f'arr1 + arr2: {arr1 + arr2}')
print(f'arr1 * arr2: {arr1 * arr2}')
print(f'arr2 / arr1: {arr2 / arr1}')

# умножение массива на число
print(f'arr1 * 3: {arr1 * 3}')
# находим скалярное произведение массивов, матричное умножение
print(f'arr2 @ arr1: {arr2 @ arr1}')
arr4 = np.arange(1, 9).reshape(2, 4)
arr5 = np.arange(1, 9).reshape(4, 2)
print(f'arr4 @ arr5:\n{arr4 @ arr5}')
# транспонирование массива: создаем одномерный массив длиной 6, меняем его форму и получаем двумерный массив 2 на 3
# транспонирование переворачивает массив
arr3 = np.arange(6).reshape(2, 3)
print(f'arr3:\n{arr3}')
print(f'arr3.transpose():\n{arr3.transpose()}')

# matplotlib
# запишем координаты точек в массив
x_values = [0, 1, 2, 3]
y_values = [1, 0, 1, 0]
# запишем как точки (x, y)
x_arr = np.array(x_values)
y_arr = np.array(y_values)
xy_arr = np.concatenate((x_arr, y_arr), axis=0).reshape(2, 4).transpose()
print(f'(x,y):\n{xy_arr}')
# создаем график
fig, ax = plt.subplots()             # Создаем фигуру, содержащую одну ось.
fig.suptitle('Ломаная, соединяющая четыре точки')
ax.plot(x_values, y_values)    # Рисуем график по значениям x и y на оси.
plt.show()                           # Открываем окно с фигурой.

# pillow
# открываем изображение
image_1 = Image.open('tiger.png')
# формат, размер и цвветовая модель
print(image_1.format, image_1.size, image_1.mode)
# поменяем размер сохранив соотношение сторон
size = 512, 320
image_1.thumbnail(size)
print(image_1.size)
# применим фильтр СONTOUR
image_2 = image_1.filter(ImageFilter.CONTOUR)
# cохраняем изображение в формате jpeg
# для начала конвертируем RGBA в RGB
image_1 = image_1.convert('RGB')
image_2 = image_2.convert('RGB')
image_1.save('tiger_small.jpg', format='JPEG')
image_2.save('tiger_small_contour.jpg', format='JPEG')