print('Задача 8. Пирамидка')


# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.


# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

   #
  ###
 #####
#######

pyramid_height = int(input("Введите высоту пирамиды: "))
pyramid_width = 1
pyramid_level = 1

for level in range(pyramid_height - 1):
    pyramid_width += 2

for level in range(1, pyramid_height + 1):
    free_space = (pyramid_width - pyramid_level) // 2
    print(" " * free_space + "#" * pyramid_level + " " * free_space)
    pyramid_level += 2
