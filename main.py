# print("Артём")
# print("14")


# print("Добро пожаловать в квиз по стартапам!")
# print("Ответь на следующие вопросы: ")


# number = 10
# print(number * 5)
# number2 = 7
# print(number + number2)


# message = "Я изучаю программирование"
# print(message)




# print("Добро пожаловать в квиз!")
# print("Выбери тему вопросов: ")
# print(" ")
# print("1) Бизнес" , "2) Игры")
#
# user_answer = input("Введи название темы: ")
# if user_answer.lower() == "бизнес":
#     print("Ответь на следующие вопросы: ")
#     print(" ")
#     questions1 = [
#         "1. Как называется компания, которая создается для развития новой идеи или инновационного продукта?",
#         "2. Как назвается человек или компания, который вкладывает деньги в бизнес с целью получения прибыли?",
#         "3. Как называется капитал, который дают инвесторы на развитие стартапа?",
#         "4. Как пишется минимально жизнеспособный продукт, который создается для тестирования идей и концепций?",
#         "5. Какой план создают перед тем, как открывать стартап и занимать деньги?",
#         "6. Как называются другие компании на рынке, которые предлагают аналогичные товары или услуги?",
#         "7. Как называется разница между выручкой и затратами компании?"
#     ]
#     answers1 = [
#         "Стартап", "Инвестор", "Инвестиция", "MVP", "Бизнес-план", "Конкуренты", "Прибыль"
#     ]
#
#     score = 0
#
#     print(questions1[0])
#     user_answer = input("Введи свой ответ: ")
#     if user_answer.lower() == answers1[0].lower():
#         print("Правильно!")
#         score = score + 1
#         print("+1 ОЧКО!")
#     else:
#         print("Неправильно.")
#
#     print(questions1[1])
#     user_answer = input("Введи свой ответ: ")
#     if user_answer.lower() == answers1[1].lower():
#         print("Правильно!")
#         score = score + 1
#         print("+1 ОЧКО!")
#     else:
#         print("Неправильно.")
#
#     print(questions1[2])
#     user_answer = input("Введи свой ответ: ")
#     if user_answer.lower() == answers1[2].lower():
#         print("Правильно!")
#         score = score + 1
#         print("+1 ОЧКО!")
#     else:
#         print("Неправильно.")
#
#     print(questions1[3])
#     user_answer = input("Введи свой ответ: ")
#     if user_answer.lower() == answers1[3].lower():
#         print("Правильно!")
#         score = score + 1
#         print("+1 ОЧКО!")
#     else:
#         print("Неправильно.")
#
#     print(questions1[4])
#     user_answer = input("Введи свой ответ: ")
#     if user_answer.lower() == answers1[4].lower():
#         print("Правильно!")
#         score = score + 1
#         print("+1 ОЧКО!")
#     else:
#         print("Неправильно.")
#
#     print(questions1[5])
#     user_answer = input("Введи свой ответ: ")
#     if user_answer.lower() == answers1[5].lower():
#         print("Правильно!")
#         score = score + 1
#         print("+1 ОЧКО!")
#     else:
#         print("Неправильно.")
#
#     print(questions1[6])
#     user_answer = input("Введи свой ответ: ")
#     if user_answer.lower() == answers1[6].lower():
#         print("Правильно!")
#         score = score + 1
#         print("+1 ОЧКО!")
#     else:
#         print("Неправильно.")
#
#     print(" ")
#
#     if score == 7:
#         print("У тебя 7 очка!")
#     if score == 6:
#         print("У тебя 6 очка!")
#     if score == 5:
#         print("У тебя 5 очка!")
#     if score == 4:
#         print("У тебя 4 очка!")
#     if score == 3:
#         print("У тебя 3 очка!")
#     elif score == 2:
#         print("У тебя 2 очка")
#     elif score == 1:
#         print("У тебя 1 очко")
#     elif score == 0:
#         print("У тебя 0 очков")
#
#     print(" ")
#
#     if score > 5:
#         print("Это отличный результат! Ты много знаешь о стартапах.")
#     elif score > 3:
#         print("Неплохой результат! Как здорово, что тебе предстоит узнать ещё так много о стартапах.")
#     else:
#         print("Видимо, ты только начинаешь свой путь к стартапам! Ты ещё много чего узнаешь о мире, где мы живём.")
#
#
# if user_answer.lower() == "игры":
#     print("Ответь на следующие вопросы:   (ОТВЕЧАЙ НА ВСЕ ВОПРОСЫ НА АНГЛИЙСКОМ ЯЗЫКЕ)")
#     print(" ")
#     questions2 = [
#         "1. Как называется игра, в которой есть строительство в режиме БАТЛ РОЯЛЬ?",
#         "2. Как называется игра, в которой есть позиции, тиры и тавера в режиме 5 на 5?",
#         "3. Как называется игра, в которой есть плент бомбы, и игроки играют от 1 лица?"
#     ]
#     answers2 = [
#         "Fortnite", "Dota2", "CS2"
#     ]
#
#     score = 0
#
#     print(questions2[0])
#     user_answer1 = input("Введи свой ответ: ")
#     if user_answer1.lower() == answers2[0].lower():
#         print("Правильно!")
#         score = score + 1
#         print("+1 ОЧКО!")
#     else:
#         print("Неправильно.")
#
#     print(questions2[1])
#     user_answer1 = input("Введи свой ответ: ")
#     if user_answer1.lower() == answers2[1].lower():
#         print("Правильно!")
#         score = score + 1
#         print("+1 ОЧКО!")
#     else:
#         print("Неправильно.")
#
#     print(questions2[2])
#     user_answer1 = input("Введи свой ответ: ")
#     if user_answer1.lower() == answers2[2].lower():
#         print("Правильно!")
#         score = score + 1
#         print("+1 ОЧКО!")
#     else:
#         print("Неправильно.")
#
#     print(" ")
#
#     if score == 3:
#         print("У тебя 3 очка!")
#     elif score == 2:
#         print("У тебя 2 очка")
#     elif score == 1:
#         print("У тебя 1 очко")
#     elif score == 0:
#         print("У тебя 0 очков")
#
#     if score == 3:
#         print("Это отличный результат! Ты много знаешь о играх.")
#     elif score == 2:
#         print("Неплохой результат! Как здорово, что тебе предстоит узнать ещё так много о играх.")
#     else:
#         print("Видимо, ты только начинаешь свой путь к играм! Ты ещё много чего узнаешь о мире, где мы живём.")


# product = input("Введи продукт: ")
# money = int(input("Введи цену продукта: "))
#
# print("Сегодня скидки!")
# print("Вы купили", product, "за", money - 10, "рублей")


# game = input("Какая твоя любимая игра? ")
# ocenka = int(input("Насколько ты хорош(а) в этой игре от 1 до 10? "))
#
# print(game)
# print(ocenka)


# projects = ["Сайт для отеля", "Игра-стрелялка", "Калькулятор", "Видеохостинг"]
# print(projects[2])


# print("ab" in "abc")
# x = "артём"
# print(x.index("т"))
# print(x[2])

# x = 'abcdefghijklmnopqrstuvwxyz'
# print(x.index("p"))
# print(x.index("y"))
# print(x.index("t"))
# print(x.index("h"))
# print(x.index("o"))
# print(x.index("n"))

# x = "артём"
# print(x.lower())
# print(x.upper())
# print(len(x))

# a = "Привет, как дела?"
# b = a.count("а")
# print(b)

# message = "Делать зарядку нужно каждую неделю!"
# b = message.replace("каждую неделю", "каждый день")
# print(b)

# word = input()
# print(word[::-1])

# money = int(input())
# if money >= 35:
#     print("Пирожок куплен")
# elif money < 35:
#     print("Не хватает денег")

# ticket = input()
# if ticket == "Сочи":
#     print("Проходите на поезд")
# if ticket != "Сочи":
#     print("Ваш поезд ушёл 2 часа назад")

# is_open = True
#
# days = int(input())
#
# if is_open:
#     print("Магазин открыт!")
#     days = days + 1
#
# print("Количество дней: ", days)

# money = int(input())
# if money >= 35:
#     print("Оплата прошла успешно")
#     money = money - 35
# else:
#     print("Недостаточно средств")
#
# print("Осталось: ", money)

# print("Меню:")
# print("1. Шаверма")
# print("2. Шаурма")
# print("3. Фалафель")
# print("4. Самса")
#
# food_number = input("Введите номер блюда, которое хотите заказать: ")
#
# if food_number == "1":
#     print("Вы заказали шаверму!")
# elif food_number == "2":
#     print("Вы заказали шаурму!")
# elif food_number == "3":
#     print("Вы заказали фалафель!")
# elif food_number == "4":
#     print("Вы заказали самсу!")
# else:
#     print("Блюда с таким номером нет.")

# order_cost = 250 # стоимость заказа
# discount_cost = 1 # множитель скидки. Если 1, то платят полную стоимость, если 0, то не платят ничего.
# 
# age = int(input("Введите свой возраст: "))
# 
# if age < 18:
#     discount_cost = 0.95
# elif age < 30:
#     discount_cost = 0.85
# elif age < 60:
#     discount_cost = 0.75
# elif age < 100:
#     discount_cost = 0.50
# 
# 
# print("Стоимость заказа со скидкой:", order_cost * discount_cost)

# a = int(input())
# b = int(input())
# if a < b:
#     print(b)
# elif a > b:
#     print(a)
# elif a == b:
#     print("Числа равны")

# day = 1
#
# while day <= 30:
#     print(f"Я перевернул календарь, а там {day} сентября")
#     day += 1
#
# print("Сентябрь закончился")

# count = 1
#
# while count <= 100:
#     print(count)
#     count += 3


# import random
# number = random.randint(0, 5)
# print("Попробуй угадать число от 0 до 5!")
# user_number = int(input("Введи число: "))
# attempts = 1
# while user_number != number and attempts < 3
#     print("Не угадал")
#     user_number = int(input("Введи число"))
#     attempts += 1
# if user_number == number:
#     print(f"Это верно, я загадал число {number}")
#     print("Ты выиграл")
# else:
#     print("Ты проиграл")


# true_login = "sky@gmail.com"
#
# true_password = "12345"
#
# user_login = input("Введи логин: ")
# user_password = input("Введи пароль: ")
# if user_login == true_login and user_password == true_password:
#     print("Вы вошли в систему")
# else:
#     print("Логин или пароль неверный")


# for i in range(15):
#     print("Купи слона!")


# a = 0
# for i in range(0, 101):
#     # if i%2 == 0:
#     	a += i
# print(a)


# a = 1
# for i in range(5, 16):
#     a *= i
# print(a)




# from PIL import Image, ImageDraw, ImageFont
#
# print("Генератор мемов запущен!")
#
# top_text = input("Введите верхний текст мема: ")
# bottom_text = input("Введите нижний текст мема: ")
# print(top_text + " " + bottom_text)
#
# print("Список картинок:")
# print("1. Кот в ресторане")
# print("2. Кот в очках")
#
# image_number = int(input("Введи номер картинки: "))
#
# if image_number == 1:
#     image_file = "Кот в ресторане.png"
# elif image_number == 2:
#     image_file = "Кот в очках.png"
# print(image_file)
#
# image = Image.open(image_file)
# wigth, height = image.size
#
# draw = ImageDraw.Draw(image)
#
# font = ImageFont.truetype('arial.ttf', size=70)
#
# text = draw.textbbox((0, 0), top_text, font)
# text_wigth = text[2]
#
# draw.text(((wigth - text_wigth) / 2, 10), top_text, font=font, fill='black')
#
# text1 = draw.textbbox((0, 0), bottom_text, font)
# text_wigth1 = text1[2]
# text_height1 = text1[3]
#
# draw.text(((wigth - text_wigth1) / 2, height - text_height1 - 20), bottom_text, font=font, fill='black')
#
# image.save("new_meme.jpg")
# image.show()




# import turtle
#
# turtle.shape("turtle")
#
# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)
#
# turtle.mainloop()


# import turtle
#
# turtle.shape("turtle")
# turtle.pensize(3)
#
# for i in range(3):
#     turtle.pencolor('red')
#     turtle.forward(30)
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(30)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.left(90)
#     turtle.pencolor('blue')
#     turtle.forward(30)
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(30)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.left(90)
#
# turtle.mainloop()


# import turtle
# import random
# turtle.shape("turtle")
# turtle.pensize(3)
# for i in range(5):
#     turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
# turtle.mainloop()


# import turtle
# import random
# turtle.shape("turtle")
# for i in range(10):
#     for i in range(4):
#         turtle.forward(50)
#         turtle.right(90)
#     turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
# turtle.mainloop()


# import turtle
# turtle.shape("turtle")
# turtle.dot(100)
# turtle.forward(100)
# turtle.circle(50)


# import turtle
# turtle.speed(30)
# size = 10
# for i in range(0, 60):
#     turtle.circle(size)
#     turtle.left(5)
#     size = size + 10
# turtle.mainloop()


# items = [input(), input(), input()]
# print(items)


# deals = [
#     'погулять с друзьями',
#     'почитать новости и сцепиться с кем-нибудь в комментах',
#     'почитать книжку',
#     'рассмотреть потолок',
#     'поиграть в Brawl stars',
#     'помыть посуду',
#     'сказать родителям, что заболел',
#     'залипнуть в летсплеях по роблоксу',
# ]
# print(deals)
# ind=int(input('введите индекс: '))
# text=input('введите новое значение: ')
# deals[ind] = text
# print(deals)


# months = [
#   'январь', 'февраль', 'март', 'апрель',
#   'май', 'июнь', 'июль', 'август',
#   'сентябрь', 'октябрь', 'ноябрь', 'декабрь'
# ]
# print(months[::-1])


# months = [
# 'январь', 'февраль', 'март', 'апрель',
# 'май', 'июнь', 'июль', 'август',
# 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'
# ]

# # Продолжи решение ниже:
# winter = months[-1:] + months[:2]
# spring = months[2:5] # Пример решения
# summer = months[5:8]
# autumn = months[8:11]
# print('Зима: ' , winter)
# print('Весна: ' , spring)
# print('Лето: ' , summer)
# print('Осень: ' , autumn)



import os
import random

clear = lambda: os.system('cls')

print('Пивет! Я загадал слово, твоя задача - угадать его по буквам.')
input('*Нажми Enter, чтобы продолжить*')
clear()
print('Поехали!')

words = ['огурец', 'машина', 'карта']
word = random.choice(words)

letters = []
isWin = True
hp = 10

while hp > 0:
    isWin = True
    letter = input('Введите букву: ')
    letters.append(letter)
    print(letters)
    for symb in word:
        if symb in letters:
            print(symb, end=' ')
        else:
            print('*', end=' ')
            isWin = False
    print()

    if isWin:
        print('Ты угадал! Молодец!')
        break

    if letter not in word:
        hp -= 1
        print(f'Осталось попыток: {hp}')



