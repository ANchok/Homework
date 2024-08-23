grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# создаем из множества студентов список студентов
students_list = list(students)
print(students_list, '- созданный неупорядоченный список')
# сортируем список студентов в алфавитном порядке
students_list = sorted(students_list)
print(students_list, '- отсортированный в алфавитном порядке список')
# создадим список средних баллов
average_grades = [sum(grades[0])/len(grades[0]),
                  sum(grades[1])/len(grades[1]),
                  sum(grades[2])/len(grades[2]),
                  sum(grades[3])/len(grades[3]),
                  sum(grades[4])/len(grades[4])]
print(average_grades, '- средний балл студентов по именам в алфавитном порядке')
# создаем словарь студентов с соответствующими средними баллами
# с использование цикла for
students_average_grades = {students_list[i]: average_grades[i] for i in range(len(students_list))}
print(students_average_grades)
# без использования цикла for
students_average_grades_ = {students_list[0]: average_grades[0],
                            students_list[1]: average_grades[1],
                            students_list[2]: average_grades[2],
                            students_list[3]: average_grades[3],
                            students_list[4]: average_grades[4]}
print(students_average_grades_)

