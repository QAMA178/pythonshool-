from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = "python-school-secret-key"

users = {}
ADMIN_PASSWORD = "20120212"

lessons = [
    {
        "number": 1,
        "title": "Переменные и данные",
        "description": "Учимся хранить информацию в переменных.",
        "theory": "Переменная хранит значение под определённым именем. Например, name = 'Alex'. В Python переменные создаются обычным присваиванием.",
        "code": """name = "Alex"
age = 14

print(name)
print(age)""",
        "task": "Создай переменные name, age и city. Запиши в них своё имя, возраст и город и выведи их.",
        "result": "В консоли должны появиться значения трёх переменных."
    },

    {
        "number": 2,
        "title": "Типы данных",
        "description": "Разбираемся со строками, числами и логическими значениями.",
        "theory": "Основные типы данных: str — строка, int — целое число, float — дробное число, bool — True или False. Узнать тип можно с помощью type().",
        "code": """name = "Python"
age = 14
price = 9.99
ready = True

print(type(name))
print(type(age))
print(type(price))
print(type(ready))""",
        "task": "Создай переменную каждого из четырёх типов и проверь их через type().",
        "result": "Python покажет четыре разных типа данных."
    },

    {
        "number": 3,
        "title": "Ввод данных",
        "description": "Получаем информацию от пользователя.",
        "theory": "input() позволяет получить текст от пользователя. Если нужно получить число, результат input() нужно преобразовать через int() или float().",
        "code": """name = input("Как тебя зовут? ")
age = int(input("Сколько тебе лет? "))

print("Привет,", name)
print("Тебе", age, "лет")""",
        "task": "Попроси пользователя ввести имя и любимое число и выведи оба значения.",
        "result": "Программа должна получить данные из консоли и вывести их."
    },

    {
        "number": 4,
        "title": "Числа и арифметика",
        "description": "Учимся выполнять математические операции.",
        "theory": "Python поддерживает +, -, *, /, //, %, **. Процент даёт остаток от деления, а ** используется для степени.",
        "code": """a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)""",
        "task": "Создай две переменные и вычисли их сумму, разность, произведение и остаток от деления.",
        "result": "В консоли появятся результаты операций."
    },

    {
        "number": 5,
        "title": "Условия if",
        "description": "Учимся принимать решения в программе.",
        "theory": "if выполняет код, если условие истинно. else выполняется в противоположном случае. elif позволяет проверить дополнительное условие.",
        "code": """age = 14

if age >= 18:
    print("Совершеннолетний")
else:
    print("Ещё нет 18")""",
        "task": "Напиши программу, которая определяет, положительное число, отрицательное или ноль.",
        "result": "Программа должна правильно определить знак числа."
    },

    {
        "number": 6,
        "title": "Цикл for",
        "description": "Повторяем действия несколько раз.",
        "theory": "Цикл for перебирает элементы последовательности. range() позволяет создавать последовательность чисел.",
        "code": """for number in range(1, 6):
    print(number)""",
        "task": "Выведи числа от 1 до 10 с помощью for.",
        "result": "В консоли должны появиться числа от 1 до 10."
    },

    {
        "number": 7,
        "title": "Списки",
        "description": "Храним несколько значений вместе.",
        "theory": "Список создаётся квадратными скобками. Элементы списка имеют индексы, начиная с 0.",
        "code": """games = ["Minecraft", "Roblox", "Terraria"]

print(games)
print(games[0])""",
        "task": "Создай список из пяти любимых игр и выведи первый и последний элементы.",
        "result": "Первый и последний элементы должны появиться в консоли."
    },

    {
        "number": 8,
        "title": "Цикл по списку",
        "description": "Перебираем элементы списка.",
        "theory": "for можно использовать для последовательного получения каждого элемента списка.",
        "code": """games = ["Minecraft", "Roblox", "Terraria"]

for game in games:
    print(game)""",
        "task": "Создай список из пяти предметов и выведи каждый отдельной строкой.",
        "result": "Каждый элемент списка появится в консоли."
    },

    {
        "number": 9,
        "title": "Функции",
        "description": "Создаём собственные команды.",
        "theory": "Функция создаётся с помощью def. Она позволяет объединить код и использовать его несколько раз.",
        "code": """def hello(name):
    print("Привет,", name)

hello("Alex")
hello("Sam")""",
        "task": "Создай функцию square(number), которая выводит квадрат числа.",
        "result": "Функция должна выводить квадрат переданного числа."
    },

    {
        "number": 10,
        "title": "Мини-проект: калькулятор",
        "description": "Объединяем ввод, условия и арифметику.",
        "theory": "Калькулятор использует несколько изученных конструкций: input(), float(), if и арифметические операторы.",
        "code": """a = float(input("Первое число: "))
b = float(input("Второе число: "))
op = input("Операция (+ - * /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("На ноль делить нельзя")
    else:
        print(a / b)
else:
    print("Неизвестная операция")""",
        "task": "Добавь в калькулятор ещё одну операцию — возведение в степень.",
        "result": "Калькулятор должен выполнять основные операции и возведение в степень."
    },

    {
        "number": 11,
        "title": "Цикл while",
        "description": "Повторяем код, пока условие истинно.",
        "theory": "while выполняет код до тех пор, пока его условие равно True.",
        "code": """number = 1

while number <= 5:
    print(number)
    number += 1""",
        "task": "Выведи числа от 1 до 10 с помощью while.",
        "result": "В консоли появятся числа от 1 до 10."
    },

    {
        "number": 12,
        "title": "break и continue",
        "description": "Управляем циклом.",
        "theory": "break полностью останавливает цикл. continue пропускает текущую итерацию.",
        "code": """for number in range(1, 11):
    if number == 6:
        break
    print(number)""",
        "task": "Выведи числа от 1 до 10, пропустив число 5.",
        "result": "Все числа кроме 5 должны быть выведены."
    },

    {
        "number": 13,
        "title": "Вложенные условия",
        "description": "Используем if внутри другого if.",
        "theory": "Одно условие можно разместить внутри другого. Это удобно для последовательной проверки нескольких требований.",
        "code": """age = 15
has_ticket = True

if age >= 14:
    if has_ticket:
        print("Можно пройти")
    else:
        print("Нужен билет")
else:
    print("Возраст недостаточный")""",
        "task": "Сделай проверку возраста и наличия билета.",
        "result": "Программа должна проверить оба условия."
    },

    {
        "number": 14,
        "title": "Вложенные циклы",
        "description": "Используем цикл внутри цикла.",
        "theory": "Вложенные циклы полезны при работе с таблицами, сетками и двумерными данными.",
        "code": """for row in range(3):
    for column in range(3):
        print(row, column)""",
        "task": "Выведи координаты квадратной сетки 4 на 4.",
        "result": "Будут выведены пары координат."
    },

    {
        "number": 15,
        "title": "Логические операторы",
        "description": "Соединяем несколько условий.",
        "theory": "and требует выполнения двух условий. or требует хотя бы одного. not меняет логическое значение на противоположное.",
        "code": """age = 16
has_ticket = True

if age >= 14 and has_ticket:
    print("Доступ разрешён")""",
        "task": "Разреши доступ, если пользователь старше 14 лет или имеет специальный пропуск.",
        "result": "Программа должна правильно проверить условия."
    },

    {
        "number": 16,
        "title": "Сравнение строк",
        "description": "Сравниваем текст.",
        "theory": "Строки можно сравнивать с помощью == и !=.",
        "code": """answer = input("Напиши yes: ")

if answer == "yes":
    print("Правильно")
else:
    print("Попробуй ещё")""",
        "task": "Сделай проверку любимого цвета пользователя.",
        "result": "Программа должна сравнить введённую строку."
    },

    {
        "number": 17,
        "title": "Методы строк",
        "description": "Работаем с текстом.",
        "theory": "У строк есть методы upper(), lower(), strip(), replace() и многие другие.",
        "code": """text = "  Python School  "

print(text.strip())
print(text.upper())
print(text.lower())
print(text.replace("School", "Course"))""",
        "task": "Получи строку пользователя, убери пробелы и выведи её в верхнем регистре.",
        "result": "Текст должен быть очищен и преобразован."
    },

    {
        "number": 18,
        "title": "f-строки",
        "description": "Удобно вставляем переменные в текст.",
        "theory": "f-строки позволяют вставлять значения прямо внутрь строки.",
        "code": """name = "Alex"
age = 14

print(f"Меня зовут {name}, мне {age} лет.")""",
        "task": "Создай f-строку с именем, возрастом и любимым языком программирования.",
        "result": "Все значения должны появиться в одной строке."
    },

    {
        "number": 19,
        "title": "Индексы и срезы строк",
        "description": "Получаем части строки.",
        "theory": "Индексы начинаются с нуля. Срез text[start:end] позволяет получить часть строки.",
        "code": """word = "Python"

print(word[0])
print(word[-1])
print(word[0:3])""",
        "task": "Выведи первый символ, последний символ и первые три символа слова.",
        "result": "Программа должна правильно использовать индексы."
    },

    {
        "number": 20,
        "title": "split и join",
        "description": "Разделяем и соединяем строки.",
        "theory": "split() превращает строку в список. join() соединяет элементы списка обратно в строку.",
        "code": """text = "Python Java C++"

words = text.split()
print(words)

result = "-".join(words)
print(result)""",
        "task": "Получи предложение и собери его обратно через дефис.",
        "result": "Слова должны быть соединены через '-'."
    },

    {
        "number": 21,
        "title": "Методы списков",
        "description": "Добавляем и удаляем элементы.",
        "theory": "append() добавляет элемент, remove() удаляет, pop() удаляет по индексу, sort() сортирует список.",
        "code": """numbers = [3, 1, 4]

numbers.append(2)
numbers.sort()

print(numbers)""",
        "task": "Создай список чисел, добавь новое число и отсортируй его.",
        "result": "Список должен быть отсортирован."
    },

    {
        "number": 22,
        "title": "Срезы списков",
        "description": "Получаем часть списка.",
        "theory": "Срезы списков работают по принципу start:end:step.",
        "code": """numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])
print(numbers[::2])""",
        "task": "Выведи первые три элемента и элементы через один.",
        "result": "Должны появиться два разных среза."
    },

    {
        "number": 23,
        "title": "Кортежи",
        "description": "Изучаем неизменяемые последовательности.",
        "theory": "Кортеж похож на список, но после создания его элементы нельзя изменить.",
        "code": """point = (10, 20)

print(point[0])
print(point[1])""",
        "task": "Создай кортеж с координатами точки.",
        "result": "Обе координаты должны быть выведены."
    },

    {
        "number": 24,
        "title": "Множества",
        "description": "Храним только уникальные значения.",
        "theory": "set автоматически удаляет повторяющиеся элементы.",
        "code": """numbers = {1, 2, 2, 3, 3, 3}

print(numbers)""",
        "task": "Создай список с повторяющимися числами и преврати его в множество.",
        "result": "Повторы должны исчезнуть."
    },

    {
        "number": 25,
        "title": "Операции с множествами",
        "description": "Объединяем и сравниваем множества.",
        "theory": "Можно использовать объединение |, пересечение & и разность -.",
        "code": """a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a & b)
print(a - b)""",
        "task": "Создай два множества игр и найди игры, которые есть в обоих.",
        "result": "Программа должна показать пересечение."
    },

    {
        "number": 26,
        "title": "Словари",
        "description": "Храним данные по ключам.",
        "theory": "Словарь хранит пары ключ: значение.",
        "code": """user = {
    "name": "Alex",
    "age": 14
}

print(user["name"])""",
        "task": "Создай словарь ученика с именем, возрастом и классом.",
        "result": "Все данные должны находиться в одном словаре."
    },

    {
        "number": 27,
        "title": "Методы словаря",
        "description": "Работаем с ключами и значениями.",
        "theory": "Полезные методы: get(), keys(), values(), items(), update() и pop().",
        "code": """user = {
    "name": "Alex",
    "age": 14
}

user["city"] = "Tashkent"

print(user.keys())
print(user.values())""",
        "task": "Добавь в словарь город и выведи все ключи.",
        "result": "Новый ключ должен появиться в словаре."
    },

    {
        "number": 28,
        "title": "Вложенные словари",
        "description": "Создаём сложные структуры.",
        "theory": "Значением словаря может быть другой словарь.",
        "code": """students = {
    "alex": {
        "age": 14,
        "grade": 8
    },
    "sam": {
        "age": 15,
        "grade": 9
    }
}

print(students["alex"]["grade"])""",
        "task": "Создай словарь с двумя учениками и их данными.",
        "result": "Ты должен научиться обращаться к вложенным значениям."
    },

    {
        "number": 29,
        "title": "return и несколько значений",
        "description": "Возвращаем результаты из функции.",
        "theory": "return передаёт значение из функции наружу. Python позволяет вернуть несколько значений.",
        "code": """def calculate(a, b):
    return a + b, a * b

sum_value, product = calculate(3, 4)

print(sum_value)
print(product)""",
        "task": "Создай функцию, которая возвращает минимум и максимум из двух чисел.",
        "result": "Результаты должны быть получены через return."
    },

    {
        "number": 30,
        "title": "Аргументы по умолчанию",
        "description": "Задаём стандартные значения параметров.",
        "theory": "Параметр функции может иметь значение по умолчанию.",
        "code": """def hello(name="друг"):
    print(f"Привет, {name}!")

hello()
hello("Alex")""",
        "task": "Создай функцию greet() со стандартным именем 'Гость'.",
        "result": "Функция должна работать и с аргументом, и без него."
    },

    {
        "number": 31,
        "title": "Именованные аргументы",
        "description": "Передаём аргументы по имени.",
        "theory": "Именованные аргументы позволяют явно указать параметр.",
        "code": """def profile(name, age):
    print(name, age)

profile(age=14, name="Alex")""",
        "task": "Создай функцию с тремя параметрами и вызови её именованными аргументами.",
        "result": "Порядок аргументов при вызове не должен иметь значения."
    },

    {
        "number": 32,
        "title": "Область видимости",
        "description": "Разбираемся с локальными переменными.",
        "theory": "Переменная внутри функции обычно локальная. Переменная вне функции может быть доступна из неё.",
        "code": """name = "Python"

def show():
    message = "Привет"
    print(name)
    print(message)

show()""",
        "task": "Создай глобальную и локальную переменную и выведи их внутри функции.",
        "result": "Ты увидишь разницу областей видимости."
    },

    {
        "number": 33,
        "title": "lambda",
        "description": "Создаём короткие функции.",
        "theory": "lambda используется для простых функций из одного выражения.",
        "code": """square = lambda x: x * x

print(square(5))""",
        "task": "Создай lambda-функцию, которая удваивает число.",
        "result": "Функция должна вернуть удвоенное значение."
    },

    {
        "number": 34,
        "title": "sorted и key",
        "description": "Сортируем данные по выбранному параметру.",
        "theory": "sorted() возвращает отсортированную последовательность. key позволяет указать критерий сортировки.",
        "code": """names = ["Bob", "Alexander", "Tom"]

result = sorted(names, key=len)

print(result)""",
        "task": "Отсортируй список слов по длине.",
        "result": "Самые короткие слова должны оказаться в начале."
    },

    {
        "number": 35,
        "title": "enumerate",
        "description": "Получаем индекс и значение.",
        "theory": "enumerate() позволяет одновременно получать номер и значение элемента.",
        "code": """games = ["Minecraft", "Roblox", "Terraria"]

for index, game in enumerate(games, start=1):
    print(index, game)""",
        "task": "Выведи список предметов с номерами начиная с 1.",
        "result": "Каждый элемент должен иметь свой номер."
    },

    {
        "number": 36,
        "title": "zip",
        "description": "Соединяем несколько списков.",
        "theory": "zip() позволяет одновременно проходить по нескольким последовательностям.",
        "code": """names = ["Alex", "Sam"]
ages = [14, 15]

for name, age in zip(names, ages):
    print(name, age)""",
        "task": "Соедини список имён со списком городов.",
        "result": "Для каждого имени должен быть показан город."
    },

    {
        "number": 37,
        "title": "List comprehension",
        "description": "Создаём списки компактно.",
        "theory": "List comprehension позволяет создавать список на основе цикла.",
        "code": """squares = [x * x for x in range(1, 6)]

print(squares)""",
        "task": "Создай список кубов чисел от 1 до 10.",
        "result": "Получится список из десяти кубов."
    },

    {
        "number": 38,
        "title": "Dict comprehension",
        "description": "Создаём словари компактно.",
        "theory": "Dict comprehension создаёт словарь на основе выражения.",
        "code": """squares = {
    x: x * x
    for x in range(1, 6)
}

print(squares)""",
        "task": "Создай словарь чисел от 1 до 5, где значение — куб числа.",
        "result": "Получится словарь с пятью парами."
    },

    {
        "number": 39,
        "title": "Генераторы",
        "description": "Используем yield.",
        "theory": "Генераторы выдают значения по одному с помощью yield.",
        "code": """def numbers(limit):
    for number in range(limit):
        yield number

for number in numbers(5):
    print(number)""",
        "task": "Создай генератор чётных чисел.",
        "result": "Чётные числа должны выдаваться по одному."
    },

    {
        "number": 40,
        "title": "try и except",
        "description": "Обрабатываем ошибки.",
        "theory": "try содержит код, который может вызвать ошибку, а except позволяет её обработать.",
        "code": """try:
    number = int(input("Число: "))
    print(10 / number)
except ValueError:
    print("Нужно ввести число")
except ZeroDivisionError:
    print("На ноль делить нельзя")""",
        "task": "Сделай безопасный ввод двух чисел.",
        "result": "Программа не должна падать при неправильном вводе."
    },

    {
        "number": 41,
        "title": "else и finally",
        "description": "Дополняем обработку ошибок.",
        "theory": "else выполняется, если ошибки не было. finally выполняется всегда.",
        "code": """try:
    number = int(input("Число: "))
except ValueError:
    print("Ошибка")
else:
    print("Ты ввёл", number)
finally:
    print("Проверка закончена")""",
        "task": "Добавь else и finally в программу с вводом.",
        "result": "finally должен выполняться всегда."
    },

    {
        "number": 42,
        "title": "raise",
        "description": "Создаём исключения самостоятельно.",
        "theory": "raise позволяет вручную вызвать исключение при неправильных данных.",
        "code": """age = -5

if age < 0:
    raise ValueError("Возраст не может быть отрицательным")""",
        "task": "Создай проверку, которая запрещает отрицательные числа.",
        "result": "При отрицательном числе должна возникать понятная ошибка."
    },

    {
        "number": 43,
        "title": "Запись в файл",
        "description": "Сохраняем данные на компьютере.",
        "theory": "open() с режимом w позволяет записывать данные в файл. with автоматически закрывает файл.",
        "code": """with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Моя первая заметка")""",
        "task": "Создай файл notes.txt и запиши в него три строки.",
        "result": "В папке проекта должен появиться файл notes.txt."
    },

    {
        "number": 44,
        "title": "Чтение файла",
        "description": "Получаем данные из файла.",
        "theory": "Режим r используется для чтения файла. read() получает его содержимое.",
        "code": """with open("notes.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text)""",
        "task": "Прочитай файл с заметками и выведи его содержимое.",
        "result": "Текст файла должен появиться в консоли."
    },

    {
        "number": 45,
        "title": "Добавление в файл",
        "description": "Дописываем данные в существующий файл.",
        "theory": "Режим a добавляет новые данные в конец файла и сохраняет старое содержимое.",
        "code": """with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("\\nНовая заметка")""",
        "task": "Сделай программу, которая добавляет новую заметку в файл.",
        "result": "Старые заметки должны сохраниться."
    },

    {
        "number": 46,
        "title": "JSON",
        "description": "Сохраняем структурированные данные.",
        "theory": "JSON удобен для хранения словарей и списков. В Python для него используется модуль json.",
        "code": """import json

user = {
    "name": "Alex",
    "age": 14
}

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, ensure_ascii=False, indent=2)""",
        "task": "Сохрани список пользователей в JSON-файл.",
        "result": "В файле должен появиться читаемый JSON."
    },

    {
        "number": 47,
        "title": "Модули и import",
        "description": "Используем готовый код Python.",
        "theory": "Модули содержат готовые функции и классы. Подключаются они через import.",
        "code": """import math

print(math.sqrt(25))
print(math.pi)""",
        "task": "Подключи math и вычисли квадратный корень.",
        "result": "Программа должна вывести корень числа."
    },

    {
        "number": 48,
        "title": "Модуль random",
        "description": "Работаем со случайными значениями.",
        "theory": "random позволяет получать случайные числа и выбирать случайные элементы.",
        "code": """import random

number = random.randint(1, 10)

print(number)""",
        "task": "Создай программу, которая случайно выбирает элемент списка.",
        "result": "При каждом запуске может выбираться другой элемент."
    },

    {
        "number": 49,
        "title": "Модуль datetime",
        "description": "Работаем с датой и временем.",
        "theory": "datetime позволяет получать текущую дату и время и выполнять операции с ними.",
        "code": """from datetime import datetime

now = datetime.now()

print(now)
print(now.year)
print(now.month)
print(now.day)""",
        "task": "Выведи текущий год, месяц и день.",
        "result": "Программа должна показать текущую дату."
    },

    {
        "number": 50,
        "title": "Финальный проект: список задач",
        "description": "Объединяем знания Python в одном проекте.",
        "theory": "В проекте используются списки, функции, циклы, условия, input() и enumerate(). Это уже настоящий небольшой консольный проект.",
        "code": """tasks = []

while True:
    print()
    print("1 — добавить задачу")
    print("2 — показать задачи")
    print("3 — удалить задачу")
    print("4 — выйти")

    choice = input("Выбор: ")

    if choice == "1":
        task = input("Новая задача: ")
        tasks.append(task)
        print("Задача добавлена")

    elif choice == "2":
        if not tasks:
            print("Задач пока нет")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if not tasks:
            print("Удалять нечего")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                number = int(input("Номер задачи: "))
                removed = tasks.pop(number - 1)
                print("Удалена:", removed)
            except (ValueError, IndexError):
                print("Неверный номер")

    elif choice == "4":
        print("До встречи!")
        break

    else:
        print("Неизвестная команда")""",
        "task": "Добавь в проект возможность отмечать задачу выполненной.",
        "result": "В конце у тебя должен получиться небольшой настоящий менеджер задач."
    }
]


@app.route("/")
def home():
    if session.get("username"):
        return redirect("/learn")

    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            return "Заполни все поля", 400

        if username in users:
            return "Такой пользователь уже существует", 400

        users[username] = generate_password_hash(password)
        session["username"] = username

        return redirect("/learn")

    return render_template("register.html")


@app.route("/learn")
def learn():
    if not session.get("username"):
        return redirect("/register")

    return render_template(
        "learn.html",
        lessons=lessons,
        username=session.get("username")
    )


@app.route("/lesson/<int:number>")
def lesson(number):
    if not session.get("username"):
        return redirect("/register")

    if number < 1 or number > len(lessons):
        return "Урок не найден", 404

    lesson_data = lessons[number - 1]

    return render_template(
        "lesson.html",
        lesson=lesson_data,
        total_lessons=len(lessons)
    )


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        password = request.form.get("password", "")

        if password == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect("/admin")

        return "Неверный пароль"

    if not session.get("admin"):
        return """
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>Админка — PythonSchool</title>
            <style>
                * {
                    box-sizing: border-box;
                }

                body {
                    margin: 0;
                    min-height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    background: #0b1020;
                    color: white;
                    font-family: Arial, sans-serif;
                }

                .box {
                    width: 90%;
                    max-width: 420px;
                    padding: 35px;
                    border: 1px solid #26345f;
                    border-radius: 20px;
                    background: #121a30;
                    text-align: center;
                }

                input {
                    width: 100%;
                    padding: 14px;
                    margin: 15px 0;
                    border: 0;
                    border-radius: 10px;
                }

                button {
                    width: 100%;
                    padding: 14px;
                    border: 0;
                    border-radius: 10px;
                    background: #4f7cff;
                    color: white;
                    font-weight: bold;
                    cursor: pointer;
                }
            </style>
        </head>

        <body>
            <div class="box">
                <h1>🔐 Админка</h1>
                <p>Введите пароль администратора</p>

                <form method="post">
                    <input
                        type="password"
                        name="password"
                        placeholder="Пароль"
                        required
                    >

                    <button type="submit">
                        Войти
                    </button>
                </form>
            </div>
        </body>
        </html>
        """

    return render_template(
        "admin.html",
        users_count=len(users),
        lessons_count=len(lessons)
    )


@app.route("/admin/logout")
def admin_logout():
    session.pop("admin", None)
    return redirect("/learn")


if __name__ == "__main__":
    app.run(debug=True, port=5001)