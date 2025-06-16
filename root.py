U_i = int(input('Enter your value: '))
U_1 = float(input('Enter % of your value: '))
U_2 = int(input('Enter your num of years: '))

principal = U_i
rate = U_1
num_year = U_2
year = 1
while year <= num_year:
    principal = principal * (1 + rate)
    print('%3d %0.2f' % (year, principal))
    year += 1


import random

random_number = random.randint(1, 10)
user_number = input('Введите ваше число: ')

if user_number == random_number:
    print('Вы угадали!')
else:
    print('упс, вы не угадали')

new_try = input('Хотите попробовать еще раз?')

new_try2 = input('Введите новое число: ')
if new_try2 == user_number:
    f = print("Вы выйграли!")
else:
    print('Вы не угадали, игра окончена:(')
input('Начать новую игру?:' )
if input == 1:
    print('+ 1 коин')






    def greet():
        print('--hello Jhon!')
        print('--How do you do?')
        print('--fine')
greet()    



f = open("root.py")
line = f.readline()
while line:
    print(line)
    line = f.readline()
f.close()







for line in open('root.py'):
    print(line)





    import turtle
turtle.bgcolor('black')
t = turtle.Turtle()
colors = ['red', 'dark red']
for number in range(400):
    t.forward(number+1)
    t.right(89)
    t.pencolor(colors[number%2])





class person:
  def __init__(self, name, num):
    self.name = name
    self.num = num

kl = person("Dave", 55)
print('Now the file has more content!')





class MyClass:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
mynumber = MyClass()
myit = iter(mynumber)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))



tuple = ('jook', 'zook', 'pooklik')
for x in range(len(tuple)):
    print(x)

    set = dict(name='Joe', country='Norway', cash=66, level=5, difficulty='Hard')
    set['graphics'] = 'well'
    print(set.items())

    for x in set.keys():
        print(x)

full_name = {
    'name': 'Hugo',
    'surname': 'Padington'
}
car = {
    'car': 'BMW',
    'year': 2010
}


def printing():
    print(full_name['name'])
    print(car.values())


U_i = input('Enter: ')
if U_i == 'a':
    print(printing())

import sqlite3

data_base = sqlite3.connect('mark_data.db')

cursor = data_base.cursor()

#cursor.execute("""CREATE TABLE info(
   #age integer,
    #last_name text
#)""")

cursor.execute("INSERT INTO info VALUES ('Hi', 'Cartman', '567')")

cursor.execute("SELECT * FROM info")

print(cursor.fetchall())


data_base.close()








import sqlite3
db = sqlite3.connect("data.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user(
     name text,
     age integer,
     bio text
)
""")

cursor.execute("""INSERT INTO user(name, age, bio) VALUES (?, ?, ?)""", ('koo', 'tyh', 77))

db.commit()

cursor.execute("SELECT * FROM user")

print(cursor.fetchall())

cursor.close()
db.close()







print('Hello! Welcome to circle calculator. There you can find all circle parameters')

attemps = 100

for num in range(attemps):
    radius_value = int(input('Enter there radius value: '))
    user_choose = input('Enter what you would like to do (find circumference len-1, find diameter-2), find S-3: ')

    if user_choose == '1':
        print(2 * 3.14 * radius_value)
    elif user_choose == '2':
        print(radius_value * radius_value)
    elif user_choose == '3':
        print(3.14 * (radius_value * radius_value))


