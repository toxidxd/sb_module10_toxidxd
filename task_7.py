print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

num_seq_size = int(input("Введите количество чисел: "))
max_summ = 0

for numbers in range(num_seq_size):
	number = int(input("Введите число: "))
	summ = 0
	while number > 0:
		x = number % 10
		summ += x
		number //= 10
	if summ > max_summ:
		max_summ = summ

print(f"{max_summ} - максимальная сумма цифр в числах")

