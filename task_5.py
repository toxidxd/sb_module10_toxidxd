print('Задача 5. Простые числа')


# Напишите программу,
# которая считает количество простых чисел в заданной последовательности
# и выводит ответ на экран.

num_seq_size = int(input("Введите количество чисел: "))
simple_count = 0

for numbers in range(num_seq_size):
	number = int(input("Введите число: "))
	simple = True

	if number == 1:
		simple = False
	else:
		for dev in range(2, number):
			if number % dev == 0:
				simple = False

	if simple:
		simple_count += 1

print(f"Количество простых чисел в последовательности: {simple_count}")
