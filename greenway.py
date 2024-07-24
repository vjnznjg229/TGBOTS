import telebot

from telebot import types
TOKEN=('7420849186:AAGMqf7IxRFeRGmwc5rHvTA-BqLs4LQs5Xk')
bot =telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1= types.InlineKeyboardButton('Каталог🌟',callback_data='1')
    item2 = types.InlineKeyboardButton('Корзина🛒',callback_data='2')
    item3 = types.InlineKeyboardButton('Техподдержка🛠️', callback_data='3')
    markup.add(item1,item2,item3)
    bot.send_message(message.chat.id,f'Привет!Это бета тест',reply_markup=markup)
@bot.callback_query_handler(func=lambda call:call.data in ['1','2','3'])
def vibor_menu(call):
    if call.data == '1':
        menu(call.message)
    if call.data =='2':
        pass
    if call.data== '3':
        bot.send_message(call.message.chat.id, 'ТГ техподдержки https://t.me/saltykodashok')


@bot.message_handler(commands=['2345165723'])
def menu(message):
        markup = types.InlineKeyboardMarkup(row_width=1)
        item4 = types.InlineKeyboardButton('Файберы и губки.', callback_data='4')
        item5 = types.InlineKeyboardButton('---', callback_data='5')
        item6 = types.InlineKeyboardButton('---', callback_data='6')
        markup.add(item4, item5, item6)
        bot.send_message(message.chat.id, 'Выберите раздел.', reply_markup=markup)
items=[       '360₽-ФАЙБЕР ДЛЯ МЫТЬЯ ПОСУДЫ S1,20×16см',
    '420₽-ГУБКА ДЛЯ МЫТЬЯ ПОСУДЫ S15,15,5×9см',
    '710₽-ФАЙБЕР УНИВЕРСАЛ A1,40×30см',
    '710₽-ДИСК ИНВОЛВЕР S2,Ø 12см',

    '790₽-ФАЙБЕР РЕБРИСТЫЙ S3,30×30см',
    '730₽-СКРАБЕР ТВИСТ S4,30×30см',
    '840₽-ФАЙБЕР ВЕЛЬВЕТОВЫЙ S5,40×40см',
    '720₽-СПОНЖ СПЛИТТЕР S6,22×17,5см',

    '1130₽-ФАЙБЕР ИНВОЛВЕР S7,30×23см',
        '1000₽-ГУБКА ИНВОЛВЕР S8,14,5×7см',
    '1030₽-ВАРЕЖКА УНИВЕРСАЛЬНАЯ A2,27×20см',
        '1200₽-ФАЙБЕР ДЛЯ КУХНИ A3,60×40см',

        '1430₽-ВАРЕЖКА ТВИСТ S9,25×19см',
        '1370₽-ВАРЕЖКА ИНВОЛВЕР S10,23×21см',
        '530₽-ФАЙБЕР ПОЛИРУЮЩИЙ P2,40×30см',
        '1130₽-СПОНЖ ИНВОЛВЕР S11,26,5×15,5см',

        '780₽-ФАЙБЕР ТВИСТ S12,40×40см',
        '1140₽-ФАЙБЕР ТВИСТ ДЛЯ ПОЛА S13,60×40см',
        '780₽-СПОНЖ ТВИСТ S14,30×16см',
        '650₽-ФАЙБЕР УНИВЕРСАЛЬНЫЙ A4,40×40см',

        '590₽-ФАЙБЕР ДЛЯ С',
        '210₽-ФАЙБЕР ДЛЯ ОПТИКИ P3,15×15см',
        '300₽-ФАЙБЕР ДЛЯ ЭКРАНОВ P4,20×15см',

        '2150₽-НАБОР ДЛЯ ЧИСТКИ СЛОЖНЫХ ЗАГРЯЗНЕНИЙ Heavy-duty сleaning',
        '1990₽-НАБОР ДЛЯ КУХНИ Kitchen cleaning',
        '2150₽-НАБОР ДЛЯ ОБЩЕЙ УБОРКИ General cleaning',
        '2170₽-НАБОР ДЛЯ УБОРКИ ВАННОЙ Bathroom cleaning']
ITEMS_PER_RANGE=4

def generate_markup(page=0):
    markup=types.InlineKeyboardMarkup()
    start_index= page * ITEMS_PER_RANGE
    end_index = start_index + ITEMS_PER_RANGE


    for item in items[start_index:end_index]:
        button = types.InlineKeyboardButton(item,callback_data=f'item_{items.index(item)}')
        markup.add(button)

    if page > 0:
        markup.add(types.InlineKeyboardButton(text="<<",callback_data=f'page_{page - 1}'))

    if end_index < len(items):
        markup.add(types.InlineKeyboardButton(text=">>",callback_data=f'page_{page + 1}'))
    return markup
@bot.callback_query_handler(func=lambda call:call.data in ['4','5','6'])
def menu2(call):
    if call.data == '4':
        Fiber(call)
def Fiber(call):
    if call.data.startswith('page_'):
        text,page=call.data.split('_')

        markup = generate_markup(int(page))
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='Выбор элемента' ,
                              reply_markup=markup)

        # bot.send_message(call.message.chat.id, 'Выберите товар. GREEN FIBER HOME', reply_markup=markup)
    elif call.data.startswith('item_'):
        text,item_index=call.data.split('_')
        bot.send_message(call.message.chat.id,text=item_index)

bot.polling(none_stop=True)