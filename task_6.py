print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N! 

num_seq_size = int(input("Введите количество чисел: "))
fact_sum = 0

for num in range(1, num_seq_size + 1):
	print(f"{num}! = ", end="")
	cur_fact = 1

	for x in range(1, num + 1):
		cur_fact *= x

	print(cur_fact)
	fact_sum += cur_fact

print(f"Сумма факториалов: {fact_sum}")
