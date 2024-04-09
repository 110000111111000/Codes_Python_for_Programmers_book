#country_codes = {'Finland': 'fi', 'South Africa': 'za', 'Nepal': 'np'}
#country_codes.clear()
#print(len(country_codes))
#if country_codes:
#    print('kklll')
#else:
#    print("lll")

#days_per_month = {'January':31, 'February':28, 'March':31}
#print(days_per_month)
#days_per_month['December'] = 12
#months_view = days_per_month.keys()
#for key in months_view:
#    print(key, end = '  ')
#for month_days in days_per_month.values():
#    print(month_days, end = '  ')
 

#roman_numerals = { 'I':1, 'II':2, 'III':3, 'V':5,'X': 100}

#roman_numerals ['V'] = 10
#roman_numerals ['L'] = 50

#del roman_numerals ['III']
#roman_numerals.pop('X')

#print(roman_numerals.get('V'))
#print('V' in roman_numerals)

#print( 'III' not in roman_numerals)


months = {'January':1 , 'February': 2, 'March':3}
#print(list(months.keys()))
#print(list(months.values()))
#print(list(months.items()))
#for month_name in sorted(months.keys()):
#    print(month_name, end = '  ')


#country_capitals1 = {'Beliguim': 'Brussels', 'Haiti': 'Port-au-Prince'}
#country_capital2 = {'Nepal':'Kathmandu', 'Uruguay': 'Montevideo'}
#conutry_capitals3 = {'Haiti': 'Port-au-Prince', 'Beliguim':'Brussels'}
#print(country_capitals1 == country_capital2 )
#print(country_capitals1 == conutry_capitals3)
#print(country_capitals1 != country_capital2)

# fig06_01.py
#""" Using a dictionary to represent an instructor's grade book."""

#grade_book = {'susan':[92,85,100], 'eduardo':[83,95,79], 'azizi':[91,89,82],'pantipa': [ 97,91,92]}

#all_grades_total = 0
#all_grades_count = 0

#for name, grades in grade_book.items():
#    total = sum(grades)
#    print(f'Average for {name} is {total/len(grades):.2f}')
#    all_grades_total += total
#    all_grades_count += len(grades)
    
#print(f"Class's average is: {all_grades_total / all_grades_count:.2f}")

#fig06_02.py
#"Tokenizing a string and counting unique words."""

#text = ('This is sample text with several words '
#        'this is more sample text with some diffrent words')

#word_counts = {} 

# count accurrences of each unique word

#for word in text.split():
#    if word in word_counts:
#        word_counts[word] += 1
#    else:
#        word_counts[word] = 1
#print(f'{"WORD":<12}COUNT')

#for word, count in sorted(word_counts.items()):
#    print(f'{word:<12}{count}')


#from collections import Counter

#text = ('this is sample text with several words '
#        'this is more sample text with some different words')

#counter = Counter(text.split())

#for word, count in sorted(counter.items()):
#    print(f'{word:<12}{count}')

#country_codes ={}
#country_codes.update({'South Africa' : 'za'})
#country_codes.update({'Australia':'ar'})
#country_codes.update({'Australia': 'au'})
#print(country_codes)

#months2 = {number:name for name, number in months.items()}
#print(months2)

#grades = {'Sue': [98,87,94], 'Bob':[84,95,91]}
#grades2 = {k:sum(v)/len(v) for k, v in grades.items()}
#print(grades2)

#colors = {'red','yellow','orange','green', 'blue', 'red'}
#print ('purple' not in colors)
#print(len(colors))
#for color in colors:
#    print(color.upper(), end = ' ')
#numbers = {1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10}
#numbers.add(17)
#numbers.remove(1)
#numbers.pop()
#numbers.clear()

#evens = [item for item in numbers if item % 2 == 0]
#print(evens)
#print({1, 3, 5 ,7}.symmetric_difference([1,2,2,3,3,4,4]))



# RollDieDynamic.py

""" Dynamically graphing frequencies of die rolls."""
from matplotlib import animation
import matplotlib.pyplot as plt
import random
import seaborn as sns
import sys

def update(frame_number, rolls, faces, frequencies):
    """"Configures bar plot contents for each animation frame"""

