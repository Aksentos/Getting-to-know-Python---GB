"""Задача №1. 
За день машина проезжает n километров. Сколько
дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя
пользоваться условной инструкцией if и циклами."""

auto_disstance = int(input("Какое расстояние проездает авто: "))
disstance = int(input("Какое общее расстоение нужно прохать?: "))
res = -(-disstance // auto_disstance)  # 1 вариант c унарным минусом
res = (disstance // auto_disstance) + bool(
    disstance % auto_disstance
)  # 2 вариант с булевым значением
print(res)
import math  # 3 вариант с помощью модуля math

res = disstance / auto_disstance
print(math.ceil(res))

# Варианты от преподавателя
per_day = int(input("Машина проезжает за день: "))
total = int(input("Сколько надо проехать: "))
print(math.ceil(total / per_day))
print(total // per_day + bool(total % per_day))
print(total // per_day + (total % per_day > 0))
print((total + per_day - 1) // per_day)
print(-(-total // per_day))

"""Задача №3. 
В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)"""

import math

class1 = int(input("Сколько учеников в 1 классе?: "))
class2 = int(input("Сколько учеников во 2 классе?: "))
class3 = int(input("Сколько учеников в 3 классе?: "))

sum = math.ceil(class1 / 2) + math.ceil(class2 / 2) + math.ceil(class3 / 2)  # вариант 1
sum = -(-class1 // 2) - (-class2 // 2) - (-class3 // 2)  # вариант 2
sum = (class1 + 1) // 2 + (class2 + 1) // 2 + (class3 + 1) // 2  # вариант 3
print("Всего парт нужно:", sum)

""" Задача №5. 
Вагоны в электричке пронумерованы натуральными
числами, начиная с 1 (при этом иногда вагоны
нумеруются от «головы» поезда, а иногда – с
«хвоста»; это зависит от того, в какую сторону едет
электричка). В каждом вагоне написан его номер.
Витя сел в i-й вагон от головы поезда и обнаружил,
что его вагон имеет номер j. Он хочет определить,
сколько всего вагонов в электричке. Напишите
программу, которая будет это делать или сообщать,
что без дополнительной информации это сделать
невозможно."""

num_go_in = int(input("Сколько вагонов прошёл Витя: "))
vagon = int(input("№ вагона в который сел Витя: "))

if num_go_in == vagon:
    print("без дополнительной информации это сделать невозможно")
else:
    print("Вагонов в поезде: ", num_go_in + vagon - 1)


"""Задача №7. 
Дано натуральное число. Требуется определить,
является ли год с данным номером високосным. Если
год является високосным, то выведите YES, иначе
выведите NO. Напомним, что в соответствии с
григорианским календарем, год является
високосным, если его номер кратен 4, но не кратен
100, а также если он кратен 400."""

# 1 вариант
year = int(input("Введите год: "))
if not year % 4 and year % 100 or not year % 400:
    print("Високосный")
else:
    print("No")

# 2 вариант
import calendar

year = int(input("Введите год: "))
if calendar.isleap(year):
    print("Год високосный.")
else:
    print("Год не високосный.")

# 3 вариант
year = int(input("Введите год: "))
print("YES" if not year % 400 or not year % 4 and year % 100 else "NO")
