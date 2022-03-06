import telebot

command = """
/print  - напечать все задачи на заданную дату. Запрос по шаблону:
/print дата_задачаи
Например: /print 05.03.2022

--------------------------------------------------------------------------------------------          
/todo - добавить задачу. Добавлять обязательно по шаблону:
/todo дата_задачи текст_задачи
Например: /print 05.03.2022 Помыть голову

--------------------------------------------------------------------------------------------            
/help - Напечатать help
          """
bd = {}

token = '5213595106:AAE8QXamur2cekLbr5goDSKnZIjYR6l6sfM'

bot = telebot.TeleBot(token)

r = True

def TODO(a, b):
    if a not in bd.keys():
        bd[a] = [b]
    else:
        bd[a].append(b)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, command)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, command)

@bot.message_handler(commands=['todo'])
def todo(message):
    if len(message.text.split()) < 3:
        bot.send_message(message.chat.id, 'Ввели команду не по шаблону.')
    else:
        com = message.text.split(maxsplit=2)
        d = com[1]
        z = com[2]
        TODO(d, z)
        bot.send_message(message.chat.id, f'Задача "{z}" добавлена на {d}.')
        print(bd)

@bot.message_handler(commands=['print'])
def ptint(message):
    com = message.text.split(maxsplit=1)
    if len(com) < 2:
        bot.send_message(message.chat.id, 'Ввели команду не по шаблону.')
    else:
        d = com[1]
        if d in bd.keys():
            bot.send_message(message.chat.id, f'Задача на {d}: {bd[d]}')
        else:
            bot.send_message(message.chat.id, 'На эту дату нет задач.')

bot.polling(none_stop=r)