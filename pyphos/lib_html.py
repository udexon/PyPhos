def f_quotes():
    a=S.pop()
    p=a.index("='")
    q=a.index("';")
    S.append(a[p+2:q])


soup = BeautifulSoup(s[-1], 'html.parser') 

soup.string.replace_with('9999')

import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')


# ==== khilafahgold start; copy paste in Phos_chrome.py terminal
# (2) s=S ## define
# (3) f=SM

# (1) load khilafahgold.js into s[5]
# f('../KhilafahGold/wix0219.js fi:')
# s.append(s[5].split('\n'))
# s[6]
#
# s.append('../KhilafahGold/emas runcit - auto update.csv')
# f_csv()
# print("\n".join(s[7:]))


import csv
from bs4 import BeautifulSoup

def f_quotesf(): # full output: prefix suffix quoted_string 
    a=S.pop()
    print('in quotesf:', a)
    p=a.index("='")
    q=a.index("';")
    S.append(a[0:p+2])
    S.append(a[q:])
    S.append(a[p+2:q])


def f_csv():
    with open(S.pop()) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            print('in csv_reader', line_count, len(s))
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            elif line_count == 9:
                print(row)
                kg_date=row[6].split(',')[1]
                line_count += 1
            elif line_count == 12:
                print(f'\tKhilafah {row[7]} row8 {row[8]} row9 {row[9]}.')
                print(f'\t{s[6][9]}')
                s.append(kg_date+' Khilafah gold 999 RM'+row[7]+'/gram'); s.append(s[6][9]); f_rstr(); print(s[-1])
                print(f'\t{s[6][10]}')
                s.append('KHILAFAH GOLD CURRENT PRICE '+kg_date); s.append(s[6][10]); f_rstr(); print(s[-1])
                print(f'\t{s[6][11]}')
                s.append(row[7]); s.append(s[6][11]); f_rstr(); print(s[-1])
                print(f'\t{s[6][12]}')
                s.append(row[8]); s.append(s[6][12]); f_rstr(); print(s[-1])
                print(f'\t{s[6][15]}')
                s.append(row[9]); s.append(s[6][15]); f_rstr(); print(s[-1])
                line_count += 1
            elif line_count == 13:
                print(f'\t{s[6][13]}')
                s.append(row[7]); s.append(s[6][13]); f_rstr(); print(s[-1])
                print(f'\t{s[6][14]}')
                s.append(row[8]); s.append(s[6][14]); f_rstr(); print(s[-1])
                print(f'\t{s[6][16]}')
                s.append(row[9]); s.append(s[6][16]); f_rstr(); print(s[-1])
                line_count += 1
            else:
                print(f'\telse row7 {row[7]} row8 {row[8]} row9 {row[9]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')

def f_rstr(): # full output
    # s.append(s[6][15])
    print('in rstr:', s[-1])
    f_quotesf()
    soup = BeautifulSoup(s.pop(), 'html.parser') 
    soup.string.replace_with( s[-3] )
    f_swap()
    s.append( s.pop()+str(soup)+s.pop() )
    f_swap()
    s.pop()


s=S ## define
f=SM
f('1 2 3 4')
f('../KhilafahGold/wix0219.js fi:')
s.append(s[5].split('\n'))

s.append('../KhilafahGold/emas runcit - auto update.csv')
f_csv()
print("\n".join(s[7:]))

# ====

s.append('../KhilafahGold/emas runcit - auto update.csv')
f_csv()

s.append('~/Downloads/emas runcit - auto update(1).csv')
f_csv()

def f_rstrh (): # output html only
    # s.append(s[6][15])
    f_quotes()
    soup = BeautifulSoup(s.pop(), 'html.parser') 
    soup.string.replace_with( s.pop() )
    s.append( str(soup) )


s.append(s[6][15])
f_quotes()
s
h()
soup = BeautifulSoup(s[-1], 'html.parser') 

soup.string.replace_with('9999')
