#c = ['Mary', 'Smith', 3.5, 2022]

#c = [-45, 6, 0, 72, 1543]
#print(c[0],c[4])
#print(len(c))
#print(c[-1],c[-5])
#print(c)


#a = 1

#b = 2
#print(c[a +b])
#print(c)
#c[4] = 17
#print(c)

#s = 'hello'

#print(s[0])
#s[0] = 'H'
#print(c[100])

#print(c[0] + c[1] +c[2])


#a_list = []
#for number in range(1,6):
#    a_list += [number]
#print(a_list)  

#letters = []
#letters += 'Python'
#print(letters)


#list1 = [10, 20, 30]
#list2 = [40, 50]

#concatenated_list = list1 + list2

#print(concatenated_list)

#for i in range(len(concatenated_list)):
#    print(f'{i}:{concatenated_list[i]}')

#a = [1,2,3]
#b = [1,2,3]
#c= [1,2,3,4]

#print(a == b)
#print(a < c)
#print(c >= b)


#student_tuple = ()
#student_tuple = 'John', 'Green', 3.3
#print(student_tuple)
#print(len(student_tuple))

#another_student_tuple = ('Mary', 'Red', 3.3)
#print(another_student_tuple)

#a_singleton_tuple = ('red',)
#print(a_singleton_tuple)

#time_tuple = (9, 16, 1)
#print(time_tuple)
#print(time_tuple[1])
#print(time_tuple[0]*3600 + time_tuple[1]*60 + time_tuple[2])

#tuple1 = (10, 20, 30)
#tuple2 = tuple1
#print(tuple2)

#tuple1 += (40, 50)
#print(tuple1)

#number = [1, 2, 3, 4, 5]
#number += (6,7)
#print(number)

#student_tuple = ('Amanda', [98, 75, 87])
#first_name, grades = student_tuple

#print(first_name)
#print(grades)

#first, second = 'hi'
#print(f'{first}{second}')
#print(first)

#number1, number2, number3 = [2, 3, 5]
#print(number1, number2, number3)

#number1, number2, number3 = range(10, 40, 10)
#print(number1, number2, number3)


#student_tuples = ('Amanda',[98,85, 87])

#first_name, grades = student_tuples
#print(first_name)
#print(grades)

#number1 = 99
#number2 = 22
#number1, number2 = (number2 , number1)
#print(number1,number2)

#colors = ['red', 'orange', 'yellow']
#print(list(enumerate(colors)))
#print(tuple(enumerate(colors)))

#for index,value in enumerate(colors):
#    print(index,value)

# fig05_01.py
#"""Display a bar charts"""
#numbers = [19, 3, 15, 7, 11]
#for index, value in enumerate(numbers):
#    print(f'{index:>5}{value:>8} {"*" * value}')

#numbers = [2, 3, 5, 7, 11, 13, 17, 19]
#numbers[:]  = [] 
#print(numbers)

#numbers = list(range(0,10))
#del numbers
#print(numbers)

#def modify_elements(items):
#    """"Multiplies all element value in items by 2."""
#    for i in range(len(items)):
#        print(items[i] * 2)   

#numbers = [10, 3, 7, 1, 9]
#modify_elements(numbers)

#numbers_tuple = (10, 20, 30)
#modify_elements(numbers_tuple)


#numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
#numbers.sort()
#numbers.sort(reverse=True)
#ascending_numbers = sorted(numbers)
#print(ascending_numbers)
#print(numbers)

#letters = 'fadgchjebi'
#ascending_letters = sorted(letters)
#print(ascending_letters)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
#ascending_colors = sorted(colors)
#print (ascending_colors)
#print(numbers.index(5))
#i = numbers + numbers
#print(i)
#print(i.index(8,14))
#print(i.index(5, 7, len(i)))
#print(i.index(7,0,4))

#print(5 not in numbers)

#c = ['orange', 'yellow', 'green']
#c.insert(0, "red" )
#c.append('blue')
#c.extend(['indigo', 'violet'])
#c.remove('green')
#c.clear()
#print(c)

#sample_list = []
#s = 'abc'
#sample_list.extend(s)
#t = (1,2,3)
#sample_list.extend(t)
#sample_list.extend((4, 5, 6))
#print(sample_list)

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 2, 3, 3, 2, 2]

#for i in range(1, 6):
#    print(i, {responses.count(i)})

#colors.reverse() 
#print(colors)
#copied_list = colors.copy()
#print(copied_list)

#stack = []
#stack.append('red')
#print(stack)
#stack.append('green')
#print(stack)
#stack.pop()
#print(stack)
#stack.pop()
#print(stack)
#list1 = []
#for item in range(1,6):
#    list1.append(item)
#print(list1)


#list2 = [item for item in range(1,6)]
#list3 = [item ** 3 for item in range(1,6)]
#list4 = [item for item in range(1,11) if item % 2 == 0]
#print(list4)
#print(list2)
#print(list3)

#colors = [ 'red', 'orange', 'yellow', 'green', 'blue']
#colors2 = [item.upper() for item in colors ]
#print(colors2)

#for value in (x ** 2 for x in responses if x % 2 != 0):
#    print(value)

#square_of_odds =  (x ** 2 for x in responses if x % 2 != 0) 
#print(square_of_odds)

#numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
#def is_odd(x):
#     return x % 2 != 0
#print(list(filter(is_odd, numbers)))

#list6 = [item for item in responses if is_odd(item)]
#print(list6)
#list7 = list(filter(lambda x: x % 2 != 0, numbers))
#print(list7)

#numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
#print(list(map(lambda x: x **2, numbers)))

#print(list(map(lambda x: x**2,
#         filter(lambda x: x % 2 != 0,numbers))))

#print('Red' < 'orange')
#print(ord('R'))
#print(ord('o'))

#color = [ 'Red', 'orange', 'Yellow', 'green', 'Blue']
#print(max(color))

#print(max(colors, key = lambda s:s.lower()))

#reversed_number = [item **2 for item in reversed(numbers)]
#print(reversed_number)

#names = ['Bob', 'Sue', 'Amanda']
#grade_point_averages = [3.5, 4.0, 3.75]

#for name, gpa in zip(names, grade_point_averages):
#    print(name , gpa)

#a = [[77, 68, 86, 73], [96, 87, 89, 81],[70, 90, 86, 81]]
#for i,row in enumerate(a):
#    print(i,row)
#    for j, item in enumerate(row):
#        print(f'a[{i}][{j}] = {item}')

import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
import sys
rolls = [random.randrange(1,7) for i in range(int(sys.argv[1]))]
print('rolls',rolls,len(rolls))

values, frequencies = np.unique(rolls, return_counts = True)
print('values:', values, 'frequencies:', frequencies)  

print('p', frequencies/len(rolls) )
title = f'Rolling a six-sided Die {len(rolls):,} Times'
sns.set_style('whitegrid')
axes = sns.barplot(x=values, y=frequencies, palette = 'bright')
axes.set_title(title)
axes.set(xlabel='Die Value' ,ylabel = 'Frequency')
axes.set_ylim(top = max(frequencies) * 1.10)
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,},\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va = 'bottom')
plt.savefig('output6_plot.png')
plt.show()
#plt.cle()

