import telebot
bot = telebot.TeleBot('1760887475:AAEiHGCMhulkWHTVe4hSRH6chMsyl5vxG4M')
name = ''
ans = ''


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global name
    text = message.text
    if text == "/help":
        bot.send_message(message.from_user.id, "Do not contact me for help!( ͡° ͜ʖ├┬┴┬")
    elif text == "/start":
        bot.send_message(message.from_user.id, "Hello!")
        bot.send_message(message.from_user.id, "What is your name(ಠ_ಠ)?")
        bot.register_next_step_handler(message, get_name)
    elif text == '/calculate':
        bot.register_next_step_handler(message, calculate)
    elif text == '/bye':
        bot.send_message(message.from_user.id, 'bye bye, dear friend(＿ ＿*) Z z z')
    else:
        bot.send_message(message.from_user.id, 'ヽ(°□° )ノ')


def get_name(message):
    global name
    global ans
    if message.text == '/guess':
        bot.send_message(message.from_user.id, 'ok╰(▔∀▔)╯')
        name = message.from_user.first_name
        bot.send_message(message.from_user.id, 'Is your name ' + name + '?( ˘⌣˘)♡(˘⌣˘ )')
        bot.register_next_step_handler(message, get_answer)
    else:
        name = message.text
        bot.send_message(message.from_user.id, "Hello, " + name + 'ʕ ᵔᴥᵔ ʔ')


def get_answer(message):
    global ans
    ans = message.text
    if ans == 'no':
        bot.send_message(message.from_user.id, "it's a lie(‡▼益▼)")
    else:
        bot.send_message(message.from_user.id, "(´｡• ᵕ •｡) ♡")


def calculate(message):
    try:
        eval(message.text)
        bot.send_message(message.from_user.id, eval(message.text))
        bot.send_message(message.from_user.id, '(づ￣ ³￣)づ')
    except (ValueError, SyntaxError, NameError):
        bot.send_message(message.from_user.id, "I don't know how to calculate thatヽ(￣～￣　)ノ")


bot.polling(none_stop=True, interval=0)
