# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]

listnew = []

for i in list:
    n = i % 1
    if n > 0:
        listnew.append(n)
rez = round((max(listnew) - min(listnew)), 2)
print(f'Разница между max и min дробной части = {rez}')