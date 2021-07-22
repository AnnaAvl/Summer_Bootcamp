import random

# Список слов для игры
arr = ['арбуз', 'машина', 'банан', 'дерево', 'кукла',
       'майка', 'дверь', 'солнце', 'картина', 'колесо',
       'велосипед', 'ручка', 'молния', 'друг', 'стоянка']


def hangman():
    # Число ошибок
    miss = 10
    # Выбираем рандомное слово из списка
    word = random.choice(arr).lower()
    # Строка, в которую будем записывать названные буквы
    letters = ''
    # Строка для проверки, содержащая буквы, которые могут быть названы
    abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    # Загаданное слово шифруем символами "_" и выводим игроку
    guess_word = '_' * len(word)
    print(guess_word)
    # Спрашиваем у игрока букву, пока он не угадает слово
    # или не использует все попытки
    while miss > 0 and word != guess_word:
        print('Назовите букву')
        # Просим пользователя назвать букву, переводим в нижний
        # регистр и проверяем ее с помощью функции check_letter()
        letter = check_letter(input().lower(), abc, letters)
        # Если загаданное слово не содержит букву, которую назвал
        # пользователь, отнимаем одну жизнь, добавляем букву в список
        # названных, выводим сообщение об ошибке
        if word.find(letter) == -1:
            miss -= 1
            letters = add_letter(letters, letter)
            print('Неверно!')
        else:
            # В противном случае, добавляем букву в список названных
            letters = add_letter(letters, letter)
            index = -1
            # Пока в слове, которое видит игрок, все нужные символы "_"
            # не будут заменены названной буквой, определяем в загаданном
            # слове индексы буквы и в слове игрока символы "_" с данным
            # индексом заменяем на нее
            while guess_word.count(letter) != word.count(letter):
                index = word.find(letter, index+1)
                guess_word = guess_word[:index] + letter + guess_word[index+1:]
        # Выводим слово с вписанными угаданными буквами и сообщение о
        # кол-ве оставшихся ошибок и названных буквах
        print('\nОсталось ошибок:' + str(miss) + '\nНазванные буквы: ' + letters + '\n' + guess_word)
    # Если закончились попытки, выводим сообщение о проигрыше и загаданное слово.
    # Иниче, если слово угадано, выводим сообщение о выигрыше
    if miss == 0:
        print('Вы проиграли\n' + word)
    else:
        print('Вы выиграли')
    end_of_game()


def check_letter(letter, abc, letters):
    # Если введено более/менее одной буквы, она не содержится в русском алфавите
    # или она уже была названа, просим пользователя ввести другую букву.
    # Если буква прошла все проверки, возвращаем ее
    while len(list(letter)) != 1 or abc.find(letter) == -1 or letters.find(letter) != -1:
        print('Назовите другую букву')
        letter = input().lower()
    return letter


def end_of_game():
    # Спрашиваем у пользователя, хочет ли он сыграть еще раз.
    print('Хотите сыграть еще раз? (1 - да, 0 - нет)')
    ans = str(input())
    if ans == '1':
        print('\nНовая игра')
        # Начинаем новую игру
        hangman()
    elif ans == '0':
        print('\nИгра окончена')
        # Выходим из игры
        return
    else:
        print('Неверно введен ответ')
        # При некорректном вводе, спрашиваем пользователя еще раз
        end_of_game()
    return


def add_letter(letters, letter):
    # Если список букв пуст, добавляем букву.
    # Если буквы уже имеются, добавляем их через запятую,
    # для корректного вывода пользователю
    if letters == '':
        letters += letter
    else:
        letters = letters + ', ' + letter
    return letters


hangman()