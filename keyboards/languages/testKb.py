# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
# from telegram import ParseMode
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

import json

# from aiogram import Bot, Dispatcher, types
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# from database import get_user_by_id, insert_user, insert_message
# from states import MyStates, MESSAGES, USERS, User, user
# from aiogram.dispatcher import FSMContext
# from aiogram import Bot, Dispatcher, types
# import json
# userStorage = {}
# class Storage:
#     value = ''
#     old_value = ''
#     grade_value = ''
#     # lang_code = ''
#     user_language = ''
#     lang_message = ''
# #Русскоязычное меню:
# menu = []
#
# menu_pipe = []
# menu_sheet = []
# menu_roundBar = []
# menu_squareBar = []
# menu_beam = []
# menu_channel = []
# menu_corner = []
# menu_armature = []
# menu_hexagon = []
# menu_sphere = []
# def get_new_language():
#     with open('../../data/languages.json', 'r', encoding='utf-8') as file:
#         u_language = json.load(file)
#     return u_language
#
# async def user_language(message: types.Message, state: FSMContext):
#     # user = get_user_by_id(message.from_user.id)
#     user_id = message.from_user.id
#     new_lang = get_new_language()
#     u_language = new_lang
#     # try:
#     if user_id in userStorage:
#         userStorage[user_id] = Storage()
#         # if message.text == 'Change language':
#         #     if message.text in Keyboard_menu_change_language:
#         #         language_code =
#         for item in u_language:
#             if message.from_user.language_code or message.from_user.id or message.text in item:
#                 user_language = item[message.from_user.language_code][0]
#                 menu.append(user_language[0])
#                 menu_pipe.append(user_language[1])
#                 menu_sheet.append(user_language[2])
#                 menu_roundBar.append(user_language[3])
#                 menu_squareBar.append(user_language[4])
#                 menu_beam.append(user_language[5])
#                 menu_channel.append(user_language[6])
#                 menu_corner.append(user_language[7])
#                 menu_armature.append(user_language[8])
#                 menu_hexagon.append(user_language[9])
#                 menu_sphere.append(user_language[10])
#                 await message.answer(user_language)
#                 print(menu)
# await state.set_state(MyStates.all()[1])
# break  # Выходим из цикла после успешного выполнения
#             else:
#                 if len(userStorage[user_id].value) == 0:
#                     user_language = u_language[0][message.from_user.language_code][1]['lang_message']
#                     await message.answer(user_language)
#                     await state.set_state(MyStates.all()[1])
#                 else:
#                     user_language = u_language[0][message.from_user.language_code][2]['lang_message']
#                     await message.answer(user_language)
# except KeyError:
#     user_language = u_language[0][message.from_user.language_code][3]['lang_message']
# await message.answer(user_language)

# menu = []
#
# menu_pipe = []
# menu_sheet = []
# menu_roundBar = []
# menu_squareBar = []
# menu_beam = []
# menu_channel = []
# menu_corner = []
# menu_armature = []
# menu_hexagon = []
# menu_sphere = []

menu = ['Круг/кольцо', 'Квадрат/прямоугольник', 'Труба', 'Лист/полоса', 'Балка', 'Швеллер', 'Уголок', 'Шестигранник',
        'Арматура', 'Сфера/шар', 'Стандартный калькулятор',
        'Change language', 'Руководство пользователя']

menu_pipe = ['Круглая', 'Профильная', 'Главное меню']
menu_sheet = ['Лист', 'Полоса', 'Главное меню']
menu_roundBar = ['Круг', 'Кольцо', 'Главное меню']
menu_squareBar = ['Квадрат', 'Прямоугольник', 'Главное меню']
menu_beam = ['Тавровая', 'Двутавровая', 'Главное меню']
menu_channel = ['Равнополочный', 'Не равнополочный', 'Главное меню']
menu_corner = ['Равносторонний', 'Не равносторонний', 'Главное меню']
menu_armature = ['Материал и профиль', 'Главное меню']
menu_hexagon = ['Материал и профиль', 'Главное меню']
menu_sphere = ['Марка материала сферы/шара', 'Главное меню']

# from aiogram.types import ReplyKeyboardMarkup
# import json
# import os
#
# # Получаем абсолютный путь к текущему файлу
# current_dir = os.path.dirname(os.path.abspath(__file__))
#
# # Составляем путь к файлу 'languages.json' относительно текущего каталога
# json_file_path = os.path.join(current_dir, '../../data/languages.json')
#
# # Теперь используем этот путь при открытии файла


# class KeyboardManager:
#     def __init__(self):
#         self.languages = []
#
#     def load_languages(self):
#         # with open('../../data/languages.json', 'r', encoding='utf-8') as file:
#         # with open('../../data/languages.json', 'r', encoding='utf-8') as file:
#         #     self.languages = json.load(file)
#         with open(json_file_path, 'r', encoding='utf-8') as file:
#             self.languages = json.load(file)
#
#     def get_menu_for_language(self, language_code):
#         for language in self.languages:
#             if language['language_code'] == language_code:
#                 return language['menu']
#         # Если язык не найден, возвращаем английское меню
#         for language in self.languages:
#             if language['language_code'] == 'en':
#                 return language['menu']
#             print(language)
#         # Если даже английское меню не найдено, возвращаем пустой список
#         return []
#
# keyboard_manager = KeyboardManager()
# keyboard_manager.load_languages()
#
# # Пример создания клавиатуры для определенного языка
# def create_keyboard(language_code):
#     menu = keyboard_manager.get_menu_for_language(language_code)
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for item in menu:
#         keyboard.insert(item)
#     return keyboard


Keyboard_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_pipe = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_sheet = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_roundBar = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_squareBar = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_beam = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_channel = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_corner = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_hexagon = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_armature = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_sphere = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_diagonal = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_inscribed = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_described = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_stainless = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_pipeCounter = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

for i in menu:
    Keyboard_menu.insert(i)
for i in menu_pipe:
    Keyboard_menu_pipe.insert(i)
for i in menu_sphere:
    Keyboard_menu_sphere.insert(i)
for i in menu_sheet:
    Keyboard_menu_sheet.insert(i)
for i in menu_roundBar:
    Keyboard_menu_roundBar.insert(i)
for i in menu_squareBar:
    Keyboard_menu_squareBar.insert(i)
for i in menu_beam:
    Keyboard_menu_beam.insert(i)
for i in menu_channel:
    Keyboard_menu_channel.insert(i)
for i in menu_corner:
    Keyboard_menu_corner.insert(i)
for i in menu_hexagon:
    Keyboard_menu_hexagon.insert(i)
for i in menu_armature:
    Keyboard_menu_armature.insert(i)
menu_change_language = ['English', 'Deutsch', 'Italiano', 'Español', 'Français', '日本語', '中文', '한국어',
                        'Język polski', 'Čeština', 'Slovenský', 'Slovenski', 'Русский', 'Main menu']

Keyboard_menu_change_language = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for i in menu_change_language:
    Keyboard_menu_change_language.insert(i)


# def Grades():
#     Button1 = InlineKeyboardButton(text='Stainless steel', callback_data='Stainless steel')
#     Button2 = InlineKeyboardButton(text='Carbon steel', callback_data='Carbon steel')
#     Button3 = InlineKeyboardButton(text='High speed steel', callback_data='High speed steel')
#     Button4 = InlineKeyboardButton(text='Nickel heat-resistant alloys',
#                                    callback_data='Nickel heat-resistant alloys')
#     Button5 = InlineKeyboardButton(text='Iron-nickel heat-resistant alloys',
#                                    callback_data='Iron-nickel heat-resistant alloys')
#     Button6 = InlineKeyboardButton(text='Titanium alloys', callback_data='Titanium alloys')
#     Button7 = InlineKeyboardButton(text='Aluminium alloys', callback_data='Aluminium alloys')
#     Button8 = InlineKeyboardButton(text='Beryllium bronzes', callback_data='Beryllium bronzes')
#     Button9 = InlineKeyboardButton(text='Brass', callback_data='Brass')
#     Button10 = InlineKeyboardButton(text='Copper-nickel alloys', callback_data='Copper-nickel alloys')
#     Button11 = InlineKeyboardButton(text='Magnesium alloys', callback_data='Magnesium alloys')
#     Button12 = InlineKeyboardButton(text='Tin bronzes', callback_data='Tin bronzes')
#     Button13 = InlineKeyboardButton(text='Tinless bronzes', callback_data='Tinless bronzes')
#     Button14 = InlineKeyboardButton(text='All melalls', callback_data='All metalls')
#     Keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).add(Button1, Button2,
#                                                                            Button3, Button4, Button5, Button6, Button7,
#                                                                            Button8, Button9,
#                                                                            Button10, Button11, Button12, Button13,
#                                                                            Button14)
#     return Keyboard


# def start(update: Update, context: CallbackContext) -> None:
#     tooltip_text = "Это всплывающая подсказка!"
#     button_text = f"Наведите курсор на [Button 1](tooltip://{tooltip_text})"
#
#     update.message.reply_html(button_text, parse_mode=ParseMode.HTML)

logging.basicConfig(level=logging.INFO)


# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)


# @dp.message_handler(commands=['start'])
# async def tooltipFunk(message: types.Message):
#     tooltip_text = "Это всплывающая подсказка!"
#     button_text = f"Наведите курсор на [Button 1](tooltip://{tooltip_text})"
#
#     await message.reply_html(button_text, parse_mode=ParseMode.HTML)

async def tooltipFunk():
    tooltip_text = "Это всплывающая подсказка!"
    return tooltip_text


# textmessage = ["Text", "Test1"]


# def read_json_file(file_path):
#     # with open(file_path, 'r', encoding='utf-8') as file:
#     # with open('../data/metals.json', 'r', encoding='utf-8') as file:
#     with open('../../data/metals.json', 'r', encoding='utf-8') as file:
#         data = json.load(file)
#     return data


# file_path = '../../data/metals.json'
# # def read_json_file(file_path):
# #     # with open(file_path, 'r', encoding='utf-8') as file:
# #     # with open('../data/metals.json', 'r', encoding='utf-8') as file:
# #     with open(file_path, 'r', encoding='utf-8') as file:
# #         data = json.load(file)
# #     return data
#
# def read_json_file(file_path):
#     # with open(file_path, 'r', encoding='utf-8') as file:
#     # with open('../data/metals.json', 'r', encoding='utf-8') as file:
#     with open('../../data/metals.json', 'r', encoding='utf-8') as file:
#         data = json.load(file)
#     return data
#
# def allMetalls():
#     # buttons_data = read_json_file('metals.json')
#     buttons_data = read_json_file('../../data/metals.json')
#
#     buttons = [
#         InlineKeyboardButton(text=button['text'], callback_data=button['callback_data'])
#         for button in buttons_data
#     ]
#
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#     keyboard.add(*buttons)
#
#     return keyboard

print(os.getcwd())
# file_path = os.path.abspath('../../data/metals.json')
# file_path = os.path.abspath('m.json')

# def metals(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#     return data
#
#
# def allMetalls():
#     buttons_data = metals(file_path)
#
#     buttons = [
#         InlineKeyboardButton(text=button['text'], callback_data=button['callback_data'])
#         for button in buttons_data
#     ]
#
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#     keyboard.add(*buttons)
#
#     return keyboard

#
# data = [
#     {"text": "Ac", "callback_data": "Actinium"},
#     {"text": "Ag", "callback_data": "Silver"},
# {"text": "Am", "callback_data": "Americium"},
# {"text": "Au", "callback_data": "Gold"},
# {"text": "Be", "callback_data": "Beryllium"},
# {"text": "Bi", "callback_data": "Bismuth"},
# {"text": "Bk", "callback_data": "Berkelium"},
# {"text": "Bo", "callback_data": "Bohrium"},
# {"text": "Cd", "callback_data": "Cadmium"},
# {"text": "Ce", "callback_data": "Cerium"},
# {"text": "Cf", "callback_data": "Californium"},
# {"text": "Co", "callback_data": "Cobalt"},
# {"text": "Cr", "callback_data": "Chromium"},
# {"text": "Cs", "callback_data": "Cesium"},
# {"text": "Cu", "callback_data": "Copper"},
# {"text": "Cm", "callback_data": "Curium"},
# {"text": "Db", "callback_data": "Dubnium"},
# {"text": "Ds", "callback_data": "Darmstadtium"},
# {"text": "Dy", "callback_data": "Dysprosium"},
# {"text": "Es", "callback_data": "Einsteinium"},
# {"text": "Er", "callback_data": "Erbium"},
# {"text": "Eu", "callback_data": "Europium"},
# {"text": "Fm", "callback_data": "Fermium"},
# {"text": "Fr", "callback_data": "Francium"},
# {"text": "Ga", "callback_data": "Gallium"},
# {"text": "Gd", "callback_data": "Gadolinium"},
# {"text": "Ge", "callback_data": "Germanium"},
# {"text": "Hf", "callback_data": "Hafnium"},
# {"text": "Ho", "callback_data": "Holmium"},
# {"text": "Hs", "callback_data": "Hassium"},
# {"text": "In", "callback_data": "Indium"},
# {"text": "Ir", "callback_data": "Iridium"},
# {"text": "La", "callback_data": "Lanthanum"},
# {"text": "Lr", "callback_data": "Lawrencium"},
# {"text": "Lu", "callback_data": "Lutetium"},
# {"text": "Md", "callback_data": "Mendelevium"},
# {"text": "Mn", "callback_data": "Manganese"},
# {"text": "Mo", "callback_data": "Molybdenum"},
# {"text": "Mt", "callback_data": "Meitnerium"},
# {"text": "Nb", "callback_data": "Niobium"},
# {"text": "Nd", "callback_data": "Neodymium"},
# {"text": "Ni", "callback_data": "Nickel"},
# {"text": "Nh", "callback_data": "Nihonium"},
# {"text": "No", "callback_data": "Nobelium"},
# {"text": "Np", "callback_data": "Neptunium"},
# {"text": "Os", "callback_data": "Osmium"},
# {"text": "Pa", "callback_data": "Protactinium"},
# {"text": "Pb", "callback_data": "Lead"},
# {"text": "Pd", "callback_data": "Palladium"},
# {"text": "Pm", "callback_data": "Promethium"},
# {"text": "Po", "callback_data": "Polonium"},
# {"text": "Pr", "callback_data": "Praseodymium"},
# {"text": "Pt", "callback_data": "Platinum"},
# {"text": "Pu", "callback_data": "Plutonium"},
# {"text": "Ra", "callback_data": "Radium"},
# {"text": "Rb", "callback_data": "Rubidium"},
# {"text": "Re", "callback_data": "Rhenium"},
# {"text": "Rf", "callback_data": "Rutherfordium"},
# {"text": "Rh", "callback_data": "Rhodium"},
# {"text": "Ru", "callback_data": "Ruthenium"},
# {"text": "Sb", "callback_data": "Antimony"},
# {"text": "Sc", "callback_data": "Scandium"},
# {"text": "Se", "callback_data": "Selenium"},
# {"text": "Sg", "callback_data": "Seaborgium"},
# {"text": "Si", "callback_data": "Silicon"},
# {"text": "Sm", "callback_data": "Samarium"},
# {"text": "Sn", "callback_data": "Tin"},
# {"text": "Sr", "callback_data": "Strontium"},
# {"text": "Ta", "callback_data": "Tantalum"},
# {"text": "Tb", "callback_data": "Terbium"},
# {"text": "Te", "callback_data": "Tellurium"},
# {"text": "Th", "callback_data": "Thorium"},
# {"text": "Ti", "callback_data": "Titanium"},
# {"text": "Tl", "callback_data": "Thallium"},
# {"text": "Tm", "callback_data": "Thulium"},
# {"text": "U", "callback_data": "Uranium"},
# {"text": "V", "callback_data": "Vanadium"},
# {"text": "W", "callback_data": "Tungsten"},
# {"text": "Y", "callback_data": "Yttrium"},
# {"text": "Yb", "callback_data": "Ytterbium"},
# {"text": "Zn", "callback_data": "Zinc"},
# {"text": "Zr", "callback_data": "Zirconium"}
# ]



# def allMetalls():
#     buttons_data = data
#     buttons = [
#         InlineKeyboardButton(text=button['text'], callback_data=button['callback_data'])
#         for button in buttons_data
#     ]
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#     keyboard.add(*buttons)
#     return keyboard


# def read_json_file():
#     current_dir = os.path.dirname(__file__)
#     file_path = os.path.join(current_dir, '../../data/metals.json')
#
#     with open(file_path, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#
#     return data
#
# def allMetalls():
#     buttons_data = read_json_file()
#
#     # Проверка, что файл имеет ожидаемую структуру
#     if not isinstance(buttons_data, list) or not all(isinstance(item, dict)
#                                                      and 'text' in item and 'callback_data'
#                                                      in item for item in buttons_data):
#         raise ValueError("Неверная структура JSON-файла")
#
#     buttons = [
#         InlineKeyboardButton(text=text, callback_data=callback_data)
#         for metal_data in buttons_data
#         for text, callback_data in zip(metal_data['text'], metal_data['callback_data'])
#     ]
#
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#     keyboard.add(*buttons)
#
#     return keyboard





# def allMetalls():
#     buttons = [
#         InlineKeyboardButton(text='Ac', callback_data='Actinium'),
#         InlineKeyboardButton(text='Ag', callback_data='Silver'),
#         InlineKeyboardButton(text='Am', callback_data='Americium'),
#         InlineKeyboardButton(text='Au', callback_data='Gold'),
#         InlineKeyboardButton(text='Be', callback_data='Beryllium'),
#         InlineKeyboardButton(text='Bi', callback_data='Bismuth'),
#         InlineKeyboardButton(text='Bk', callback_data='Berkelium'),
#         InlineKeyboardButton(text='Bo', callback_data='Bohrium'),
#         InlineKeyboardButton(text='Cd', callback_data='Cadmium'),
#         InlineKeyboardButton(text='Ce', callback_data='Cerium'),
#         InlineKeyboardButton(text='Cf', callback_data='Californium'),
#         InlineKeyboardButton(text='Co', callback_data='Cobalt'),
#         InlineKeyboardButton(text='Cr', callback_data='Chromium'),
#         InlineKeyboardButton(text='Cs', callback_data='Cesium'),
#         InlineKeyboardButton(text='Cu', callback_data='Copper'),
#         InlineKeyboardButton(text='Cm', callback_data='Curium'),
#         InlineKeyboardButton(text='Db', callback_data='Dubnium'),
#         InlineKeyboardButton(text='Ds', callback_data='Darmstadtium'),
#         InlineKeyboardButton(text='Dy', callback_data='Dysprosium'),
#         InlineKeyboardButton(text='Es', callback_data='Einsteinium'),
#         InlineKeyboardButton(text='Er', callback_data='Erbium'),
#         InlineKeyboardButton(text='Eu', callback_data='Europium'),
#         InlineKeyboardButton(text='Fm', callback_data='Fermium'),
#         InlineKeyboardButton(text='Fr', callback_data='Francium'),
#         InlineKeyboardButton(text='Ga', callback_data='Gallium'),
#         InlineKeyboardButton(text='Gd', callback_data='Gadolinium'),
#         InlineKeyboardButton(text='Ge', callback_data='Germanium'),
#         InlineKeyboardButton(text='Hf', callback_data='Hafnium'),
#         InlineKeyboardButton(text='Ho', callback_data='Holmium'),
#         InlineKeyboardButton(text='Hs', callback_data='Hassium'),
#         InlineKeyboardButton(text='In', callback_data='Indium'),
#         InlineKeyboardButton(text='Ir', callback_data='Iridium'),
#         InlineKeyboardButton(text='La', callback_data='Lanthanum'),
#         InlineKeyboardButton(text='Lr', callback_data='Lawrencium'),
#         InlineKeyboardButton(text='Lu', callback_data='Lutetium'),
#         InlineKeyboardButton(text='Md', callback_data='Mendelevium'),
#         InlineKeyboardButton(text='Mn', callback_data='Manganese'),
#         InlineKeyboardButton(text='Mo', callback_data='Molybdenum'),
#         InlineKeyboardButton(text='Mt', callback_data='Meitnerium'),
#         InlineKeyboardButton(text='Nb', callback_data='Niobium'),
#         InlineKeyboardButton(text='Nd', callback_data='Neodymium'),
#         InlineKeyboardButton(text='Ni', callback_data='Nickel'),
#         InlineKeyboardButton(text='Nh', callback_data='Nihonium'),
#         InlineKeyboardButton(text='No', callback_data='Nobelium'),
#         InlineKeyboardButton(text='Np', callback_data='Neptunium'),
#         InlineKeyboardButton(text='Os', callback_data='Osmium'),
#         InlineKeyboardButton(text='Pa', callback_data='Protactinium'),
#         InlineKeyboardButton(text='Pb', callback_data='Lead'),
#         InlineKeyboardButton(text='Pd', callback_data='Palladium'),
#         InlineKeyboardButton(text='Pm', callback_data='Promethium'),
#         InlineKeyboardButton(text='Po', callback_data='Polonium'),
#         InlineKeyboardButton(text='Pr', callback_data='Praseodymium'),
#         InlineKeyboardButton(text='Pt', callback_data='Platinum'),
#         InlineKeyboardButton(text='Pu', callback_data='Plutonium'),
#         InlineKeyboardButton(text='Ra', callback_data='Radium'),
#         InlineKeyboardButton(text='Rb', callback_data='Rubidium'),
#         InlineKeyboardButton(text='Re', callback_data='Rhenium'),
#         InlineKeyboardButton(text='Rf', callback_data='Rutherfordium'),
#         InlineKeyboardButton(text='Rh', callback_data='Rhodium'),
#         InlineKeyboardButton(text='Ru', callback_data='Ruthenium'),
#         InlineKeyboardButton(text='Sb', callback_data='Antimony'),
#         InlineKeyboardButton(text='Sc', callback_data='Scandium'),
#         InlineKeyboardButton(text='Se', callback_data='Selenium'),
#         InlineKeyboardButton(text='Sg', callback_data='Seaborgium'),
#         InlineKeyboardButton(text='Si', callback_data='Silicon'),
#         InlineKeyboardButton(text='Sm', callback_data='Samarium'),
#         InlineKeyboardButton(text='Sn', callback_data='Tin'),
#         InlineKeyboardButton(text='Sr', callback_data='Strontium'),
#         InlineKeyboardButton(text='Ta', callback_data='Tantalum'),
#         InlineKeyboardButton(text='Tb', callback_data='Terbium'),
#         InlineKeyboardButton(text='Te', callback_data='Tellurium'),
#         InlineKeyboardButton(text='Th', callback_data='Thorium'),
#         InlineKeyboardButton(text='Ti', callback_data='Titanium'),
#         InlineKeyboardButton(text='Tl', callback_data='Thallium'),
#         InlineKeyboardButton(text='Tm', callback_data='Thulium'),
#         InlineKeyboardButton(text='U', callback_data='Uranium'),
#         InlineKeyboardButton(text='V', callback_data='Vanadium'),
#         InlineKeyboardButton(text='W', callback_data='Tungsten'),
#         InlineKeyboardButton(text='Y', callback_data='Yttrium'),
#         InlineKeyboardButton(text='Yb', callback_data='Ytterbium'),
#         InlineKeyboardButton(text='Zn', callback_data='Zinc'),
#         InlineKeyboardButton(text='Zr', callback_data='Zirconium')
#     ]
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
#     keyboard.add(*buttons)
#
#     return keyboard


# def allMetalls():
#     # Button1 = InlineKeyboardButton(text='Ac', callback_data='Actinium', tooltip="Tooltip for Button 1")
#     Button1 = InlineKeyboardButton(text='Ac', callback_data='Actinium')
#     Button2 = InlineKeyboardButton(text='Ag', callback_data='Silver')
#     Button3 = InlineKeyboardButton(text='Am', callback_data='Americium')
#     Button4 = InlineKeyboardButton(text='Au', callback_data='Gold')
#     Button5 = InlineKeyboardButton(text='Be', callback_data='Beryllium')
#     Button6 = InlineKeyboardButton(text='Bi', callback_data='Bismuth')
#     Button7 = InlineKeyboardButton(text='Bk', callback_data='Berkelium')
#     Button8 = InlineKeyboardButton(text='Bo', callback_data='Bohrium')
#     Button9 = InlineKeyboardButton(text='Cd', callback_data='Cadmium')
#     Button10 = InlineKeyboardButton(text='Ce', callback_data='Cerium')
#     Button11 = InlineKeyboardButton(text='Cf', callback_data='Californium')
#     Button12 = InlineKeyboardButton(text='Co', callback_data='Cobalt')
#     Button13 = InlineKeyboardButton(text='Cr', callback_data='Chromium')
#     Button14 = InlineKeyboardButton(text='Cs', callback_data='Cesium')
#     Button15 = InlineKeyboardButton(text='Cu', callback_data='Copper')
#     Button16 = InlineKeyboardButton(text='Cm', callback_data='Curium')
#     Button17 = InlineKeyboardButton(text='Db', callback_data='Dubnium')
#     Button18 = InlineKeyboardButton(text='Ds', callback_data='Darmstadtium')
#     Button19 = InlineKeyboardButton(text='Dy', callback_data='Dysprosium')
#     Button20 = InlineKeyboardButton(text='Es', callback_data='Einsteinium')
#     Button21 = InlineKeyboardButton(text='Er', callback_data='Erbium')
#     Button22 = InlineKeyboardButton(text='Eu', callback_data='Europium')
#     Button23 = InlineKeyboardButton(text='Fm', callback_data='Fermium')
#     Button24 = InlineKeyboardButton(text='Fr', callback_data='Francium')
#     Button25 = InlineKeyboardButton(text='Ga', callback_data='Gallium')
#     Button26 = InlineKeyboardButton(text='Gd', callback_data='Gadolinium')
#     Button27 = InlineKeyboardButton(text='Ge', callback_data='Germanium')
#     Button28 = InlineKeyboardButton(text='Hf', callback_data='Hafnium')
#     Button29 = InlineKeyboardButton(text='Ho', callback_data='Holmium')
#     Button30 = InlineKeyboardButton(text='Hs', callback_data='Hassium')
#     Button31 = InlineKeyboardButton(text='In', callback_data='Indium')
#     Button32 = InlineKeyboardButton(text='Ir', callback_data='Iridium')
#     Button33 = InlineKeyboardButton(text='La', callback_data='Lanthanum')
#     Button34 = InlineKeyboardButton(text='Lr', callback_data='Lawrencium')
#     Button35 = InlineKeyboardButton(text='Lu', callback_data='Lutetium')
#     Button36 = InlineKeyboardButton(text='Md', callback_data='Mendelevium')
#     Button37 = InlineKeyboardButton(text='Mn', callback_data='Manganese')
#     Button38 = InlineKeyboardButton(text='Mo', callback_data='Molybdenum')
#     Button39 = InlineKeyboardButton(text='Mt', callback_data='Meitnerium')
#     Button40 = InlineKeyboardButton(text='Nb', callback_data='Niobium')
#     Button41 = InlineKeyboardButton(text='Nd', callback_data='Neodymium')
#     Button42 = InlineKeyboardButton(text='Ni', callback_data='Nickel')
#     Button43 = InlineKeyboardButton(text='Nh', callback_data='Nihonium')
#     Button44 = InlineKeyboardButton(text='No', callback_data='Nobelium')
#     Button45 = InlineKeyboardButton(text='Np', callback_data='Neptunium')
#     Button46 = InlineKeyboardButton(text='Os', callback_data='Osmium')
#     Button47 = InlineKeyboardButton(text='Pa', callback_data='Protactinium')
#     Button48 = InlineKeyboardButton(text='Pb', callback_data='Lead')
#     Button49 = InlineKeyboardButton(text='Pd', callback_data='Palladium')
#     Button50 = InlineKeyboardButton(text='Pm', callback_data='Promethium')
#     Button51 = InlineKeyboardButton(text='Po', callback_data='Polonium')
#     Button52 = InlineKeyboardButton(text='Pr', callback_data='Praseodymium')
#     Button53 = InlineKeyboardButton(text='Pt', callback_data='Platinum')
#     Button54 = InlineKeyboardButton(text='Pu', callback_data='Plutonium')
#     Button55 = InlineKeyboardButton(text='Ra', callback_data='Radium')
#     Button56 = InlineKeyboardButton(text='Rb', callback_data='Rubidium')
#     Button57 = InlineKeyboardButton(text='Re', callback_data='Rhenium')
#     Button58 = InlineKeyboardButton(text='Rf', callback_data='Rutherfordium')
#     Button59 = InlineKeyboardButton(text='Rh', callback_data='Rhodium')
#     Button60 = InlineKeyboardButton(text='Ru', callback_data='Ruthenium')
#     Button61 = InlineKeyboardButton(text='Sb', callback_data='Antimony')
#     Button62 = InlineKeyboardButton(text='Sc', callback_data='Scandium')
#     Button63 = InlineKeyboardButton(text='Se', callback_data='Selenium')
#     Button64 = InlineKeyboardButton(text='Sg', callback_data='Seaborgium')
#     Button65 = InlineKeyboardButton(text='Si', callback_data='Silicon')
#     Button66 = InlineKeyboardButton(text='Sm', callback_data='Samarium')
#     Button67 = InlineKeyboardButton(text='Sn', callback_data='Tin')
#     Button68 = InlineKeyboardButton(text='Sr', callback_data='Strontium')
#     Button69 = InlineKeyboardButton(text='Ta', callback_data='Tantalum')
#     Button70 = InlineKeyboardButton(text='Tb', callback_data='Terbium')
#     Button71 = InlineKeyboardButton(text='Te', callback_data='Tellurium')
#     Button72 = InlineKeyboardButton(text='Th', callback_data='Thorium')
#     Button73 = InlineKeyboardButton(text='Ti', callback_data='Titanium')
#     Button74 = InlineKeyboardButton(text='Tl', callback_data='Thallium')
#     Button75 = InlineKeyboardButton(text='Tm', callback_data='Tullium')
#     Button76 = InlineKeyboardButton(text='U', callback_data='Uranium')
#     Button77 = InlineKeyboardButton(text='V', callback_data='Vanadium')
#     Button78 = InlineKeyboardButton(text='W', callback_data='Tungsten')
#     Button79 = InlineKeyboardButton(text='Y', callback_data='Yttrium')
#     Button80 = InlineKeyboardButton(text='Yb', callback_data='Ytterbium')
#     Button81 = InlineKeyboardButton(text='Zn', callback_data='Zinc')
#     Button82 = InlineKeyboardButton(text='Zr', callback_data='Zirconium')
#     Keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=6).add(Button1, Button2, Button3,
#                                                                            Button4, Button5, Button6, Button7,
#                                                                            Button8, Button9, Button10, Button11,
#                                                                            Button12, Button13, Button14,
#                                                                            Button15, Button16, Button17, Button18,
#                                                                            Button19, Button20, Button21,
#                                                                            Button22, Button23, Button24, Button25,
#                                                                            Button26, Button27, Button28,
#                                                                            Button29, Button30, Button31, Button32,
#                                                                            Button33, Button34, Button35,
#                                                                            Button36, Button37, Button38, Button39,
#                                                                            Button40, Button41, Button42,
#                                                                            Button43, Button44, Button45, Button46,
#                                                                            Button47, Button48, Button49,
#                                                                            Button50, Button51, Button52, Button53,
#                                                                            Button54, Button55, Button56,
#                                                                            Button57, Button58, Button59, Button60,
#                                                                            Button61, Button62, Button63,
#                                                                            Button64, Button65, Button66, Button67,
#                                                                            Button68, Button69, Button70,
#                                                                            Button71, Button72, Button73, Button74,
#                                                                            Button75, Button76, Button77,
#                                                                            Button78, Button79, Button80, Button81,
#                                                                            Button82)
#     return Keyboard

# keyboard = [
#        [InlineKeyboardButton("Button 1", callback_data='1', tooltip="Tooltip for Button 1")],
#        [InlineKeyboardButton("Button 2", callback_data='2', tooltip="Tooltip for Button 2")],
#    ]

# def allMetalls():
#     Button1 = InlineKeyboardButton(text='Ac', callback_data='Actinium')
#     Button2 = InlineKeyboardButton(text='Ag', callback_data='Silver')
#     Button3 = InlineKeyboardButton(text='Am', callback_data='Americium')
#     Button4 = InlineKeyboardButton(text='Au', callback_data='Gold')
#     Button5 = InlineKeyboardButton(text='Be', callback_data='Beryllium')
#     Button6 = InlineKeyboardButton(text='Bi', callback_data='Bismuth')
#     Button7 = InlineKeyboardButton(text='Bk', callback_data='Berkelium')
#     Button8 = InlineKeyboardButton(text='Bo', callback_data='Bohrium')
#     Button9 = InlineKeyboardButton(text='Cd', callback_data='Cadmium')
#     Button10 = InlineKeyboardButton(text='Ce', callback_data='Cerium')
#     Button11 = InlineKeyboardButton(text='Cf', callback_data='Californium')
#     Button12 = InlineKeyboardButton(text='Co', callback_data='Cobalt')
#     Button13 = InlineKeyboardButton(text='Cr', callback_data='Chromium')
#     Button14 = InlineKeyboardButton(text='Cs', callback_data='Cesium')
#     Button15 = InlineKeyboardButton(text='Cu', callback_data='Copper')
#     Button16 = InlineKeyboardButton(text='Cm', callback_data='Curium')
#     Button17 = InlineKeyboardButton(text='Db', callback_data='Dubnium Db')
#     Button18 = InlineKeyboardButton(text='Ds', callback_data='Darmstadtium')
#     Button19 = InlineKeyboardButton(text='Dy', callback_data='Dysprosium')
#     Button20 = InlineKeyboardButton(text='Es', callback_data='Einsteinium')
#     Button21 = InlineKeyboardButton(text='Er', callback_data='Erbium')
#     Button22 = InlineKeyboardButton(text='Eu', callback_data='Europium')
#     Button23 = InlineKeyboardButton(text='Fm', callback_data='Fermium')
#     Button24 = InlineKeyboardButton(text='Fr', callback_data='Francium')
#     Button25 = InlineKeyboardButton(text='Ga', callback_data='Gallium')
#     Button26 = InlineKeyboardButton(text='Gd', callback_data='Gadolinium')
#     Button27 = InlineKeyboardButton(text='Ge', callback_data='Germanium')
#     Button28 = InlineKeyboardButton(text='Hf', callback_data='Hafnium')
#     Button29 = InlineKeyboardButton(text='Ho', callback_data='Holmium')
#     Button30 = InlineKeyboardButton(text='Hs', callback_data='Hassium')
#     Button31 = InlineKeyboardButton(text='In', callback_data='Indium')
#     Button32 = InlineKeyboardButton(text='Ir', callback_data='Iridium')
#     Button33 = InlineKeyboardButton(text='La', callback_data='Lanthanum')
#     Button34 = InlineKeyboardButton(text='Lr', callback_data='Lawrencium')
#     Button35 = InlineKeyboardButton(text='Lu', callback_data='Lutetium')
#     Button36 = InlineKeyboardButton(text='Md', callback_data='Mendelevium')
#     Button37 = InlineKeyboardButton(text='Mn', callback_data='Manganese')
#     Button38 = InlineKeyboardButton(text='Mo', callback_data='Molybdenum')
#     Button39 = InlineKeyboardButton(text='Mt', callback_data='Meitnerium')
#     Button40 = InlineKeyboardButton(text='Nb', callback_data='Niobium')
#     Button41 = InlineKeyboardButton(text='Nd', callback_data='Neodymium')
#     Button42 = InlineKeyboardButton(text='Ni', callback_data='Nickel')
#     Button43 = InlineKeyboardButton(text='No', callback_data='Nobelium')
#     Button44 = InlineKeyboardButton(text='Np', callback_data='Neptunium')
#     Button45 = InlineKeyboardButton(text='Os', callback_data='Osmium')
#     Button46 = InlineKeyboardButton(text='Pa', callback_data='Protactinium')
#     Button47 = InlineKeyboardButton(text='Pb', callback_data='Lead')
#     Button48 = InlineKeyboardButton(text='Pd', callback_data='Palladium')
#     Button49 = InlineKeyboardButton(text='Pm', callback_data='Promethium')
#     Button50 = InlineKeyboardButton(text='Po', callback_data='Polonium')
#     Button51 = InlineKeyboardButton(text='Pr', callback_data='Praseodymium')
#     Button52 = InlineKeyboardButton(text='Pt', callback_data='Platinum')
#     Button53 = InlineKeyboardButton(text='Pu', callback_data='Plutonium')
#     Button54 = InlineKeyboardButton(text='Ra', callback_data='Radium')
#     Button55 = InlineKeyboardButton(text='Rb', callback_data='Rubidium')
#     Button56 = InlineKeyboardButton(text='Re', callback_data='Rhenium')
#     Button57 = InlineKeyboardButton(text='Rf', callback_data='Rutherfordium')
#     Button58 = InlineKeyboardButton(text='Rh', callback_data='Rhodium')
#     Button59 = InlineKeyboardButton(text='Ru', callback_data='Ruthenium')
#     Button60 = InlineKeyboardButton(text='Sb', callback_data='Antimony')
#     Button61 = InlineKeyboardButton(text='Sc', callback_data='Scandium')
#     Button62 = InlineKeyboardButton(text='Se', callback_data='Selenium')
#     Button63 = InlineKeyboardButton(text='Sg', callback_data='Seaborgium')
#     Button64 = InlineKeyboardButton(text='Si', callback_data='Silicon')
#     Button65 = InlineKeyboardButton(text='Sm', callback_data='Samarium')
#     Button66 = InlineKeyboardButton(text='Sn', callback_data='Tin')
#     Button67 = InlineKeyboardButton(text='Sr', callback_data='Strontium')
#     Button68 = InlineKeyboardButton(text='Ta', callback_data='Tantalum')
#     Button69 = InlineKeyboardButton(text='Tb', callback_data='Terbium')
#     Button70 = InlineKeyboardButton(text='Te', callback_data='Tellurium')
#     Button71 = InlineKeyboardButton(text='Th', callback_data='Thorium')
#     Button72 = InlineKeyboardButton(text='Ti', callback_data='Titanium')
#     Button73 = InlineKeyboardButton(text='Tl', callback_data='Thallium')
#     Button74 = InlineKeyboardButton(text='Tm', callback_data='Tullium')
#     Button75 = InlineKeyboardButton(text='U', callback_data='Uranium')
#     Button76 = InlineKeyboardButton(text='V', callback_data='Vanadium')
#     Button77 = InlineKeyboardButton(text='W', callback_data='Tungsten')
#     Button78 = InlineKeyboardButton(text='Y', callback_data='Yttrium')
#     Button79 = InlineKeyboardButton(text='Yb', callback_data='Ytterbium')
#     Button80 = InlineKeyboardButton(text='Zn', callback_data='Zinc')
#     Button81 = InlineKeyboardButton(text='Zr', callback_data='Zirconium')
#     Keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=6).add(Button1, Button2, Button3,
#                                           Button4, Button5, Button6, Button7,
#                                           Button8, Button9, Button10, Button11, Button12, Button13, Button14,
#                                           Button15, Button16, Button17, Button18, Button19, Button20, Button21,
#                                           Button22, Button23, Button24, Button25, Button26, Button27, Button28,
#                                           Button29, Button30, Button31, Button32, Button33, Button34, Button35,
#                                           Button36, Button37, Button38, Button39, Button40, Button41, Button42,
#                                           Button43, Button44, Button45, Button46, Button47, Button48, Button49,
#                                           Button50, Button51, Button52, Button53, Button54, Button55, Button56,
#                                           Button57, Button58, Button59, Button60, Button61, Button62, Button63,
#                                           Button64, Button65, Button66, Button67, Button68, Button69, Button70,
#                                           Button71, Button72, Button73, Button74, Button75, Button76, Button77,
#                                           Button78, Button79, Button80, Button81)
#     return Keyboard
# Меню клавиатуры стандартного калькулятора
def calculator():
    Button1 = InlineKeyboardButton(text=str('C'), callback_data=str('C'))
    Button2 = InlineKeyboardButton(text=str('<='), callback_data=str('<='))
    Button3 = InlineKeyboardButton(text=str('+'), callback_data=str('+'))
    Button4 = InlineKeyboardButton(text=str('9'), callback_data=str('9'))
    Button5 = InlineKeyboardButton(text=str('8'), callback_data=str('8'))
    Button6 = InlineKeyboardButton(text=str('-'), callback_data=str('-'))
    Button7 = InlineKeyboardButton(text=str('7'), callback_data=str('7'))
    Button8 = InlineKeyboardButton(text=str('6'), callback_data=str('6'))
    Button9 = InlineKeyboardButton(text=str('x'), callback_data=str('*'))
    Button10 = InlineKeyboardButton(text=str('5'), callback_data=str('5'))
    Button11 = InlineKeyboardButton(text=str('4'), callback_data=str('4'))
    Button12 = InlineKeyboardButton(text=str('/'), callback_data=str('/'))
    Button13 = InlineKeyboardButton(text=str('3'), callback_data=str('3'))
    Button14 = InlineKeyboardButton(text=str('2'), callback_data=str('2'))
    Button15 = InlineKeyboardButton(text=str('.'), callback_data=str('.'))
    Button16 = InlineKeyboardButton(text=str('1'), callback_data=str('1'))
    Button17 = InlineKeyboardButton(text=str('0'), callback_data=str('0'))
    Button18 = InlineKeyboardButton(text=str('='), callback_data=str('='))
    Button19 = InlineKeyboardButton('  Hide keyboard   ', callback_data='Hide keyboard')
    Button20 = InlineKeyboardButton(' ', callback_data=' ')
    Keyboard = InlineKeyboardMarkup().add(Button1,
                                          Button2, Button3, Button4, Button5, Button6, Button7,
                                          Button8, Button9, Button10, Button11, Button12, Button13,
                                          Button14, Button15, Button16, Button17,
                                          Button18, Button19, Button20)
    return Keyboard


# Меню клавиатуры для круглой трубы:
def pipeRound():
    a = 'Ø - clear all, S - wall thickness, mm., L - length, m.'
    Button1 = InlineKeyboardButton(text=str('Ø'), callback_data=str('C'))
    Button2 = InlineKeyboardButton('Annotation', callback_data=str(a))
    Button3 = InlineKeyboardButton(text=str('<='), callback_data=str('<='))
    Button4 = InlineKeyboardButton(text=str('9'), callback_data=str('9'))
    Button5 = InlineKeyboardButton(text=str('8'), callback_data=str('8'))
    Button6 = InlineKeyboardButton(text=str('L'), callback_data=str('*'))
    Button7 = InlineKeyboardButton(text=str('7'), callback_data=str('7'))
    Button8 = InlineKeyboardButton(text=str('6'), callback_data=str('6'))
    Button9 = InlineKeyboardButton(text=str('S'), callback_data=str('*'))
    Button10 = InlineKeyboardButton(text=str('5'), callback_data=str('5'))
    Button11 = InlineKeyboardButton(text=str('4'), callback_data=str('4'))
    Button12 = InlineKeyboardButton(text=str(','), callback_data=str('.'))
    Button13 = InlineKeyboardButton(text=str('3'), callback_data=str('3'))
    Button14 = InlineKeyboardButton(text=str('2'), callback_data=str('2'))
    Button15 = InlineKeyboardButton(text=str('='), callback_data=str('='))
    Button16 = InlineKeyboardButton(text=str('1'), callback_data=str('1'))
    Button17 = InlineKeyboardButton(text=str('0'), callback_data=str('0'))
    Button18 = InlineKeyboardButton('All results', callback_data='All results')
    Button19 = InlineKeyboardButton('Hide keyboard', callback_data='Hide keyboard')
    Keyboard = InlineKeyboardMarkup().add(Button1,
                                          Button2, Button3, Button4, Button5, Button6, Button7,
                                          Button8, Button9, Button10, Button11, Button12,
                                          Button13, Button14, Button15, Button16, Button17, Button18, Button19)
    return Keyboard


# Меню клавиатуры для кругов и колец:
def roundCircle():
    a = 'Ø - clear all, D - internal diameter, mm., L - length, m.'
    Button1 = InlineKeyboardButton(text=str('Ø'), callback_data=str('C'))
    Button2 = InlineKeyboardButton('Annotation', callback_data=str(a))
    Button3 = InlineKeyboardButton(text=str('<='), callback_data=str('<='))
    Button4 = InlineKeyboardButton(text=str('9'), callback_data=str('9'))
    Button5 = InlineKeyboardButton(text=str('8'), callback_data=str('8'))
    Button6 = InlineKeyboardButton(text=str('L'), callback_data=str('*'))
    Button7 = InlineKeyboardButton(text=str('7'), callback_data=str('7'))
    Button8 = InlineKeyboardButton(text=str('6'), callback_data=str('6'))
    Button9 = InlineKeyboardButton(text=str('D'), callback_data=str('*'))
    Button10 = InlineKeyboardButton(text=str('5'), callback_data=str('5'))
    Button11 = InlineKeyboardButton(text=str('4'), callback_data=str('4'))
    Button12 = InlineKeyboardButton(text=str(','), callback_data=str('.'))
    Button13 = InlineKeyboardButton(text=str('3'), callback_data=str('3'))
    Button14 = InlineKeyboardButton(text=str('2'), callback_data=str('2'))
    Button15 = InlineKeyboardButton(text=str('='), callback_data=str('='))
    Button16 = InlineKeyboardButton(text=str('1'), callback_data=str('1'))
    Button17 = InlineKeyboardButton(text=str('0'), callback_data=str('0'))
    Button18 = InlineKeyboardButton('All results', callback_data='All results')
    Button19 = InlineKeyboardButton('Hide keyboard', callback_data='Hide keyboard')
    Keyboard = InlineKeyboardMarkup().add(Button1,
                                          Button2, Button3, Button4, Button5, Button6, Button7,
                                          Button8, Button9, Button10, Button11, Button12,
                                          Button13, Button14, Button15, Button16, Button17,
                                          Button18, Button19)
    return Keyboard


# Меню клавиатуры для профильной трубы:
def pipeProfile():
    a = 'S - wall thickness, mm., H - height, mm., L - length, m.'
    Button1 = InlineKeyboardButton(text=str('□'), callback_data=str('C'))
    Button2 = InlineKeyboardButton('Annotation', callback_data=str(a))
    Button3 = InlineKeyboardButton(text=str('<='), callback_data=str('<='))
    Button4 = InlineKeyboardButton(text=str('9'), callback_data=str('9'))
    Button5 = InlineKeyboardButton(text=str('8'), callback_data=str('8'))
    Button6 = InlineKeyboardButton(text=str('L'), callback_data=str('*'))
    Button7 = InlineKeyboardButton(text=str('7'), callback_data=str('7'))
    Button8 = InlineKeyboardButton(text=str('6'), callback_data=str('6'))
    Button9 = InlineKeyboardButton(text=str('H'), callback_data=str('*'))
    Button10 = InlineKeyboardButton(text=str('5'), callback_data=str('5'))
    Button11 = InlineKeyboardButton(text=str('4'), callback_data=str('4'))
    Button12 = InlineKeyboardButton(text=str('S'), callback_data=str('*'))
    Button13 = InlineKeyboardButton(text=str('3'), callback_data=str('3'))
    Button14 = InlineKeyboardButton(text=str('2'), callback_data=str('2'))
    Button15 = InlineKeyboardButton(text=str(','), callback_data=str('.'))
    Button16 = InlineKeyboardButton(text=str('1'), callback_data=str('1'))
    Button17 = InlineKeyboardButton(text=str('0'), callback_data=str('0'))
    Button18 = InlineKeyboardButton(text=str('='), callback_data=str('='))
    Button19 = InlineKeyboardButton('All results', callback_data='All results')
    Button20 = InlineKeyboardButton('Hide keyboard', callback_data='Hide keyboard')
    Keyboard = InlineKeyboardMarkup().add(Button1,
                                          Button2, Button3, Button4, Button5, Button6, Button7,
                                          Button8, Button9, Button10, Button11, Button12, Button13,
                                          Button14, Button15, Button16, Button17, Button18, Button19,
                                          Button20)
    return Keyboard


# Меню клавиатуры для расчета квадрата, прямоугольника, листа и полосы
def square():
    a = 'S - wall thickness, mm., H - height, mm., L - length, m.'
    Button1 = InlineKeyboardButton(text=str('■'), callback_data=str('C'))
    Button2 = InlineKeyboardButton('Annotation', callback_data=str(a))
    Button3 = InlineKeyboardButton(text=str('<='), callback_data=str('<='))
    Button4 = InlineKeyboardButton(text=str('9'), callback_data=str('9'))
    Button5 = InlineKeyboardButton(text=str('8'), callback_data=str('8'))
    Button6 = InlineKeyboardButton(text=str('L'), callback_data=str('*'))
    Button7 = InlineKeyboardButton(text=str('7'), callback_data=str('7'))
    Button8 = InlineKeyboardButton(text=str('6'), callback_data=str('6'))
    Button9 = InlineKeyboardButton(text=str('H'), callback_data=str('*'))
    Button10 = InlineKeyboardButton(text=str('5'), callback_data=str('5'))
    Button11 = InlineKeyboardButton(text=str('4'), callback_data=str('4'))
    Button12 = InlineKeyboardButton(text=str('S'), callback_data=str('*'))
    Button13 = InlineKeyboardButton(text=str('3'), callback_data=str('3'))
    Button14 = InlineKeyboardButton(text=str('2'), callback_data=str('2'))
    Button15 = InlineKeyboardButton(text=str(','), callback_data=str('.'))
    Button16 = InlineKeyboardButton(text=str('1'), callback_data=str('1'))
    Button17 = InlineKeyboardButton(text=str('0'), callback_data=str('0'))
    Button18 = InlineKeyboardButton(text=str('='), callback_data=str('='))
    Button19 = InlineKeyboardButton('All results', callback_data='All results')
    Button20 = InlineKeyboardButton('Hide keyboard', callback_data='Hide keyboard')
    Keyboard = InlineKeyboardMarkup().add(Button1,
                                          Button2, Button3, Button4, Button5, Button6, Button7,
                                          Button8, Button9, Button10, Button11, Button12, Button13,
                                          Button14, Button15, Button16, Button17, Button18, Button19,
                                          Button20)
    return Keyboard


# Меню клавиатуры для расчета листового материала
def flat():
    a = 'S - wall thickness, mm., H - height, mm., L - length, m.'
    Button1 = InlineKeyboardButton(text=str('▬'), callback_data=str('C'))
    Button2 = InlineKeyboardButton('Annotation', callback_data=str(a))
    Button3 = InlineKeyboardButton(text=str('<='), callback_data=str('<='))
    Button4 = InlineKeyboardButton(text=str('9'), callback_data=str('9'))
    Button5 = InlineKeyboardButton(text=str('8'), callback_data=str('8'))
    Button6 = InlineKeyboardButton(text=str('L'), callback_data=str('*'))
    Button7 = InlineKeyboardButton(text=str('7'), callback_data=str('7'))
    Button8 = InlineKeyboardButton(text=str('6'), callback_data=str('6'))
    Button9 = InlineKeyboardButton(text=str('H'), callback_data=str('*'))
    Button10 = InlineKeyboardButton(text=str('5'), callback_data=str('5'))
    Button11 = InlineKeyboardButton(text=str('4'), callback_data=str('4'))
    Button12 = InlineKeyboardButton(text=str('S'), callback_data=str('*'))
    Button13 = InlineKeyboardButton(text=str('3'), callback_data=str('3'))
    Button14 = InlineKeyboardButton(text=str('2'), callback_data=str('2'))
    Button15 = InlineKeyboardButton(text=str(','), callback_data=str('.'))
    Button16 = InlineKeyboardButton(text=str('1'), callback_data=str('1'))
    Button17 = InlineKeyboardButton(text=str('0'), callback_data=str('0'))
    Button18 = InlineKeyboardButton(text=str('='), callback_data=str('='))
    Button19 = InlineKeyboardButton('All results', callback_data='All results')
    Button20 = InlineKeyboardButton('Hide keyboard', callback_data='Hide keyboard')
    Keyboard = InlineKeyboardMarkup().add(Button1,
                                          Button2, Button3, Button4, Button5, Button6, Button7,
                                          Button8, Button9, Button10, Button11, Button12, Button13,
                                          Button14, Button15, Button16, Button17, Button18, Button19,
                                          Button20)
    return Keyboard


# Меню клавиатуры для расчета балки
def beam():
    a = 'H-height,mm, B-width,mm, S-thickness,mm, Т-shelf thickness,mm'
    Button1 = InlineKeyboardButton(text=str('H'), callback_data=str('H'))
    Button2 = InlineKeyboardButton('Annotation', callback_data=str(a))
    Button3 = InlineKeyboardButton(text=str('<='), callback_data=str('<='))
    Button4 = InlineKeyboardButton(text=str('9'), callback_data=str('9'))
    Button5 = InlineKeyboardButton(text=str('8'), callback_data=str('8'))
    Button6 = InlineKeyboardButton(text=str('B'), callback_data=str('*'))
    Button7 = InlineKeyboardButton(text=str('7'), callback_data=str('7'))
    Button8 = InlineKeyboardButton(text=str('6'), callback_data=str('6'))
    Button9 = InlineKeyboardButton(text=str('T'), callback_data=str('*'))
    Button10 = InlineKeyboardButton(text=str('5'), callback_data=str('5'))
    Button11 = InlineKeyboardButton(text=str('4'), callback_data=str('4'))
    Button12 = InlineKeyboardButton(text=str('S'), callback_data=str('*'))
    Button13 = InlineKeyboardButton(text=str('3'), callback_data=str('3'))
    Button14 = InlineKeyboardButton(text=str('2'), callback_data=str('2'))
    Button15 = InlineKeyboardButton(text=str(','), callback_data=str('.'))
    Button16 = InlineKeyboardButton(text=str('1'), callback_data=str('1'))
    Button17 = InlineKeyboardButton(text=str('0'), callback_data=str('0'))
    Button18 = InlineKeyboardButton(text=str('='), callback_data=str('='))
    Button19 = InlineKeyboardButton('All results', callback_data='All results')
    Button20 = InlineKeyboardButton('Hide keyboard', callback_data='Hide keyboard')
    Keyboard = InlineKeyboardMarkup().add(Button1,
                                          Button2, Button3, Button4, Button5, Button6, Button7,
                                          Button8, Button9, Button10, Button11, Button12, Button13,
                                          Button14, Button15, Button16, Button17, Button18, Button19,
                                          Button20)
    return Keyboard


# Меню клавиатуры для расчета уголка
def corner():
    a = 'H-height,mm, B-width,mm, S-thickness,mm, L-length,mm'
    Button1 = InlineKeyboardButton(text=str('H'), callback_data=str('H'))
    Button2 = InlineKeyboardButton('Annotation', callback_data=str(a))
    Button3 = InlineKeyboardButton(text=str('<='), callback_data=str('<='))
    Button4 = InlineKeyboardButton(text=str('9'), callback_data=str('9'))
    Button5 = InlineKeyboardButton(text=str('8'), callback_data=str('8'))
    Button6 = InlineKeyboardButton(text=str('L'), callback_data=str('*'))
    Button7 = InlineKeyboardButton(text=str('7'), callback_data=str('7'))
    Button8 = InlineKeyboardButton(text=str('6'), callback_data=str('6'))
    Button9 = InlineKeyboardButton(text=str('B'), callback_data=str('*'))
    Button10 = InlineKeyboardButton(text=str('5'), callback_data=str('5'))
    Button11 = InlineKeyboardButton(text=str('4'), callback_data=str('4'))
    Button12 = InlineKeyboardButton(text=str('S'), callback_data=str('*'))
    Button13 = InlineKeyboardButton(text=str('3'), callback_data=str('3'))
    Button14 = InlineKeyboardButton(text=str('2'), callback_data=str('2'))
    Button15 = InlineKeyboardButton(text=str(','), callback_data=str('.'))
    Button16 = InlineKeyboardButton(text=str('1'), callback_data=str('1'))
    Button17 = InlineKeyboardButton(text=str('0'), callback_data=str('0'))
    Button18 = InlineKeyboardButton(text=str('='), callback_data=str('='))
    Button19 = InlineKeyboardButton('All results', callback_data='All results')
    Button20 = InlineKeyboardButton('Hide keyboard', callback_data='Hide keyboard')
    Keyboard = InlineKeyboardMarkup().add(Button1,
                                          Button2, Button3, Button4, Button5, Button6, Button7,
                                          Button8, Button9, Button10, Button11, Button12, Button13,
                                          Button14, Button15, Button16, Button17, Button18, Button19,
                                          Button20)
    return Keyboard
