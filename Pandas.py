#При помощи библиотеки pandas импортируйте набор данных об автомобилях в формате CSV. Колонка 'name'
# должна быть использована в качестве индекса. Десятичный разделитель — точка, разделитель колонок — запятая.
# С помощью метода drop удалите лишние колонки. Должны остаться колонки 'hp', 'cyl', 'weight', 'accel' и индекс 'name'.
# Получите выборку из исходного набора данных на основании следующего критерия:Все строки, где cyl =4 (автомобили
# с четырехцилиндровым двигателем).
# Получите выборку из исходного набора данных на основании следующего критерия: Все строки, где  cyl =4 (автомобили
# с четырехцилиндровым двигателем) и hp > 80 (мощность строго больше 80) И все строки, где cyl = 8 (автомобили
# с восьмицилиндровым двигателем) и hp> 90 (мощность строго больше 90).
# Определите выборочное среднее столбца weight полученной в прошлом задании выборки. Результат округлите до тысячных.

import pandas as pd

all_cars = pd.read_csv('auto-mpg-quiz.csv',
                       index_col='name')

# print(all_cars)
# print()
# print(all_cars.columns)
# print()
all_cars = all_cars.drop(['mpg', 'displ','yr', 'origin'], axis=1)
#print(all_cars)
# print()
#print(all_cars.columns)
print()
#print(all_cars[all_cars.cyl == 4])
#print(all_cars[(all_cars.cyl == 4) & (all_cars.hp>80)])
cars_frame = all_cars[(all_cars.cyl == 4) & (all_cars.hp>80) | (all_cars.cyl == 8) & (all_cars.hp>90)]
print(cars_frame)

#print(round(cars_frame.weight.mean(), 3))