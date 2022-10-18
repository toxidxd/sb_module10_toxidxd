print('Задача 9. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             11
#          31    51
#       71    91    11
#    13    15    17    19
# 21    23    25    27    29

pyramid_height = int(input("Введите высоту пирамиды: "))
pyramid_width = 1
pyramid_level = 1
number = 1

for level in range(pyramid_height - 1):
    pyramid_width += 2

for level in range(1, pyramid_height + 1):
    free_space = (pyramid_width - pyramid_level) // 2
    # print(" " * free_space + "#" * pyramid_level + " " * free_space)
    for _ in range(free_space):
        print("  ", end="")

    for _ in range(pyramid_level):
        if number % 2 != 0:
            if number < 10:
                print(number, end=" ")
            else:
                print(number, end="")
        else:
            print(" ", end=" ")
        number += 1

    for _ in range(free_space):
        print(" ", end="")

    number += 1
    pyramid_level += 2
    print()
