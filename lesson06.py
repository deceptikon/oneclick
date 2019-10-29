# Урок 6
########

# Работа с модулями

# import os, sys
# print(sys.path)
# sys.path.append('/home/lexx/levaya_papka_dlya_moduley')

# import our_module
# import wrongmodule
# os.oprst()
# our_module.sum(6, 666)

# l = dir(os)
# print(l)
# import builtins  # встроенные, всегда доступные ф-ии
# print(dir(builtins))

# import pyautogui as gui
# import our_module as om
# om.test_method()

# from os import listdir as spisok_faylov
# spisok = spisok_faylov('lesson05_data')
# print(spisok)
# ['users', 'test.txt', 'data.pickle', 'data.json']

# from our_module import *
# sum(3, 4)
# test_method()
# import our_module as om

# from our_module import *
# module_test()

# Пакеты модулей - Packages

# from our_package import submodule
# from our_package import *  # указанные в __all__
# submodule.sub_test()
# other_module.method_of_other_module()

# import our_package as p
# print(dir(p))
# p.subpackage.subsubmodule.subsubtest()
#
# from our_package.subpackage import subsubmodule as ss
# print(dir(ss))
# ss.subsubtest()


# пз - создать пакет mymath, добавить в него подпакет operations
# в operations должны быть модули arithmetic с ф-ями add/subtract, trigonometric c ф-ями sin/cos
# также добавить в пакет mymath модуль other c ф-ями min, max, round
# # Должен нормально отрабатывать следующий код:
# from mymath import other
# other.round()
# import mymath as m
# m.operations.arithmetic.add()
# import mymath.operations.trigonometric as trig
# trig.sin()
#







import os, sys

def show_file_list():
    dir_name = 'lesson05_data/test'
    d = os.listdir(dir_name)
    files_not_exist = True
    for i, file in enumerate(d):
        files_not_exist = False
        print(i, ':', file)
    if files_not_exist:
        print('Файлов пока нет')

# show_file_list()

dir_name = 'lesson05_data/users'
d = os.listdir(dir_name)
print(d)
print(enumerate(d))
for w, x in enumerate(d):
    print(w, '==>', x)












