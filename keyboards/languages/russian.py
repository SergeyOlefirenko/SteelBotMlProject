import asyncio

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import os
import json
from aiogram import Dispatcher, types
dp = Dispatcher
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

def alloys():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '../../data/alloys.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        alloy = json.load(file)

    return alloy
def Grades():
    buttons_data = alloys()
    # Проверка, что файл имеет ожидаемую структуру
    if not isinstance(buttons_data, list) or not all(isinstance(item, dict)
                                                     and 'text' in item and 'callback_data'
                                                     in item for item in buttons_data):
        raise ValueError("Неверная структура JSON-файла")
    buttons = [
        InlineKeyboardButton(text=text, callback_data=callback_data)
        for alloys_data in buttons_data
        for text, callback_data in zip(alloys_data['text'], alloys_data['callback_data'])
    ]
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
    keyboard.add(*buttons)
    return keyboard

def metals():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '../../data/metals.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        metal = json.load(file)
    return metal

def allMetals():
    buttons_data = metals()
    # Проверка, что файл имеет ожидаемую структуру
    if not isinstance(buttons_data, list) or not all(isinstance(item, dict)
                                                     and 'text' in item and 'callback_data'
                                                     in item for item in buttons_data):
        raise ValueError("Неверная структура JSON-файла")
    buttons = [
        InlineKeyboardButton(text=text, callback_data=callback_data)
        for metal_data in buttons_data
        for text, callback_data in zip(metal_data['text'], metal_data['callback_data'])
    ]
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=6)
    keyboard.add(*buttons)
    return keyboard

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
    # Button18 = InlineKeyboardButton('All results', callback_data='https://cryptoconverter-sand.vercel.app/')

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
