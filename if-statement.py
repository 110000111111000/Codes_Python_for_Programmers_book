
#if grade >= 60:
#    print('Passed')
#else:
#    print('Faield')

###
#result = ('Passed'if grade >= 60 else 'Failed')
#print(result)
###

###
#print('You must take this course again')
#grade = 100
#if grade >= 60:
#    print('Passed')
#else:
#    print('Failed')
###

###
#product = 3
#while product <= 50:
#    product = product *3

#    print(product)
###

#for character in 'Programming':
#    print(character, end = ' ')
#    print (10,20,30, sep=', ')

#total = 0
#for number in [2, -3, 0, 17,9]:
#    total = total + number
#print(total) 

#for counter in range(10):
#    print(counter ,end = ' ')


#total = 0
#for number in [1,2,3,4,5]:
#    total += number
#print(total)

#class_average.py
# initialized phase
#total = 0
#grade_counter = 0
#grades = [98, 76,71,87,83, 90, 57, 79, 82, 94]
#for grade in grades:
#    total += grade
#    grade_counter += 1

#average = total /grade_counter
#print(f'Class average is {average}')

#class_average_senital.py

# initialization phase

#total = 0
#grade_counter = 0

#grade = int(input('Enter grade, -1 to end: '))
#while grade != -1:
#    total += grade
#    grade_counter += 1
#    grade = int(input('Enter grade, -1 to end: '))

    #termination phase
#if grade_counter != 0:
#    average = total/grade_counter
#    print(f'Class average is {average:.2f}')
#else:
### to here
#    print('No grades were entered')

#for number in range(10,0,-2):
#     print(number,end = ' ')
from decimal import Decimal


#amount = 112.31
#print(f'{amount:.20f}')

#principal = Decimal('1000.00')
#print (principal)
#rate = Decimal('0.05')

#x = Decimal('10.5')

#y = Decimal('2')
#x += y

#print(x += y) 


#for year in range(1,11):
#    amount = principal * (1 + rate ) ** year
#print(f'{year:>2}{amount:>10.2f}')

#for number in range(100):
#    if number == 2:
#        break
#    print(number)
    

#for number in range(10):
#    if number == 6:
#        continue
#    print(number)

#gender = 'Female'
#age = 70
#if gender == 'Female' and age >= 70:
#    print('Senior female')

#####
#semester_average = 83
#final_exam = 95

#if semester_average >= 90 or final_exam >= 90:
#    print('Student gets an A')

####
#grade = 87
#if grade != -1:
#    print ('The next grade is',grade)
####

####
grades = [85,93,45,89,85]
#print(sum(grades)/len(grades))
####

import statistics
a=statistics.mean(grades)
print(a)
b=statistics.median(grades)
print(b)
c=statistics.mode(grades)
print(c)
d=sorted(grades)
print(d)











