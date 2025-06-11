import telebot
from telebot import types
import pandas as pd
df = pd.DataFrame(columns=["Username", "trade.link"], data=[["User1","https://steamcommunity.com/tradeoffer/new/?partner=1111111&token=ZoVCcFtC"],
                                                            ["User2", "https://steamcommunity.com/tradeoffer/new/?partner=2222222&token=ZXCghoul"],
                                                            ["User3", "https://steamcommunity.com/tradeoffer/new/?partner=3333333&token=SP-Burg"],
                                                            ["User4", "https://steamcommunity.com/tradeoffer/new/?partner=4444444&token=ZX32Hert"],
                                                            ["User5", "https://steamcommunity.com/tradeoffer/new/?partner=6665555&token=ZX24Scrol"],
                                                            ["User6", "https://steamcommunity.com/tradeoffer/new/?partner=7775555&token=ZB72Brot"],
                                                            ["User7", "https://steamcommunity.com/tradeoffer/new/?partner=8885555&token=ZG67Jrei"],
                                                            ["User8", "https://steamcommunity.com/tradeoffer/new/?partner=9995555&token=ZX54Feol"],
                                                            ["User9", "https://steamcommunity.com/tradeoffer/new/?partner=1111555&token=PV22Deri"],
                                                            ["User10", "https://steamcommunity.com/tradeoffer/new/?partner=2222555&token=ZH44Derti"],
                                                            ["User11", "https://steamcommunity.com/tradeoffer/new/?partner=3333555&token=ZP27Pont"],
                                                            ["User12", "https://steamcommunity.com/tradeoffer/new/?partner=4444555&token=ZK94Fint"],
                                                            ["User13", "https://steamcommunity.com/tradeoffer/new/?partner=6666555&token=KJ27Fluo"],
                                                            ["User14", "https://steamcommunity.com/tradeoffer/new/?partner=7777555&token=UI84Sctil"],
                                                            ["User15", "https://steamcommunity.com/tradeoffer/new/?partner=8888555&token=SV09froul"]])

print(df[df['Username'].isin(["User1","User2","User3","User4","User5","User6","User7","User8","User9","User10","User11","User12","User13","User14","User15"])]["trade.link"].values)
df.to_excel("excel_to_bot.xlsx", index=False)

API_TOKEN = '7922085084:AAGiiN-a6jYqsKbs7LnMK42rscFGHD72DXk'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcom(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text='AWP', callback_data='AWP')
    button2 = telebot.types.InlineKeyboardButton(text='AK-47', callback_data='AK-47')
    button3 = telebot.types.InlineKeyboardButton(text='Knife', callback_data='Knife')
    button4 = telebot.types.InlineKeyboardButton(text='Desert Eagle', callback_data='Desert Eagle')
    button5 = telebot.types.InlineKeyboardButton(text='M4A4', callback_data='M4A4')
    markup.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, 'Приветствую тебя на бесплатной торговой площадке, нажми на любой скин и забери его себе!', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'AWP')
def ak(call):
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text='AWP | Gungnir', callback_data='1')
    button2 = telebot.types.InlineKeyboardButton(text='AWP | Containment Breach', callback_data='2')
    button3 = telebot.types.InlineKeyboardButton(text='AWP | Dragon Lore', callback_data='3')
    markup.add(button1, button2, button3)
    bot.send_message(call.message.chat.id, 'Выберете нужный вам скинчик', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'AK-47')
def ak(call):
    markup = telebot.types.InlineKeyboardMarkup()
    button4 = telebot.types.InlineKeyboardButton(text='AK-47 | Inheritance', callback_data='4')
    button5 = telebot.types.InlineKeyboardButton(text='AK-47 | Asiimov', callback_data='5')
    button6 = telebot.types.InlineKeyboardButton(text='AK-47 | Bloodsport', callback_data='6')
    markup.add(button4, button5, button6)
    bot.send_message(call.message.chat.id, 'Выберете нужный вам скинчик', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'Knife')
def ak(call):
    markup = telebot.types.InlineKeyboardMarkup()
    button7 = telebot.types.InlineKeyboardButton(text='Navaja Knife | Marble Fade', callback_data='7')
    button8 = telebot.types.InlineKeyboardButton(text='Karambit | Case Hardened', callback_data='8')
    button9 = telebot.types.InlineKeyboardButton(text='Knife | Gamma Doppler', callback_data='9')
    markup.add(button7, button8, button9)
    bot.send_message(call.message.chat.id, 'Выберете нужный вам скинчик', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'Desert Eagle')
def ak(call):
    markup = telebot.types.InlineKeyboardMarkup()
    button10 = telebot.types.InlineKeyboardButton(text='Desert Eagle | Fennec Fox', callback_data='10')
    button11 = telebot.types.InlineKeyboardButton(text='Desert Eagle | Hand Cannon', callback_data='11')
    button12 = telebot.types.InlineKeyboardButton(text='Desert Eagle | Code Red', callback_data='12')
    markup.add(button10, button11, button12)
    bot.send_message(call.message.chat.id, 'Выберете нужный вам скинчик', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'M4A4')
def ak(call):
    markup = telebot.types.InlineKeyboardMarkup()
    button13 = telebot.types.InlineKeyboardButton(text='M4A4 | Howl', callback_data='13')
    button14 = telebot.types.InlineKeyboardButton(text='M4A4 | Asiimov', callback_data='14')
    button15 = telebot.types.InlineKeyboardButton(text='M4A4 | Neo-Noir', callback_data='15')
    markup.add(button13, button14, button15)
    bot.send_message(call.message.chat.id, 'Выберете нужный вам скинчик', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def ak(call):
    bot.send_message(call.message.chat.id, 'Мабой дропни свою ссылочку на стимчик')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if 'http' in message.text:
        bot.send_message(message.chat.id, 'Молодец, трейд уже отправлен, играй, живи и кайфуй')
    else:
        pass

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,"Ты пишешь мне с желание получить бесплатные скины, а я даю тебе их по твоей же трейд ссылке")

bot.infinity_polling()

