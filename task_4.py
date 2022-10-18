print('Задача 4. Крест')

# Напишите программу,
# которая выводит на экран крест из символов “^”.
#
# (Символы выводятся по диагоналям воображаемого квадрата.)

# ^        ^
#  ^      ^
#   ^    ^
#    ^  ^
#     ^^
#     ^^
#    ^  ^
#   ^    ^
#  ^      ^
# ^        ^

size = int(input("Введите кол-во размер квадрата: "))

for row in range(size):
	for col in range(size):
		if col == row:
			print("^", end="")
		elif row + col + 1 == size:
			print("^", end="")
		else:
			print(" ", end="")

	print()
