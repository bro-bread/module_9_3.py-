import math

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


first_result = (int(math.sqrt((len(x) - len(y))**2)) for x in first for y in second if len(x) != len(y))

second_result = (
    max(len(first[i]), len(second[i]))
    for i in range(min(len(first), len(second)))
)

print(list(first_result))
print(list(second_result))

