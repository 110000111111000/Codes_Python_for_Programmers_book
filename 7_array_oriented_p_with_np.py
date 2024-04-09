import numpy as np
integers = np.array([[1,2,3], [4,5,6]])
#print(integers.dtype)
#print(integers.ndim)
#print(integers.shape)

floats = np.array([0.0 , 0.1, 0.2, 0.3, 0.4])
#print(floats.dtype)
#print(floats.ndim)
#print(floats.shape)
#print(integers.size)
#print(integers.itemsize)
#print(floats.size)
#print(floats.itemsize)

#for rows in integers:
#    print('rows', rows)
#    for column in rows:
#        print('column:',column)

#for i in integers.flat:
#    print(i, end= ' ')

#print(np.zeros(5))
#print(np.ones((2,4), dtype = int))
#print(np.full((3,5),13))

#print(np.arange(5))
#print(np.arange(10,1,-2))
#print(np.arange(5, 10))

#print(np.linspace(0.0, 1.0,5)) 
#print(np.arange(1,21).reshape(4,5))
#print(np.arange(1, 100001).reshape(4,25000))
#print(np.arange(1,100001).reshape(100,1000))

import random
import numpy as np
import timeit
#print(timeit.timeit('output = 10**2'))

#print(timeit.timeit('output = [i for i in range(0, 6000000)]'))
#output = [random.randrange(1,7) for i in range(0, 60)]
#print('output',output)
#rolls_array = np.random.randint(1,7,6000000)
#print('rolls_array',rolls_array)
#numbers = np.arange(1,6)
#numbers2 = numbers.copy()
#numbers[1] *= 10
#numbers += 10
#numbers2 = np.linspace(1.1, 5.5, 5)
#print(numbers)
#numbers2[1] /= 10
#numbers2 = numbers[0:3]
#print(numbers2)
#print('numbers', (numbers ))
#print(numbers * numbers2)
#print(numbers >=13)
#print(numbers2 < numbers)
#print(numbers == numbers)
#grades = np.array([[87, 96, 70], [100, 87, 90]])
#print('square:', np.sqrt(numbers))
#print('grades:',grades)
#print('sum:',grades.sum())
#print('min:', grades.min())
#print('max:', grades.max())
#print('mean:',grades.mean(axis = 1))
#print('std:',grades.std())
#print('var:', grades.var())
#numbers2 = np.arange(1,7) * 10
#print('numbers2',numbers2)
#numbers = np.array([1 ,4 ,9 , 16, 25, 36])
#print(np.add(numbers, numbers2))
#print(np.multiply(numbers2, 5))
#numbers3 = numbers2.reshape(2, 3)
#print(numbers3)
#numbers4 = np.array([2,4,6])
#print('numbers4', numbers4)
#print(np.multiply(numbers3, numbers4))
#flattened = grades.flatten()
#print(flattened)
#grades2 = np.array([[94, 77, 90] , [100, 81, 82]])
#print('grades2', grades2)
#print(np.hstack((grades, grades2)))
#print(np.vstack((grades, grades2)))
import pandas as pd
#grades = pd.Series([87, 100, 94])
#print(grades)

#print(pd.Series(98.6 , range(3)))
#print(grades.count())
#print(grades.mean())
#print(grades.min())
#print(grades.max())
#print(grades.std())
#print(grades.describe())

#grades = pd.Series([87 ,100, 94], index = ['Wally', 'Eva', 'Sam'])
#print(grades)
#grdes = pd.Series({'Wally':87, 'Eva': 100, 'Sam': 94})
#print(grades.values)
#hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])
#print(hardware.str.contains('a'))
#print(hardware.str.upper())
#print(hardware)

grades_dict = {'Wally': [87,96, 70] , 'Eva': [100 ,87, 90] , 'Sam': [94,77 , 90], 'Katie': [100, 81, 82] , 'Bob': [83, 65, 85] } 
grades = pd.DataFrame(grades_dict)
grades.index = ['Test1', 'Test2', 'Test3']

print(grades)
#print(grades.pd.set_option('precision',2))
#print(grades.mean())
#print(grades.T.mean())
#print(grades.sort_values(by= 'Test1',axis=1 ,ascending= False))
print(grades.loc['Test1'].sort_values(ascending = False))

