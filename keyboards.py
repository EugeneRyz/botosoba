from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

backbtn = KeyboardButton('')

mybtn1 = KeyboardButton('')
mybtn2 = KeyboardButton('')
mybtn3 = KeyboardButton('')


#кнопки меню первого уровня, каждая с отдельной клавой:

menukb1 = InlineKeyboardMarkup(row_width=1)
menubtn1 = InlineKeyboardButton('ДА', callback_data='mybtn1')
menukb1.add(menubtn1)

menukb2 = InlineKeyboardMarkup(row_width=1)
menubtn2_1 = InlineKeyboardButton('OK', callback_data='okbtn')
menubtn2_2 = InlineKeyboardButton('ПОВТОР', callback_data='povtorbtn')
menukb2.add(menubtn2_1)
menukb2.add(menubtn2_2)

menukb3 = InlineKeyboardMarkup(row_width=1)
menubtn3_1 = InlineKeyboardButton('OK', callback_data='okbtn1')
menubtn3_2 = InlineKeyboardButton('ПОВТОР', callback_data='povtorbtn1')
menukb3.add(menubtn3_1)
menukb3.add(menubtn3_2)


menukb4 = InlineKeyboardMarkup(row_width=1)
menubtn4_1 = InlineKeyboardButton('OK', callback_data='okbtn2')
menubtn4_2 = InlineKeyboardButton('ПОВТОР', callback_data='povtorbtn2')
menukb4.add(menubtn4_1)
menukb4.add(menubtn4_2)
