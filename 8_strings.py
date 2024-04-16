#print(f'{17.489:.2f}')

#print(f'{10:d}')
#print(f'{68:c} {97:c}')
#print(f'{"hello":s}{7}')

from decimal import Decimal
#print(f'{Decimal("10000000000000.0"):.3f}')
#print(f'{Decimal("10000000000000.0"):.2e}')
#print(f'[{27:10d}]')
#print(f'[{"hello":10}]')
#print(f'[{3.5:12f}]')
#print(f'[{27:<15d}]')
#print(f'[{"hello":>15}]')
#print(f'[{27:^7d}]')
#print(f'[{3.5:^8.1f}]')
#print(f'[{"hello":^7}]')
#print(f'[{27:+010d}]')
#print(f'{27:d}\n{27: d}\n{-27:d}')
#print(f'{12345678:,d}')
#print(f'{123456.78:,.2f}')
#print('{:.2f}'.format(17.489))
#print('{} {}'.format('Amanda','Cyan'))
#print('{0},{0},{1}'.format('Happy','Birthday'))
#print('{last} {first}'.format(first = 'Amanda', last ='Gray'))
#s1 = 'happy'
#s2 = 'birthday'
#s1 += s2
#print(s1)

#symbol = '>'
#symbol *= 7
#print(symbol)
#sentence = '\t \n This is a test string. \t\t \n'
#print(sentence.strip())
#print(sentence.lstrip())
#print(sentence.rstrip())

#print('happy birthday'.capitalize())
#print('strings : a deeper look'.title())
#print(f'A: {ord("A")}; a: {ord("a")}')
#print('Orange' >= 'orange')
sentence = 'to be or not to be that is the question'
#print(sentence.count('that',24, 25))
#print(sentence.rindex('be'))
#print('THAT' not in sentence)
#print(sentence.startswith('be'))
#letters = 'A, B, C, D'
#print(letters.split(', '))
#letters_list = ['A', 'B', 'C', 'D']
#print(','.join(letters_list))

#print('Amanda: 89, 97, 92'.partition(':'))

#url = 'http://www.deitel.com/books/PyCDS/table_of_contents.html'
#rest_of_url, seprator, document = url.rpartition('/')
#print(rest_of_url)
#print(seprator)
#print(document)

#lines = """This is line1\n
#This is line2
#This is line3"""
#print(lines)
#print(lines.splitlines(True))

#print('27'.isdigit())

#print('123 Main Street'.isalnum())

#file_path = r'C:\MyFolder\MySubFolder\MyFile.txt'
#print(file_path)

import re
pattern = '02215'
if re.fullmatch(pattern, '02215'):
#    print('Match')
else:
#    print('No match')

#print('Match' if re.fullmatch(pattern, '51220') else 'No match')
#print('Valid' if re.fullmatch(r'\d{5}', '02215') else 'Invalid')
#print('Valid' if re.fullmatch('[A-Z][a-z]*', 'Wally') else 'Invalid')
#print('Valid' if re.fullmatch('[A-Z][a-z]*', 'eva') else 'Invalid')
print('Valid' if re.fullmatch('[^a-z]','A') else 'Invalid')
print('Valid' if re.fullmatch('[^a-z]','a') else 'Invalid')
