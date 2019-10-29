# # Урок 7
# ########
#
# # def my_func:
# #     pass
# #
# # class Creature:
# #     pass
#
# # class Creature:
# #     age = 0
# #     sex = 'Male'
# #
# # suschestvo = Creature() # создаст объект класса
# # bad_creature = Creature # НЕ ДЕЛАТЬ будет просто ссылаться на сам класс
# # print(type(suschestvo), type(bad_creature))
# #
# # print(suschestvo.sex)
# # suschestvo.test = 'test'
# # print(suschestvo.test)
# #
# # eshe_suschestvo = Creature()
# # eshe_suschestvo.sex = 'Female'
# # #
# # print('Существо: ', suschestvo.sex)
# # print('Еще существо: ', eshe_suschestvo.sex)
#
# M = 'Male'
# F = 'Female'
#
# class Creature:
#     age = 0
#     sex = 'Male'
#
#     def __init__(self, age, sex = 'Male'):
#         self.age = age
#         self.sex = sex
#
#     def show(self):
#         print('Это существо, ему', self.age, 'лет и его пол -', self.sex)
# #
#     # def __del__(self):
#     #     print('Сейчас существо будет удалено')
# #
# # s = Creature()
# # s = Creature(5, M)
# # s.show()
# # del(s)
# #
# # while True:
# #     pass
# #
# #
# class Man(Creature):
#     def __init__(self, age):
#         self.sex = M
#         self.age = age
# #
#     def show(self):
#         print('Это мужчина, ему', self.age, 'лет')
#
#
# class Woman(Creature):
#     __can_fly = False
# #
#     def __init__(self, age):
#         self.sex = F
#         self.name = 'Mary'
#         self.age = age
# #
#     def show(self):
#         print('Это женщина, ей', self.age, 'лет')
#         print('Защищенное свойство', self.__can_fly)
# #
#     def normal_method(self):
#         self.__protected_method()
#
#     def __protected_method(self):
#         print('Это защищенный метод, мы не можем его вызвать извне')
# #
# muzhik = Man(48)
# muzhik.show()
# #
# fem = Woman(12)
# fem.show()
# print(fem.age)
# fem.normal_method()
# # fem.__protected_method()
# fem.age = 100
# print(fem.age)
# print(fem.__can_fly)



# создать класс Worker c методом work и свойством salary, создать класс Driver,
# наследующийся от класса Worker, переопределить метод work(), добавить в Driver
# конструктор, который выставляет свойство salary по умолчанию отличное от родительского класса
# добавить деструктор в родительский класс
# создать объекты обеих классов, вызвать методы work

class Worker:
    salary = 5000
    def work(self):
        print('Зарплата: ', self.salary)
    def __del__(self):
        print('Это деструктор')

class Driver(Worker):
    # salary = 300
    def __init__(self):
        self.salary = 500
    def work(self):
        print('Зарплата водителя: ', self.salary)

obj_worker = Worker()
obj_driver = Driver()
obj_worker.work()
obj_driver.work()

obj_driver.salary = 15000
obj_driver.work()
