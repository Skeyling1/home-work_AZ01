#Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv​
import pandas as pd

df = pd.read_csv('dz.csv')

avg_sl = df.groupby('City')['Salary'].mean()

print(avg_sl)
