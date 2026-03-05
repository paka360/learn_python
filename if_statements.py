#intro to If Statements
cars = ['audi', 'toyota', 'bmw', 'rolls_royce', 'bugatti']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

destination = 'Kumasi'
if destination != 'Accra':
    print('You are going the wrong way again.')

answer = 45
if answer != 50:
    print('Wrong answer. Please try again!')

age = 24
if age < 30:
    print ('\nYou are young')
if age > 30:
    print('You are grown')

#checking multiple conditions 
#Using 'and' to check multiple conditions
age_1 = 24
age_2 = 21
if age_1 > 30 and age_2 > 30:
    print('false')
if age_1 < 30 and age_2 < 30:
    print('true')
if (age_1 < 30) and (age_2 > 30):
    print('false')

#Using 'or' to check multiple conditions
if age_1 > 30 or age_2 > 30:
    print('false')
if age_1 < 30 or age_2 < 30:
    print('\nTrue')
if age_1 < 30 or age_2 > 30:
    print('True')

#checking for values in a list
destination = ['accra', 'kumasi', 'tamale', 'kasoa', 'ho']
location = 'accra'
if location in destination:
    print ('\nFinally we have arrived at '+ location.title())

location = 'amasaman'
if location not in destination:
    print('\nThis is '+location.title()+ ' we have not arrived yet.')


#Boolleon Expresssions 
game_active = True
Can_sing = False

#Practice Exercise
car = 'bugatti'
print("Is car == 'bugatti'? I predict true.")
print (car == 'bugatti')

print("\nIs car == 'toyota'? I vote False.")
print(car == 'toyota')

savings = 10 + 28 + 34 + 23
print ('Is my savings more than 100?')
print(savings >= 100)

print('Is my savings exactly 100?')
print(savings == 100)

print('Is my savings less than 100?')
print(savings <= 100)

phones = ['samsung', 'tecno', 'iphone', 'infinix', 'huawei']
print(phones)
print(phones[2] == 'samsung')

print(len(phones))
print(len(phones) == 5)

print(phones[4] == 'iphone' )

ages = [23, 18, 17, 22, 20, 18, 16, 17, 19]
print(ages)
for age in ages:
    if age >= 18:
        print(age)
        print('You are old enough to vote.\n')


#If-else staements
age = 16
if age >= 18:
    print('You are old enough to vote.')
    print('Have you registered to vote yet?')
else:
    print('Sorry, you are too young to vote.')
    print('Please register to vote as soon as you turn 18.')

numbers = [33, 43, 51, 22, 28, 29,10]
for number in numbers:
    if number >= 30:
        print(number)
        print('This numbear is large enough.\n')
    else:
        print(number)
        print('This number is too small.\n')

#If-elif-else chain
ages = [12, 19, 3]
for age in ages:
    if age < 4:
        print("Your child's admission cost is free.\n")
    elif age < 18:
        print("Your child's admission cost is $10.\n")
    else:
        print("Your child's admission cost is $20.\n")

#Alternative way of executing the code
ages = [12, 19, 3]
for age in ages:
    if age < 4:
        price = 'free'
    elif age < 18:
        price = '$10'
    else:
        price = '$20'
    print("Your child's admission fee is " + price +'.\n')

#Testing multiple conditions 
foods = ['tea', 'oat', 'porridge', 'coffee']
if 'tea' in foods:
    print('I would like a cup of tea.')
if 'coffee' in foods:
    print('I would like a cup of coffee.')
if 'porridge' in foods:
    print('I would like a cup of porridge.')
print('Here is your order.')

#Practise Exercise
alien_color = 'blue'

if alien_color == 'blue':
    print('\nYou just earned 5 points!')

if alien_color == 'green':
    print("You just earned 10 points!")

car_color = 'red'
if car_color == 'red':
    print("This is my father's car.")
else:
    print("This is not my father's car. It belongs to my mom.")

car_color = 'black'
if car_color == 'red':
    print("This is my father's car.")
else:
    print("This is not my father's car. It belongs to my mom.\n")

alien_color = 'blue'
if alien_color == 'blue':
    print("You have earned 3 points!\n")
elif alien_color == 'green':
    print("You have earned 5 points!\n")
elif alien_color == 'red':
    print('You have earned 10 points!\n')

alien_color = 'green'
if alien_color == 'blue':
    print("You have earned 3 points!\n")
elif alien_color == 'green':
    print("You have earned 5 points!\n")
elif alien_color == 'red':
    print('You have earned 10 points!\n')

alien_color = 'red'
if alien_color == 'blue':
    print("You have earned 3 points!\n")
elif alien_color == 'green':
    print("You have earned 5 points!\n")
elif alien_color == 'red':
    print('You have earned 10 points!\n')

age = 70
if age < 2:
    print ("You are a baby")
elif age < 4:
    print ("You are a toddler.")
elif age < 13:
    print ("You are a kid.")
elif age < 18:
    print ("You are a teenager")
elif age < 60:
    print ("You are an adult")
else:
    print ("You are an elder.\n")

favorite_fruits = ['pear', 'pawpaw', 'coconut', 'orange', 'banana', 'grape']
print (favorite_fruits)
favorite_fruit = 'banana'
if favorite_fruit in favorite_fruits:
    print ("I really like "+ favorite_fruit+"s.\n")
favorite_fruit = 'coconut'
if favorite_fruit in favorite_fruits:
    print ("I really like "+ favorite_fruit+"s.\n")
favorite_fruit = 'grape'
if favorite_fruit in favorite_fruits:
    print ("I really like "+ favorite_fruit+"s.\n")
    favorite_fruit = 'pear'
if favorite_fruit in favorite_fruits:
    print ("I really like "+ favorite_fruit+"s.\n")
    favorite_fruit = 'watermelon'
if favorite_fruit in favorite_fruits:
    print ("I really like "+ favorite_fruit+"s.\n")
if favorite_fruit in favorite_fruits:
    print ("I really like pawpaw")