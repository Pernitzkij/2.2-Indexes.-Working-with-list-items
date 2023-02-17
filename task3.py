from random import randint

numbers = []
numbers_rid = []

for i in range(10):
    numbers.append(randint(1, 20))
max_num = max(numbers)
min_num = min(numbers)
print(f'начало {numbers}')
one = max_num
two = min_num

for i_numer in numbers:
    if i_numer == one:
        numbers_rid.append(two)
    elif i_numer == two:
        numbers_rid.append(one)
    else:
        numbers_rid.append(i_numer)
print(f'конец {numbers_rid}')
