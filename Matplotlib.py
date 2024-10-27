#Постройте гистограмму распределения лошадиных сил (столбец hp) среди автомобилей.
# Используйте метод hist библиотеки matplotlib с параметрами по умолчанию.

import pandas as pd
import matplotlib.pyplot as plt

all_cars = pd.read_csv('auto-mpg-quiz (1).csv',
                       index_col='name')

#all_cars_sorted = all_cars.sort_values(by=['hp'])

#plt.plot( 'hp','accel', data=all_cars_sorted)
#plt.show()

#plt.hist('hp', data=all_cars)
#plt.show()

pie_data = all_cars.groupby(['cyl']).count()
print(pie_data)
plt.pie(pie_data['mpg'], labels=pie_data.index)
plt.show()