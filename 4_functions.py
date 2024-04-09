#def square(number):
#    """Calculate the square of number"""
#    return number ** 2
#print('The square of 7 is',square(7))
#print(square(4) + 1)

#def myfunction():
#    print("Hello World")
#myfunction() 


"""the first input number has one digit and the second number and third number have 2 digit the code gives wrong result"""
#def maximum(v1, v2, v3):
#    """Return the maximum of three values."""
#    max_value = v1
#    if v2 > max_value:
#        max_value = v2
#    if v3 > max_value:
#        max_value = v3
#    return max_value

#value1 = int(input("Enter first number:"))
#value2 = int(input("Enter second number:"))
#value3 = int(input("Enter third number:"))

#print("the max between ",value1," ",value2,"and ",value3,"is ",maximum(value1,value2,value3))

#import random

#for roll in range(10):
#    print(random.randrange(1,7))


#fig04_01.py

#"""Roll a six-sided die 6000000 times."""

#import random

# Face frequency counters
#frequency1 = 0
#frequency2 = 0
#frequency3 = 0
#frequency4 = 0
#frequency5 = 0
#frequency6 = 0

# 6,000,000 die rolls
#for roll in range(6000000):
#    face = random.randrange(1,7)

    # increment appropriate face counter
#    if face == 1:
#        frequency1 += 1
#    elif face == 2:
#        frequency2 += 1
#    elif face == 3:
#        frequency3 += 1
#    elif face == 4:
#        frequency4 += 1
#    elif face == 5:
#        frequency5 += 1
#    elif face == 6:
#        frequency6 += 1

#print(f'Face{"Frequency":>13}')
#print(f'{1:>4}{frequency1:>13}')
#print(f'{2:>4}{frequency2:>13}')
#print(f'{3:>4}{frequency3:>13}')
#print(f'{4:>4}{frequency4:>13}')
#print(f'{5:>4}{frequency5:>13}')
#print(f'{6:>4}{frequency6:>13}')

#random.seed(32)

#for roll in range(10):
#    print(random.randrange(1,7), end= ' ')

#for roll in range(10):
#    print(random.randrange(1,7), end= ' ')

#random.seed(32) 

#for roll in range(10):
#    print(random.randrange(1,7), end= ' ')




# fig04_02.py
#"""Simulating the dice game Craps."""
import random
#def roll_dice():
#    """Roll two dice and return their face values as a tuple."""
#    random.seed(3)
#    die11 = [] 
#    die1 = random.randrange(1, 7)
#    die11.append(random.randrange(1,7))
#    die2 = random.randrange(1, 7)
#    print(die11)
#    return (die1, die2) # pack die face value into a tuple
#print(roll_dice())

#def display_dice(dice):
#    random.seed(3)
#    """Display one roll of two dice."""
#    die1, die2 = dice # unpack the tuple into variables die1 and die2
#    print(f'Player rolled {die1} + {die2} = {sum(dice)}')
#die_values = roll_dice()#first roll
#display_dice(die_values)


# determine game status and point, based on first roll
#sum_of_dice = sum(die_values)

#if sum_of_dice in (7,11): #win
#    game_status = 'WON'
#elif sum_of_dice in (2,3,12): #lose
#    game_status = 'LOST'
#else: #remeber point
#    game_status = 'CONTINUE'
#    my_point = sum_of_dice
#    print('Point is', my_point)
# continue rolling until player wins or loses
#while game_status == 'CONTINUE':
#    die_value = roll_dice()
#    display_dice(die_values)
#    sum_of_dice = sum(die_values)

#    if sum_of_dice == my_point:
#        game_status = 'WON'
#    elif sum_of_dice == 7:
#        game_status = 'Lost'
# display "win" or "loses" messasge
#if game_status == 'WON':
#    print("Player wins")
#else:
#    print("Player loses")

import math
#l = math.sqrt(900)
#l = math.fabs(-10)
#print(l)

#def rectangle_area(length , width):
#    """ Return a rectangle's area."""
#    return length * width
#print(rectangle_area(10,5))



#def average(*args):
#    return sum(args)/ len(args)
#print(average(5,10))
#print(average(5,10,15,20))
#print(average(5,10,15,20,67))


#s = 'hello'
#print(s.lower())
#print(s.upper())

#x = 7
#def access_global():
#    x = 3.5
#    return print('x printed from acess_global:' , x)
#print(access_global())

#sum = 10 + 5
#print(sum)
#print(sum[10,5])


#from math import ceil, floor

#print(ceil(10.3))
#print(floor(10.7))

#from math import *
#e = 'hello'
#print(e)

#import statistics as stats
#grades = [85,93,45, 87,93]
#print(stats.mean(grades))


#x = 7
#print(id(x))

#def cube(number):
#    print('id(number):',id(number))
#    number **= 3
#    print('id(number):', id(number))
#    return number
#print(cube(x))
#print(f'x = {x}; id(x) = {id(x)}') 

#factorial = 1
#for number in range(5,0,-1):
#    factorial *= number  
#print(factorial)   

#def factorial(number):
#    """Return factorial of number"""
#    if number <= 1:
#        return 1
#    return number * factorial(number -1)

#for i in range(11):
#    print(f'{i}!', factorial(i))

#values = [1, 2, 3]
#print(sum(values))

#import statistics as st
#a = st.pstdev([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])
#print(a)

c = [-45, 6, 0, 72, 1543]

print(c)
