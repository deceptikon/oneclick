# # Урок 4
# ########

# Кортежи (tuples)
# кортежи - это по сути неизменяемые списки. Они имеют все те же свойства что и списки, кроме того,
# что элементы кортежа нельзя удалять/изменять/добавлять после того, как кортеж объявлен.
# польза кортежей в том, что это служит защитой от дурака (от случайного нежелательного изменения), а также
# в том что кортежи занимают меньше места в памяти
my_list = ['red', 'yellow', 'green']  # это привычный список
my_tuple = ('red', 'yellow', 'green')  # а это уже кортеж с тем же содержимым

# кортеж неизменяем, но можно поменять посредством конвертации в список и обратно
my_list = list(my_tuple)  # создаем список из кортежа
my_list.append('test')  # меняем список
my_list[1] = 'test2'
my_tuple = tuple(my_list)  # обратно создаем кортеж из списка и присваиваем его в переменную со старым кортежем
print( my_tuple)  # ('red', 'test2', 'green', 'test')

# создание кортежа с одним значением
# если попытаться создать кортеж с одним значением и не добавить запятую, то будет создана
# переменная с типом строка или число - то есть с тем типом, который мы пытались положить в кортеж
myvar = ('red') # если не поставим запятую, то переменная будет строкой
print(type(myvar)) # <class 'str'> 
tt = ('red',)  # a это корректное создание кортежа с одним значением
print(type(tt))  # <class 'tuple'>

# кортежи можно объединить через +
t1 = ('yin',)
t2 = ('yang',)
dual_tuple = t1 + t2
print(dual_tuple, type(dual_tuple))  # ('yin', 'yang') <class 'tuple'>


# Множества (sets)
# множества немного похожи на списки, но хранят в себе НЕ повторяющиеся элементы в случайном порядке.
# У множеств нет индексов, они неупорядочены и нельзя точно сказать, какой элемент будет первый
thisset = {"apple", "banana", "cherry", 'pineapple'}  # зададим множество
empty_set = set()  # а тут мы создали пустое множество с помощью ф-ии set
bad_set = {} # НА ЗАМЕТКУ - вот так вот пустое множество нельзя создать, то что мы получили тут - это пустой словарь.

# методы add/update []/remove/discard/pop/clear/union (returns new)
thisset.add('potato')  # добавим элемент во множество
thisset.update(['potato', 'carrot', 'pumpkin'])  # добавим сразу много элементов во множество, передав список
thisset.remove('carrot')  # удаляет значение из множества, выдаст ошибку, если не найдет такого значения
thisset.discard('carrot')  # тоже удаляет значение, но ошибку не выдаст, даже если не найдет че удалять
thisset.pop()  # удаляет первый элемент из мн-ва. Так как они неупорядочены, нельзя точно сказать, какой будет первый
print(thisset)  # я распечатывал это множ-во несколько раз
# {'pumpkin', 'apple', 'pineapple', 'potato', 'banana'}
# {'pineapple', 'potato', 'cherry', 'apple', 'pumpkin'}
# {'cherry', 'pumpkin', 'banana', 'apple', 'pineapple'}
# как видите, каждый раз расположение элементов разное и каждый раз методом pop() удалялся разный элемент
# это поведение наглядно демонстрирует, что такое неупорядоченность, когда мы говорим о множествах
newset = thisset.copy()  # так мы создаем копии множеств (как и у списков)
empty_set.clear()  # А этот метод очищает множество

# объединение множеств
set_1 = {'red', 'green'}
set_2 = {'black', 'red'}
set_1.update(set_2)  # изменяет первое множество, дополняя его вторым
set3 = set_1.union(set_2)  # создает третье множество из набора двух
print(set_1, set_2, set3)  # {'black', 'red', 'green'} {'black', 'red'} {'black', 'green', 'red'}

# Множества удобно использовать, если надо избавиться от повторяющихся элементов
repeating_list = ['one', 'two', 'three', 'two', 'one', 'one', 'one']  # возьмем список с дубликатами внутри
print(repeating_list)  # ['one', 'two', 'three', 'two', 'one', 'one', 'one']
myset = set(repeating_list)  # создадим множество из списка, тем самым избавясь от дублей
unique_list = list(myset)  # создадим новый список из множества, содержащий теперь только уникальные значения
print(unique_list)  # ['one', 'three', 'two']

# Немаловажно во множествах то, что с ними можно проводить операции как с математическими множествами - т.е.
# делать объединения (что мы уже делали выше), находить пересечения множеств, делать вычитания множеств, проверять,
# включает ли в себя одно множество другое, есть ли общие элементы у множеств и т.п.
# не будем подробно останавливаться на этом, лишь приведу здесь список подобных методов для общего понимания
# set.isdisjoint(other) - истина, если set и other не имеют общих элементов.
# set == other - все элементы set принадлежат other, все элементы other принадлежат set.
# set.issubset(other) или set <= other - все элементы set принадлежат other.
# set.issuperset(other) или set >= other - аналогично.
# set.union(other, ...) или set | other | ... - объединение нескольких множеств.
# set.intersection(other, ...) или set & other & ... - пересечение.
# set.difference(other, ...) или set - other - ... - множество из всех элементов set, не принадлежащие ни одному из other.
# set.symmetric_difference(other); set ^ other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
# set.update(other, ...); set |= other | ... - объединение.
# set.intersection_update(other, ...); set &= other & ... - пересечение.
# set.difference_update(other, ...); set -= other | ... - вычитание.
# set.symmetric_difference_update(other); set ^= other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.


# Словари (dictionaries)
# словари - самая развитая структура данных, предлагаемая в python.
# это изменяемые, индексируемые коллекции произвольного типа объектов с доступом по ключу, похожи на ассоциативные массивы в других языках
thisdict = {
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2010
}
empty_dict = dict()
print(thisdict)  # {'brand': 'Toyota', 'model': 'Corolla', 'year': 2010}
# к значениям можно обращаться по ключу, вместо индекса
print(thisdict['brand'])  # Toyota
print(thisdict['year'])  # 2010
# или через метод get(), обращение через него защищает от ошибки, если такого ключа нет
print(thisdict.get('model'))  # Corolla
print(thisdict.get('missing_key'))  # None
print(thisdict.get('missing_key', 'значение по умолчанию, если ключ не найден'))  # значение по умолчанию, если ключ не найден

# Добавим еще одно новое поле в словарь
thisdict['sell_year'] = 2010  # добавили в словарь поле с ключом sell_year и со значением 2010key exists
print(thisdict)  # {'brand': 'Toyota', 'model': 'Corolla', 'year': 2010, 'sell_year': 2010}

# in сравнивает наличие ключа
if 'year' in thisdict:
  print('Year is: ', thisdict['year'])

for a in thisdict:  # подобная конструкция итерирует (бежит по циклу) по ключам
  print('dict key: ', a, ' value: ', thisdict[a])  # в переменную a будет передаваться значение каждого ключа
# вот как это выведется
# dict key:  brand  value:  Toyota
# dict key:  model  value:  Corolla
# dict key:  year  value:  2010
# dict key:  sell_year  value:  2010


# Методы словарей
dict = {"test_key": "test_value"};
# dict.clear()  # очищает словарь.
# dict.copy()  # возвращает копию словаря, как и раньше с другими подобными типами.
# dict.get(key[, default])  # возвращает значение ключа, но если его нет, не бросает исключение (не дает ошибки),
# а возвращает default (по умолчанию None).
# например, тут, так как ключа another_test_key нет, вернет значение по умолчанию
print(dict.get('another_test_key', 'значение по умолчанию'))  # значение по умолчанию
# а тут ключ есть и вернется его значение
print(dict.get('test_key', 'значение по умолчанию'))  # test_value

dict.items()  # возвращает пары (ключ, значение).
for key, value in thisdict.items():
  print('ключ - ', key, 'значение - ', value)
# выведет
# ключ -  brand значение -  Toyota
# ключ -  model значение -  Corolla
# ключ -  year значение -  2010
# ключ -  sell_year значение -  2010

# dict.keys() - возвращает ключи в словаре.
print( thisdict.keys() )  # dict_keys(['brand', 'model', 'year', 'sell_year'])

# dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).
s = thisdict.pop('year')  # в переменную s запишется значение с ключом year и ключ со значением удалятся из списка
print("altered dict: ", thisdict, s)  # altered dict:  {'brand': 'Toyota', 'model': 'Corolla', 'sell_year': 2010} 2010

# dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError.
# Помните, что словари неупорядочены. А значит вы не можете точно знать, какой ключ-значение выберет этот метод
s = thisdict.popitem()  # в переменную s запишется кортеж с ключом и значением и ключ со значением удалятся из списка
print("altered dict 2: ", thisdict, s)  # altered dict 2:  {'brand': 'Toyota', 'model': 'Corolla'} ('sell_year', 2010)

# dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение,
# а создает ключ с значением default (по умолчанию None).
thisdict.setdefault(s[0], 'новое значение')  # возьмем ключ из предыдущего кортежа, возвращенного popitem
print(thisdict) # {'brand': 'Toyota', 'model': 'Corolla', 'sell_year': 'новое значение'}

# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other.
# Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
thisdict.update(dict)
print(thisdict) # {'brand': 'Toyota', 'model': 'Corolla', 'sell_year': 'новое значение', 'test_key': 'test_value'}

# dict.values() - возвращает значения в словаре.
# полезно если мы хотим поискать наличие значения в любом поле вообще
# удобно потом использовать в конструкциях for-in или if-in
print(thisdict.values())  # dict_values(['Toyota', 'Corolla', 2010, 2010])
if 'Toyota' in thisdict.values():
  print('The Toyota value exists in the dict')



# Функции - куски кода, которые исполняются только когда вызваны, а вызывать можно сколько угодно раз
# в функцию можно передавать аргументы и функция может вернуть результат
# переменные созданные внутри функции невидимы вне ее
def my_function():
  inner_variable = 'Внутренняя переменная'
  print("Hello from a function", inner_variable)

# Код выше не вызовется, пока мы не попросим его вызваться
my_function() # вот так вот

# print("----", inner_variable) - это выдаст ошибку, так как эта переменная только внутри ф-ии

x = 'outer variable'
def min_or_max(a, b): # так мы объявляем, что ф-я принимает аргументы a и b
  x = 'inner variable'  # здесь тоже пер-я x и она не перезаписывает пер-ю x выше
  if a > b:
    print('a > b')
  elif b > a:
    print('b > a')
  else:
    print('oni ravni')

a, b = 5, 10
# a и b это аргументы, передаваемые в функцию
min_or_max(a, b)  # распечатает b > a

# вызовем ф-ю с другими значениями
c, d = 45, 34
min_or_max(c, d)  # выведет a > b
min_or_max(5, 5)  # oni ravni


def summa(x = 10, y = 100):  # аргументам можно задавать значения по умолчанию
  sum = x + y
  return sum  # ключевое слово return указывает что возвращать из функции

# если мы вызовем ф-ю без аргументов, она все равно сработает, так как есть значения по умолчанию
our_sum = summa() # за счет ключевого слова return ф-я вернет сумму и она запишется в пер-ю
print(our_sum)  # 110
print(summa(100)) # 200
print(summa, 100, 99) # 199

# еще ф-я
def raznost(x, y):
  diff = x - y
  print("diff: ", diff)

raznost(y = 10, x = 5)  # можно указывать названия аргументов при вызове, тем самым делая неважным порядок аргументов
# diff: -5
raznost(10, 5)
# diff: 5

# можно указать аргумент со звездочкой и передавать хоть сколько аргументов далее в ф-ю -
# все что не поместилось, запишется в аргумент со звездочкой
def many_args(x, y, *args):
  print('x: ', x, 'y: ', y)
  print('many args:', args)
  for arg in args:
    print(arg)

many_args(1, 2, 3, 4, 5, 6, 7) # и тут мы можем еще хоть сколько аргументов передать, ф-я их примет.

# Рекурсия - это вызов функцией самой себя
def printer(stroka, x = 0):
  if x < 100:
    print(x, stroka)
    x += 1
    printer(stroka, x)  # тут мы вызываем саму же функцию изнутри, тем самым повторяя исполнение кода выше, пока x < 100

printer('Моя строка')  # вызов этой функции распечатает строку 100 раз

# создавая рекурсивную функцию, нужно помнить о том, чтобы не войти в бесконечный цикл, то есть обеспечить условие
# выхода из рекурсии



# Практические занятия

# создать пустой список, запросить у пользователя марку авто, модель и год,
# записать в словарь, записать этот словарь в наш список, повторить три раза,
# вывести список с содержащимися в нем данными
# использовать функции!



##### телебот - простой пример
# https://github.com/eternnoir/pyTelegramBotAPI
# botfather для получения токена
# pip install pyTelegramBotAPI


# import telebot
#
# bot = telebot.TeleBot("874489829:AAGKFBxs1QhsX1Hh-l6YKhxgVDk0Ke6bVmk")
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#   bot.reply_to(message, "Howdy, how are you doing?")
#
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#   # bot.reply_to(message, message.text)
#   # print(message)
#   reply = get_answer(message.text)
#   bot.send_message(message.chat.id, reply)
#
# def get_answer(ans):
#   if ans == 'привет':
#     return 'привет!!!'
#   elif ans == 'как дела':
#     return 'хорошо'
#   else:
#     return 'Не понял вас'
#
# bot.polling()
