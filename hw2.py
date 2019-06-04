
# Home work Lesson 2 Husainova Alina
# Easy

# 1 zadanie_easy
# cities = ['Nur-Sultan', 'Almaty', 'Qaragandy', 'Shymkent', 'Aqtobe', 'Atyrau', 'Semey', 'Taraz', 'Kokshetau', 'Aqtau']
# len_city = len(max(cities, key=len))
# for i, x in enumerate(cities, start=1):
#         print('{}. {}'.format(i, x.rjust(len_city)))

# 2 zadanie_easy
# x = [344, 567, 9, 56, 1022, 421]
# y = [457, 47875, 56, 421, 3000, 4, 9, 34, 123]
# a = list(set(y) - set(x))
# b = list(set(x) - set(y))
# print(a)
# print(b)

# 3 zadanie_easy
# a = [1, 3, 455, 400, 244, 9874, 344, 9]
# print(a)
# b = []
# for x in a:
#     if x % 2 == 0:
#         b.append(x / 4)
#     else:
#         b.append(x * 2)
#         print(b)

# Normal
# 1 zadanie


# a = [242, 367, 21, 674,  87655, -632]
# spisok = []
#
# for val in a:
#     if val >= 0:
#         sqr = val * 0.5
#
#         if sqr == int(sqr):
#             spisok.append(int(sqr))
# print(spisok)

2 zadanie

mon = ('', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')
days = ('', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'nineth', 'tenth',
       'eleventh', 'twelveth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteeth',
       'twentieth', 'twenty first', 'twenty second', 'twenty third', 'twenty fourth', 'twenty fifth', 'twenty sixth', 'twenty seventh', 'twenty eighth', 'twenty nineth', 'thirtieth', 'thirty first')
data = '19.12.2018'
day, month, year = data.split('.')
day = int(day)
month = int(month)
year = int(year)

print(days[day], mon[month], 'year', year)
