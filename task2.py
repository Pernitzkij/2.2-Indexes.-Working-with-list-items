nums_list = []
sum_i = 0
i = 1
Numers = int(input('Кол-во чисел в списке: '))
for _ in range(Numers):
    Numer = int(input(f'Введите {i} число: '))
    i += 1
    nums_list.append(Numer)

Numers_delete = int(input('Введите делитель: '))


for i_numers in range(len(nums_list)):
    if nums_list[i_numers] % Numers_delete == 0:
        print(f'Индекс числа {nums_list[i_numers]}: {nums_list[i_numers] // Numers_delete}')
        sum_i += (nums_list[i_numers] // Numers_delete)


print(f'Сумма индексов: {sum_i}')
