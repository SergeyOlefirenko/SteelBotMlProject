import datetime

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from babel import dates

from ml.data_preparing_for_ml import round_pipe_data_preparation
# from ml.data_preparing_for_ml import round_pipe_data_preparation
from states import MyStates, MESSAGES, USERS, User, user
from keyboards import languages as kb
from database import (get_user_by_id, insert_user, insert_message, insert_result, get_user_actions_by_id,
                      update_round_pipe_data_analysis,
                      get_round_pipe_data_analysis,
                      get_nomenclature_id,
                      update_time_table_data,
                      )
import os
import json

from ml import (forecast, analyze_data)
from keyboards import main_product_keyboard, pipe_type_keyboard, square_rectangle_keyboard, forging_type_keyboard
from ml import (cmd_show_round_pipe_forecast, cmd_show_profile_pipe_forecast, cmd_show_round_bar_forecast,
                cmd_show_square_forecast, cmd_show_rectangle_forecast, cmd_show_round_bar_forging_forecast,
                cmd_show_square_forging_forecast, cmd_show_rectangle_forging_forecast, cmd_show_ring_forging_forecast)

TOKEN = os.environ['token']
bot = Bot(token=TOKEN)
print("https://t.me/SteelBot_bot")

users = {}
userStorage = {}


class Storage:
    value = ''
    old_value = ''
    grade_value = ''
    lang_message = ''


dp = Dispatcher(bot, storage=MemoryStorage())


# Загрузка данных о плотности материалов из JSON файла
# Loading material density data from a JSON file

def get_new_data():
    with open('../data/grades.json', 'r') as file:
        grades = json.load(file)
    return grades


def get_new_language():
    with open('../data/language-code.json', 'r', encoding='utf-8') as file:
        language_c = json.load(file)
    return language_c


def get_new_language_message():
    with open('../data/language-message.json', 'r', encoding='utf-8') as file:
        language_m = json.load(file)
    return language_m


def userStorageUpdate(user_id, value, old_value, grade_value=0):
    userStorage[user_id].value = value
    userStorage[user_id].old_value = old_value
    if grade_value != 0:
        userStorage[user_id].grade_value = grade_value


def log_result(user_id, nomenclature, material, dimensions, weight):
    try:
        # Подготавливаем данные для вставки в коллекцию results
        # Preparing data for insertion into the results collection

        result_data = {
            'user_id': str(user_id),
            'nomenclature': nomenclature,
            'material': material,
            'dimensions': dimensions,
            'weight': weight,
            'timestamp': datetime.datetime.now()
        }

        # Вставляем данные в коллекцию results
        # Inserting data into the results collection

        insert_result(result_data)
        # print("Результат вставлен в коллекцию results:", result_data)
        print("Result inserted into the results collection:", result_data)

        # Запускаем анализ данных после вставки
        analyze_data(result_data)  # Вызываем анализ данных с текущим результатом

    except Exception as e:
        # print(f"Ошибка при вставке данных в results: {e}")
        print(f"Error inserting data into results: {e}")


@dp.message_handler(commands=['forecast'])
async def cmd_show_forecast(message: types.Message):
    """
    Обработчик команды /forecast.
    Открывает инлайн-клавиатуру для выбора типа продукта.
    """
    """
    Handler for the /forecast command.
    Opens an inline keyboard for selecting the type of product.
    """

    user_id = message.from_user.id
    # Проверяем, зарегистрирован ли пользователь
    # Check if the user is registered

    if user_id not in userStorage:
        # Create a storage for the new user
        userStorage[user_id] = Storage()  # Создаем хранилище для нового пользователя

    user = userStorage[user_id]

    if user is None:
        # await message.reply("Вы не зарегистрированы для использования этой команды. Пожалуйста, выполните регистрацию.")
        await cmd_start()
    else:
        # Отправка основной клавиатуры пользователю
        # Sending the main keyboard to the user
        # await message.reply("Выберите категорию продукта:", reply_markup=main_product_keyboard())
        await message.reply("Select a product category:", reply_markup=main_product_keyboard())


# Обработчик для выбора номенклатуры трубы
# Handler for selecting pipe nomenclature

@dp.callback_query_handler(lambda c: c.data == 'category_pipe')
async def process_pipe_category(callback_query: types.CallbackQuery):
    # Изменяем текст сообщения и клавиатуру
    # Change the message text and keyboard
    # await bot.edit_message_text("Выберите номенклатуру продукта:",
    await bot.edit_message_text("Select the product nomenclature:",

                                chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await callback_query.message.edit_reply_markup(reply_markup=pipe_type_keyboard())


# Обработчик для выбора круглой трубы
# Handler for selecting a round pipe
@dp.callback_query_handler(lambda c: c.data == 'pipe_round')
async def cmd_round_pipe(callback_query: types.CallbackQuery):
    # await callback_query.answer("Загружаем прогноз для круглых труб...")
    await callback_query.answer("Loading forecast for round pipes...")  # Callback confirmation

    await cmd_show_round_pipe_forecast(callback_query)


# Обработчик для выбора профильной трубы
# Handler for selecting a profile pipe
@dp.callback_query_handler(lambda c: c.data == 'pipe_profile')
async def cmd_profile_pipe(callback_query: types.CallbackQuery):
    # await callback_query.message.reply("Загружаем прогноз для профильных труб...")
    await callback_query.message.reply("Loading forecast for profile pipes...")
    await cmd_show_round_pipe_forecast(callback_query)


def get_material_name(grade_value):
    for material in grades:
        for name, details in material.items():
            if details[0]['grade_value'] == grade_value:
                return name
    return None


def get_dimensions(value):
    # value должен иметь формат "диаметр, толщина стенки, длина"
    # value must have the format "diameter, wall thickness, length"
    dimensions = value.split(',')
    if len(dimensions) == 3:
        diameter = dimensions[0].strip()
        wall_thickness = dimensions[1].strip()
        length = dimensions[2].strip()
        return f"{diameter}, {wall_thickness}, {length}"
    # return "Неверный формат"
    return "Invalid format"


@dp.message_handler(commands=['all_results'])
async def cmd_all_results(callback_q: types.CallbackQuery):
    user_id = callback_q.from_user.id
    # print(f"Запрос для user_id: {user_id}")
    print(f"Request for user_id: {user_id}")

    user_actions = get_user_actions_by_id(user_id)
    # print(f"Полученные действия: {user_actions}")
    print(f"Received actions: {user_actions}")

    if user_actions:
        result_message = "Your actions:\n"
        for action in user_actions:
            # Check and format timestamp
            if isinstance(action['timestamp'], str):
                timestamp_obj = datetime.datetime.strptime(action['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
            else:
                timestamp_obj = action['timestamp']  # If it's already a datetime object

            # Convert date to the desired format
            formatted_timestamp = timestamp_obj.strftime('%Y-%m-%d %H:%M:%S')

            # Form the action string
            result_message += (
                f"{formatted_timestamp}\n"
                f"Nomenclature: {action['nomenclature']}\n"
                f"Material: {action['material']}\n"
                f"Dimensions: {action['dimensions']}\n"
                f"Weight: {action['weight']}\n\n"
            )

        print(f"Final message to send: {result_message}")

        # if user_actions:
    #     result_message = "Ваши действия:\n"
    #     for action in user_actions:
    #         # Проверяем и форматируем timestamp
    #         if isinstance(action['timestamp'], str):
    #             timestamp_obj = datetime.datetime.strptime(action['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
    #         else:
    #             timestamp_obj = action['timestamp']  # Если это уже объект datetime
    #
    #         # Преобразуем дату в нужный формат
    #         formatted_timestamp = timestamp_obj.strftime('%Y-%m-%d %H:%M:%S')
    #
    #         # Формируем строку действия
    #         result_message += (
    #             f"{formatted_timestamp}\n"
    #             f"Номенклатура: {action['nomenclature']}\n"
    #             f"Материал: {action['material']}\n"
    #             f"Размеры: {action['dimensions']}\n"
    #             f"Вес: {action['weight']}\n\n"
    #         )
    #
    #     print(f"Финальное сообщение для отправки: {result_message}")

        # Разбиваем сообщение, если оно слишком длинное
        # Split the message if it is too long
        while len(result_message) > 4096:
            part = result_message[:4096]
            result_message = result_message[4096:]
            await bot.send_message(chat_id=callback_q.from_user.id, text=part)

        # Отправляем остаток
        # Send the remainder
        await bot.send_message(chat_id=callback_q.from_user.id, text=result_message)
    else:
        # await bot.send_message(chat_id=callback_q.from_user.id, text="У вас пока нет записанных действий.")
        await bot.send_message(chat_id=callback_q.from_user.id, text="You currently have no recorded actions.")


@dp.message_handler(commands=['menu'])
async def cmd_menu(message: types.Message, state: FSMContext):
    print(message.text)
    user_id = message.from_user.id # Get user_id
    keyboard = kb.Keyboard_menu
    print(message.from_user.language_code)
    print(message.from_user.id)
    if user_id in userStorage:
        if message.from_user.language_code == 'en':
            keyboard = kb.english.Keyboard_menu
        elif message.from_user.language_code == 'ru':
            keyboard = kb.russian.Keyboard_menu
        await message.delete()

    await message.answer(message.text, reply_markup=keyboard)


@dp.message_handler(commands=['restart'])
async def cmd_restart(message: types.Message, state: FSMContext):
    print(message.text)


@dp.message_handler(commands=['exit'])
async def cmd_exit(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    # Здесь используем types.InlineKeyboardButton.url для создания кнопки с ссылкой
    button = types.InlineKeyboardButton(text="Cryptoconverter", url="https://cryptoconverter-sand.vercel.app/")
    keyboard.add(button)
    await message.answer("Click the button to open the app:", reply_markup=keyboard)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext):
    user = get_user_by_id(message.from_user.id)
    user_id = message.from_user.id
    new_lang_m = get_new_language_message()
    language_m = new_lang_m
    try:
        if user_id not in userStorage:
            userStorage[user_id] = Storage()
            if user is None:
                for item in language_m:
                    if message.from_user.language_code in item:
                        lang_message = item[message.from_user.language_code][0]['lang_message']
                        await message.answer(lang_message)
                        await state.set_state(MyStates.all()[1])
                        break  # Выходим из цикла после успешного выполнения
                else:
                    if len(userStorage[user_id].value) == 0:
                        lang_message = language_m[0][message.from_user.language_code][1]['lang_message']
                        await message.answer(lang_message)
                        await state.set_state(MyStates.all()[1])
                    else:
                        lang_message = language_m[0][message.from_user.language_code][2]['lang_message']
                        await message.answer(lang_message)
    except KeyError:
        lang_message = language_m[0][message.from_user.language_code][3]['lang_message']
        await message.answer(lang_message)


# Обработчики состояний для заполнения таблицы Users database mongoDB
@dp.message_handler(state=MyStates.STATE_1)
async def name(message: types.Message, state: FSMContext):
    user = get_user_by_id(message.from_user.id)
    new_lang_m = get_new_language_message()
    language_m = new_lang_m
    if user is None:
        for item in language_m:
            if message.from_user.language_code in item:
                lang_message = item[message.from_user.language_code][4]['lang_message']
                await state.update_data(user_id=message.from_user.id)
                await state.update_data(name=message.text)
                await message.answer(lang_message)
                await state.set_state(MyStates.all()[2])
    else:
        if len(user) == 0:
            user_data = await state.get_data()
            user_data['name'] = message.text
            lang_message = language_m[0][message.from_user.language_code][4]['lang_message']
            await state.update_data(name=message.text)
            await message.answer(lang_message)
            await state.set_state(MyStates.all()[2])


@dp.message_handler(lambda message: message.text == "Выбрать дату", state=MyStates.STATE_BIRTHDAY)
async def select_birthday(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await message.answer("Выберите дату из выпадающего списка:", reply_markup=kb.keyboard_with_dates)
    await MyStates.next()


@dp.message_handler(lambda message: message.text in dates, state=MyStates.STATE_BIRTHDAY)
async def process_birthday(message: types.Message, state: FSMContext):
    selected_date = message.text
    # Сохраннение выбранной даты в состоянии пользователя
    await state.update_data(birthday=selected_date)
    await message.answer(f"Вы выбрали дату рождения: {selected_date}")
    await MyStates.next()


@dp.message_handler(state=MyStates.STATE_2)
async def age(message: types.Message, state: FSMContext):
    user = get_user_by_id(message.from_user.id)
    new_lang_m = get_new_language_message()
    language_m = new_lang_m
    if user is None:
        user_data = await state.get_data()
        user_data['age'] = message.text
        for item in language_m:
            if message.from_user.language_code in item:
                lang_message = item[message.from_user.language_code][5]['lang_message']
                await state.update_data(age=message.text)
                await message.answer(lang_message)
                await state.set_state(MyStates.all()[3])
    else:
        if len(user) == 0:
            user_data = await state.get_data()
            user_data['age'] = message.text
            lang_message = language_m[0][message.from_user.language_code][5]['lang_message']
            await state.update_data(age=message.text)
            await message.answer(lang_message)
            await state.set_state(MyStates.all()[3])


@dp.message_handler(state=MyStates.STATE_3)
async def email_phone(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    user_id = message.from_user.id
    new_lang_m = get_new_language_message()
    language_m = new_lang_m

    if 'email' not in user_data:
        user_data['email'] = message.text
        for item in language_m:
            if message.from_user.language_code in item:
                lang_message = item[message.from_user.language_code][6]['lang_message']
                await state.update_data(email=message.text)
                await message.answer(lang_message)
                return

    if 'phone' not in user_data:
        user_data['phone'] = message.text
        await state.update_data(phone=message.text)

        # Создание записи в базе данных с данными пользователя
        user_to_insert = {
            'UserID': user_id,
            'Firstname': user_data.get('name', ''),
            'Birthday': user_data.get('age', ''),
            'Phone': user_data['phone'],
            'Mail': user_data['email']
        }
        insert_user(user_to_insert)
        for item in language_m:
            if message.from_user.language_code in item:
                lang_message = item[message.from_user.language_code][7]['lang_message']
                await message.answer(lang_message + f", {user_data.get('name', '')}!")
                await state.set_state(MyStates.all()[4])
                await menu(message)
                await message.delete()


@dp.message_handler(state=MyStates.STATE_4)
async def menu(message: types.Message):
    chat_id = message.from_user.id
    state = dp.current_state(user=chat_id)
    # keyboard = kb.russian.Keyboard_menu
    keyboard = kb.Keyboard_menu  # Вызов меню после регистрации пользователя (пока из english.py)
    if message.text == 'Change language':
        keyboard = kb.Keyboard_menu_change_language
    elif message.text == 'Главное меню' or message.text == '/start' or message.text == '/restart' \
            or message.text == '/menu' or message.text == 'Menu' or message.text == 'Main menu':
        keyboard = kb.Keyboard_menu
        await message.delete()

    # Этот блок тестовый и будет заменен функцией с передачей данных из JSON
    elif message.text == 'Deutsch':
        keyboard = kb.deutsch.Keyboard_menu
        await message.delete()
    elif message.text == 'English':
        keyboard = kb.english.Keyboard_menu
        await message.delete()
    elif message.text == 'Français':
        keyboard = kb.french.Keyboard_menu_french
        await message.delete()
    elif message.text == 'Italiano':
        keyboard = kb.italian.Keyboard_menu_italian
        await message.delete()
    elif message.text == 'Español':
        keyboard = kb.spanish.Keyboard_menu_spanish
        await message.delete()
    elif message.text == 'Język polski':
        keyboard = kb.polish.Keyboard_menu_polish
        await message.delete()
    elif message.text == 'Slovak':
        keyboard = kb.slovak.Keyboard_menu_slovak
        await message.delete()
    elif message.text == 'Slovenský':
        keyboard = kb.slovenian.Keyboard_menu_slovenian
        await message.delete()
    elif message.text == 'Русский':
        keyboard = kb.russian.Keyboard_menu
        await message.delete()
    elif message.text == '日本語':
        keyboard = kb.japanese.Keyboard_menu_japanese
        await message.delete()
    elif message.text == '한국어':
        keyboard = kb.korean.Keyboard_menu_korean
        await message.delete()
    elif message.text == 'Труба' or message.text == 'Pipe':
        keyboard = kb.Keyboard_menu_pipe
        await message.delete()
    elif message.text == 'Квадрат/прямоугольник' or message.text == 'Square/rectangle':
        keyboard = kb.Keyboard_menu_squareBar
        await message.delete()
    elif message.text == 'Лист/полоса' or message.text == 'Sheet/Band':
        keyboard = kb.Keyboard_menu_sheet
        await message.delete()
    elif message.text == 'Круг/кольцо' or message.text == 'Round Bar/Circle':
        keyboard = kb.Keyboard_menu_roundBar
        await message.delete()
    elif message.text == 'Шестигранник' or message.text == 'Hexagon':
        keyboard = kb.Keyboard_menu_hexagon
        await message.delete()
    elif message.text == 'Арматура' or message.text == 'Armature':
        keyboard = kb.Keyboard_menu_armature
        await message.delete()
    # Вызов обработчиков
    elif message.text == 'Calculator' or message.text == 'calculator' \
            or message.text == 'Стандартный калькулятор':
        keyboard = kb.calculator()
        await state.set_state(MyStates.all()[5])
    elif message.text == 'Круглая' or message.text == 'Round':
        keyboard = kb.Grades()
        await message.delete()
        await state.set_state(MyStates.all()[6])
    elif message.text == 'Профильная' or message.text == 'Profile':
        keyboard = kb.Grades()
        await state.set_state(MyStates.all()[7])
    elif message.text == 'Квадрат' or message.text == 'Square Bar':
        keyboard = kb.Grades()
        await state.set_state(MyStates.all()[8])
    elif message.text == 'Прямоугольник' or message.text == 'Rectangle':
        keyboard = kb.Grades()
        await state.set_state(MyStates.all()[8])
        await message.delete()
    elif message.text == 'Лист' or message.text == 'Sheet':
        keyboard = kb.Grades()
        await state.set_state(MyStates.all()[9])
    elif message.text == 'Полоса' or message.text == 'Band':
        keyboard = kb.Grades()
        await state.set_state(MyStates.all()[9])
    elif message.text == 'Круг' or message.text == 'Round Bar':
        keyboard = kb.Grades()
        await state.set_state(state='A')
    elif message.text == 'Кольцо' or message.text == 'Circle':
        keyboard = kb.Grades()
        await state.set_state(state='A')
    elif message.text == 'Сфера/шар' or message.text == 'Sphere/Ball':
        keyboard = kb.Keyboard_menu_sphere
        await message.delete()
    elif message.text == 'Марка материала сферы/шара' or message.text == 'Sphere/ball material grade':
        keyboard = kb.Grades()
        await state.set_state(state='B')
    elif message.text == 'Балка' or message.text == 'Beam':
        keyboard = kb.Keyboard_menu_beam
    elif message.text == 'Тавровая' or message.text == 'Single-shelf beam':
        keyboard = kb.Grades()
        await state.set_state(state='C')
    elif message.text == 'Двутавровая' or message.text == 'Double shelf beam':
        keyboard = kb.Grades()
        await state.set_state(state='C')
    elif message.text == 'Швеллер' or message.text == 'Channel':
        keyboard = kb.Keyboard_menu_channel
    elif message.text == 'Равнополочный' or message.text == 'Equal-shelf':
        keyboard = kb.Grades()
        await state.set_state(state='D')
    elif message.text == 'Не равнополочный' or message.text == 'Not equal-shelf':
        keyboard = kb.Grades()
        await state.set_state(state='D')
    elif message.text == 'Уголок' or message.text == 'Corner':
        keyboard = kb.Keyboard_menu_corner
    elif message.text == 'Равносторонний' or message.text == 'Equilateral':
        keyboard = kb.Grades()
        await state.set_state(state='E')
    elif message.text == 'Не равносторонний' or message.text == 'Not equilateral':
        keyboard = kb.Grades()
        await state.set_state(state='E')
    elif message.text == 'Материал и номер профиля' or message.text == 'Material and profile number':
        keyboard = kb.Grades()
        await state.set_state(state='F')
    elif message.text == 'Материал и профиль' or message.text == 'Material and profile':
        keyboard = kb.Grades()
        await state.set_state(state='G')
    # Добавление фото (просто тестовый код для проверки при вводе приветствия):
    if message.text == 'Руководство пользователя' or message.text == 'User manual':
        await bot.send_message(chat_id=message.from_user.id, text='Description')
        # Необходимо добавить текст описания
        await message.delete()
    elif message.text == 'Start':
        await bot.send_photo(chat_id=message.from_user.id, photo=types.InputFile('sobach.jpg'))
        keyboard = kb.Keyboard_menu
        await bot.send_message(chat_id=message.from_user.id, text='Руководство пользователя, Руководство пользователя',
                               reply_markup=keyboard)
    elif message.text == 'Hi' or message.text == 'Hi!' or message.text == 'Hello' or message.text == 'Hello!':
        await bot.send_photo(chat_id=message.from_user.id, photo=types.InputFile('sobach.jpg'))
    elif message.text == 'M' or message.text == 'М' or message.text == 'm' or message.text == 'м':
        await bot.send_photo(chat_id=message.from_user.id, photo=types.InputFile('mc.jpg'))
    elif message.text == 'C' or message.text == 'С' or message.text == 'c' or message.text == 'с':
        await bot.send_video(chat_id=message.from_user.id, video=types.InputFile('cv.mp4'))
    await message.answer(message.text, reply_markup=keyboard)

    if message.text == 'C' or message.text == 'С' or message.text == 'c' or message.text == 'с':
        await state.set_state(state='V')

    #####################################################################################################
    # Создаем состояние для отслеживания состояния воспроизведения видео
    class VideoPlaybackState(FSMContext):
        pass

    # Функция для отправки видео с кнопками управления
    async def send_video_with_controls(message: types.Message, state: FSMContext):
        await VideoPlaybackState.set("playing")  # Устанавливаем начальное состояние воспроизведения

        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton(text="Пауза/Продолжить", callback_data="pause_resume"),
            types.InlineKeyboardButton(text="Включить/Отключить звук", callback_data="toggle_sound")
        )

        await message.answer_video(
            video=types.InputFile('cv.mp4'),
            reply_markup=markup
        )

    # Функция для обновления кнопок управления в чате
    async def update_controls(message: types.Message, state: FSMContext):
        current_state = await state.get()

        markup = types.InlineKeyboardMarkup(row_width=2)
        if current_state == "playing":
            markup.add(
                types.InlineKeyboardButton(text="Пауза", callback_data="pause"),
                types.InlineKeyboardButton(text="Включить/Отключить звук", callback_data="toggle_sound")
            )
        elif current_state == "paused":
            markup.add(
                types.InlineKeyboardButton(text="Продолжить", callback_data="resume"),
                types.InlineKeyboardButton(text="Включить/Отключить звук", callback_data="toggle_sound")
            )

        await bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message.message_id, reply_markup=markup)

    # Команда для начала воспроизведения видео
    # @dp.message_handler(Command("start"))
    @dp.message_handler(state='V')
    # @dp.callback_query_handler(state='A')
    async def cmd_start(message: types.Message, state: FSMContext):
        await send_video_with_controls(message, state)
        await bot.send_message(chat_id=message.from_user.id, text='Выбрано видео')
        print("Выбрано видео")

    # Callback-обработчик для кнопок управления
    @dp.callback_query_handler(lambda c: c.data in ["pause_resume", "toggle_sound", "pause", "resume"])
    async def callback_controls(callback_query: types.CallbackQuery, state: FSMContext):
        current_state = await state.get()

        if callback_query.data == "pause_resume":
            if current_state == "playing":
                # Логика для паузы видео
                await state.set("paused")
            elif current_state == "paused":
                # Логика для продолжения воспроизведения видео
                await state.set("playing")
        elif callback_query.data == "toggle_sound":
            # Логика для включения/отключения звука
            # Просто переключаем состояние между "sound_on" и "sound_off"
            current_sound_state = await state.get_data("sound_state") or "sound_on"
            new_sound_state = "sound_off" if current_sound_state == "sound_on" else "sound_on"
            await state.update_data(sound_state=new_sound_state)

        await update_controls(callback_query.message, state)
        await bot.answer_callback_query(callback_query.id, text="Вы изменили состояние воспроизведения видео")


# Обработчик стандартного калькулятора
@dp.callback_query_handler(state=MyStates.STATE_5)
async def standartCalc(callback_q: types.CallbackQuery):
    chat_id = callback_q.from_user.id
    value = userStorage[chat_id].value
    old_value = userStorage[chat_id].old_value
    if callback_q.data == 'Main' or callback_q.data == 'Main menu' \
            or callback_q.data == '/menu' or callback_q.data == '/start' \
            or callback_q.data == '/restart' or callback_q.data == 'Главное меню':
        chat_id = callback_q.from_user.id
        state = dp.current_state(user=chat_id)
        await state.set_state(MyStates.all()[4])
    elif callback_q.data == 'Hide keyboard':
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='Keyboard hidden. To open press Menu',
                               reply_markup=types.ReplyKeyboardRemove())
    data = callback_q.data
    if callback_q.data == ' ':
        pass
    elif callback_q.data == 'C':
        value = ' '
    elif callback_q.data == 'Ø':
        value = ' '
    elif callback_q.data == '<=':
        if value != ' ':
            try:
                value = value[:len(value) - 1]
            except:
                value = value
    elif callback_q.data == '=':
        try:
            value = str(eval(value))
        except:
            value = 'Mistake'
    else:
        value += data
    userStorageUpdate(chat_id, value, old_value)
    if (value != old_value and value != ' ') or ('0' != old_value and value == ' '):
        if value == ' ':
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text='0', reply_markup=kb.calculator())
            old_value = '0'
        else:
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text=value, reply_markup=kb.calculator())
            old_value = value
        if old_value == 'Mistake':
            value = ' '
    userStorageUpdate(chat_id, value, old_value)


# Функция исключающая введение вредоносного исполняемого кода типа: "__import__('subprocess').getoutput('rm –rf *')"
def eval_expression(input_string):
    allowed_names = {"sum": sum}
    code = compile(input_string, "<string>", "eval")
    for name in code.co_names:
        if name not in allowed_names:
            raise NameError(f"Использование {name} не разрешено.")
    return eval(code, {"__builtins__": {}}, allowed_names)


# Обработчик для калькулятора трубы


@dp.callback_query_handler(state=MyStates.STATE_6)
async def CalcPipeRound(callback_q: types.CallbackQuery):
    global grades, material
    new_data = get_new_data()
    chat_id = callback_q.from_user.id
    value = userStorage[chat_id].value
    old_value = userStorage[chat_id].old_value
    grade_value = 0
    grades = new_data
    weight = 0
    material_name = ''
    for item in grades:
        if callback_q.data in item:
            grade_value = item[callback_q.data][0]['grade_value']
            material = list(item.keys())[0]  # Получаем название материала

    if callback_q.data == '=':
        try:
            # Проверка длины, если введены только два параметра
            if value.count("*") == 1:  # Если введены только диаметр и толщина стенки
                value += "*1"  # Добавляем длину по умолчанию (1 метр)

            # Получаем вес
            weight = calculate(value, userStorage[chat_id].grade_value)
            if 'kg' in weight:  # Проверяем, что вес вычислен корректно
                # Записываем результат в базу данных
                dimensions = value.replace('*', 'x')  # Заменяем знак * на x для отображения
                await log_result(chat_id, "Round pipe", material, 'Ø' + dimensions + ' m', weight)

        except Exception as e:
            weight = 'Mistake'

    if callback_q.data == 'Main' or callback_q.data == 'Main menu' \
            or callback_q.data == '/menu' or callback_q.data == '/start' \
            or callback_q.data == '/restart' or callback_q.data == 'Главное меню' \
            or callback_q.data == 'Expand keyboard':
        chat_id = callback_q.from_user.id
        state = dp.current_state(user=chat_id)
        await state.set_state(MyStates.all()[4])
    elif callback_q.data == 'All metals':
        chat_id = callback_q.from_user.id
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='All metals',
                               reply_markup=kb.allMetals())

    if callback_q.data == 'Профильная' or callback_q.data == 'Profile':
        chat_id = callback_q.from_user.id
        state = dp.current_state(user=chat_id)
        await state.set_state(MyStates.all()[7])
        await bot.answer_callback_query(callback_q.id, text=callback_q.data)
    elif callback_q.data == 'All results':
        await cmd_all_results(callback_q)  # Передаем сам объект callback_q

    elif callback_q.data == 'Hide keyboard':
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='Keyboard hidden. To open press Menu',
                               reply_markup=types.ReplyKeyboardRemove())
    data = callback_q.data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if callback_q.data == ' ':
        pass
    elif callback_q.data == 'C':
        value = ' '
    elif callback_q.data == 'Ø':
        value = ' '

    elif callback_q.data == '<=':
        if value != ' ':
            try:
                value = value[:len(value) - 1]
            except:
                value = value
    elif callback_q.data == '=':
        try:
            value = calculate(value, userStorage[chat_id].grade_value)
        except:
            value = 'Mistake'
    else:
        value += data
    userStorageUpdate(chat_id, value, old_value, grade_value)

    if (value != old_value and value != ' ') or ('0' != old_value and value == ' '):
        if value == ' ':
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text='0', reply_markup=kb.pipeRound())
            old_value = '0'
        else:
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text=value, reply_markup=kb.pipeRound())
            old_value = value
        if old_value == 'Mistake':
            value = ' '
    userStorageUpdate(chat_id, value, old_value, grade_value)


def calculate(param, grade_value):
    values = param.split("*")
    print("param " + param)
    print(values)
    print(grade_value, " - grade_value")
    constanta = grade_value
    pi = 3.141592653

    # Если два параметра (диаметр и толщина), добавляем длину по умолчанию = 1
    if len(values) == 2:
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = 1  # Длина по умолчанию = 1

        if res1 - (res2 * 2) != 0 and res1 - (res2 * 2) > 0:
            res = ((res1 / 1000) ** 2 - ((res1 - res2 * 2) / 1000) ** 2) * pi / 4 * int(constanta) * res3
            return '%.3f' % res + ' kg.'
        else:
            return 'Mistake, with the entered parameters, the inner diameter is missing'

    # Если три параметра (диаметр, толщина и длина)
    elif len(values) == 3:
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = float(values[2])  # Ввод длины

        if res1 - (res2 * 2) != 0 and res1 - (res2 * 2) > 0:
            res = ((res1 / 1000) ** 2 - ((res1 - res2 * 2) / 1000) ** 2) * pi / 4 * int(constanta) * res3
            return '%.3f' % res + ' kg.'
        else:
            return 'Mistake, with the entered parameters, the inner diameter is missing'
    else:
        return 'Mistake. Try again'


# #Обработчик для профильной трубы:

@dp.callback_query_handler(state=MyStates.STATE_7)
async def CalcPipeProfile(callback_q: types.CallbackQuery):
    global grades
    new_data = get_new_data()
    chat_id = callback_q.from_user.id
    value = userStorage[chat_id].value
    old_value = userStorage[chat_id].old_value
    grade_value = 0
    grades = new_data
    weight = 0
    for item in grades:
        if callback_q.data in item:
            grade_value = item[callback_q.data][0]['grade_value']

    if callback_q.data == '=':
        try:
            weight = calcProfile(value, userStorage[chat_id].grade_value)
            if 'kg' in weight:  # Проверяем, что вес вычислен корректно
                # Записываем результат в базу данных
                log_result(chat_id, "Profile Pipe", grade_value, value, weight)

        except Exception as e:
            weight = 'Mistake'

    if callback_q.data == 'Main' or callback_q.data == 'Main menu' \
            or callback_q.data == '/menu' or callback_q.data == '/start' \
            or callback_q.data == '/restart' or callback_q.data == 'Главное меню' \
            or callback_q.data == 'Expand keyboard':
        chat_id = callback_q.from_user.id
        state = dp.current_state(user=chat_id)
        await state.set_state(MyStates.all()[4])
        await bot.answer_callback_query(callback_q.id, text=callback_q.data)
    elif callback_q.data == 'Hide keyboard':
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='Keyboard hidden. To open press Menu',
                               reply_markup=types.ReplyKeyboardRemove())
    elif callback_q.data == 'All metals':
        # elif callback_q.data in metals:
        chat_id = callback_q.from_user.id
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='All metals',
                               reply_markup=kb.allMetals())
    elif callback_q.data == 'All grades':
        await bot.answer_callback_query(callback_q.id, text='This is operation manual')
    data = callback_q.data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if callback_q.data == ' ':
        pass
    elif callback_q.data == 'C':
        value = ' '
    elif callback_q.data == '□':
        value = ' '

    elif callback_q.data == '<=':
        if value != ' ':
            try:
                value = value[:len(value) - 1]
            except:
                value = value
    elif callback_q.data == '=':
        try:
            value = calcProfile(value, userStorage[chat_id].grade_value)
        except:
            value = 'Mistake'
    else:
        value += data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if (value != old_value and value != ' ') or ('0' != old_value and value == ' '):
        if value == ' ':
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text='0', reply_markup=kb.pipeProfile())
            old_value = '0'
        else:
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text=value, reply_markup=kb.pipeProfile())
            old_value = value
        if old_value == 'Mistake':
            value = ' '
    userStorageUpdate(chat_id, value, old_value, grade_value)


# Функция обработки данных профильной трубы:
# Необходимо прописать условие с учетом коэффициента уменьшения массы с учетом радиуса.
def calcProfile(param, grade_value):
    values = param.split("*")
    res = 0
    constanta = grade_value
    # Для квадратного сечения длиной 1 м.
    if len(values) == 2:
        res1 = float(values[0])
        res2 = float(values[1])
        res = ((res1 / 1000) ** 2 - ((res1 - res2 * 2) / 1000) ** 2) * int(constanta)
        return '%.3f' % res + ' кг./м.'

    # Для прямоугольного сечения длиной 1 метр или заданного метража, в зависимости от условия.
    elif len(values) == 3:
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = float(values[2])
        if res2 in range(0, 22) and res2 != res1 and res2 < (res1 / 1.2) \
                and res2 < (res1 / 1.25) and res2 < (res1 / 1.33) and res2 < (res1 / 1.5) \
                and res2 < (res1 / 1.667) and res2 < (res1 / 1.8) and res2 < (res1 / 2) \
                and res2 < (res1 / 2.2) and res2 < (res1 / 2.25) and res2 < (res1 / 2.33) \
                and res2 < (res1 / 2.5) and res2 < (res1 / 2.8) and res2 < (res1 / 3):
            res = ((res1 / 1000) ** 2 - ((res1 - res2 * 2) / 1000) ** 2) * int(constanta) * res3
            return '%.3f' % res + ' кг.'
        else:
            res = (((res1 / 1000) * (res2 / 1000)) - ((res1 - (res3 * 2)) / 1000) * ((res2 - (res3 * 2)) / 1000)) * int(
                constanta)
            return '%.3f' % res + ' кг./м'

    # Для прямоугольного сечения длиной больше 1 метра
    elif len(values) == 4:
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = float(values[2])
        res4 = float(values[3])
        if res4 != 1:
            res = ((res1 / 1000) * (res2 / 1000) - ((res1 - (res3 * 2)) / 1000)
                   * ((res2 - (res3 * 2)) / 1000)) * int(constanta) * res4
            return '%.3f' % res + ' кг.'
        else:
            return '%.3f' % res + ' кг./м.'
    else:
        return ('Mistake. Try again')


# Обработчик для квадрата и прямоугольника:

@dp.callback_query_handler(state=MyStates.STATE_8)
async def squareBar(callback_q: types.CallbackQuery):
    global grades
    new_data = get_new_data()
    chat_id = callback_q.from_user.id
    value = userStorage[chat_id].value
    old_value = userStorage[chat_id].old_value
    grade_value = 0
    grades = new_data
    for item in grades:
        if callback_q.data in item:
            grade_value = item[callback_q.data][0]['grade_value']
    if callback_q.data == 'Main' or callback_q.data == 'Main menu' \
            or callback_q.data == '/menu' or callback_q.data == '/start' \
            or callback_q.data == '/restart' or callback_q.data == 'Главное меню' \
            or callback_q.data == 'Expand keyboard':
        chat_id = callback_q.from_user.id
        state = dp.current_state(user=chat_id)
        await state.set_state(MyStates.all()[4])
        await bot.answer_callback_query(callback_q.id, text=callback_q.data)
    elif callback_q.data == 'Hide keyboard':
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='Keyboard hidden. To open press Menu',
                               reply_markup=types.ReplyKeyboardRemove())
    elif callback_q.data == 'All metals':
        # elif callback_q.data in metalls:
        chat_id = callback_q.from_user.id
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='All metals',
                               reply_markup=kb.allMetals())
    elif callback_q.data == 'All grades':
        # await bot.answer_callback_query(callback_q.id, text=callback_q.data)
        await bot.answer_callback_query(callback_q.id, text='This is operation manual')
    data = callback_q.data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if callback_q.data == ' ':
        pass
    elif callback_q.data == 'C':
        value = ' '
    elif callback_q.data == '■':
        value = ' '

    elif callback_q.data == '<=':
        if value != ' ':
            try:
                value = value[:len(value) - 1]
            except:
                value = value
    elif callback_q.data == '=':
        try:
            value = calcSquare(value, userStorage[chat_id].grade_value)
        except:
            value = 'Mistake'
    else:
        value += data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if (value != old_value and value != ' ') or ('0' != old_value and value == ' '):
        if value == ' ':
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text='0', reply_markup=kb.square())
            old_value = '0'
        else:
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text=value, reply_markup=kb.square())
            old_value = value
        if old_value == 'Mistake':
            value = ' '
    userStorageUpdate(chat_id, value, old_value, grade_value)


# Функция обработки данных квадрата, прямоугольника, листа и полосы:
def calcSquare(param, grade_value):
    values = param.split("*")
    res = 0
    constanta = grade_value
    # Для квадратного сечения длиной 1 м.
    if len(values) == 1:
        # a = values[0]
        res1 = float(values[0])
        res = (res1 / 1000) ** 2 * int(constanta)
        return '%.2f' % res + ' кг./м.'
    # Для квадратного сечения длиной больше 1 м. или прямоугольного сечения длиной 1 метр
    elif len(values) == 2:
        res1 = float(values[0])
        res2 = float(values[1])
        if res2 < res1:
            res = (res1 / 1000) ** 2 * int(constanta) * res2
            return '%.2f' % res + ' кг.'
        elif res2 >= res1:
            res = (res1 / 1000) * (res2 / 1000) * int(constanta)
            return '%.2f' % res + ' кг./м'
    # Для прямоугольного сечения заданного метража
    elif len(values) == 3:
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = float(values[2])
        res = (res1 / 1000) * (res2 / 1000) * int(constanta) * res3
        return '%.2f' % res + ' кг.'
    else:
        return ('Mistake. Try again')


# Обработчик для листа и полосы:

@dp.callback_query_handler(state=MyStates.STATE_9)
async def calcFlatAll(callback_q: types.CallbackQuery):
    global grades
    new_data = get_new_data()
    chat_id = callback_q.from_user.id
    value = userStorage[chat_id].value
    old_value = userStorage[chat_id].old_value
    grade_value = 0
    grades = new_data
    for item in grades:
        if callback_q.data in item:
            grade_value = item[callback_q.data][0]['grade_value']
    if callback_q.data == 'Main' or callback_q.data == 'Main menu' \
            or callback_q.data == '/menu' or callback_q.data == '/start' \
            or callback_q.data == '/restart' or callback_q.data == 'Главное меню':
        chat_id = callback_q.from_user.id
        state = dp.current_state(user=chat_id)
        await state.set_state(MyStates.all()[4])
        await bot.answer_callback_query(callback_q.id, text=callback_q.data)
    elif callback_q.data == 'Hide keyboard':
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='Keyboard hidden. To open press Menu',
                               reply_markup=types.ReplyKeyboardRemove())
    elif callback_q.data == 'All metals':
        # elif callback_q.data in metalls:
        chat_id = callback_q.from_user.id
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='All metals',
                               reply_markup=kb.allMetals())
    elif callback_q.data == 'All grades':
        # await bot.answer_callback_query(callback_q.id, text=callback_q.data)
        await bot.answer_callback_query(callback_q.id, text='This is operation manual')

    data = callback_q.data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if callback_q.data == ' ':
        pass
    elif callback_q.data == 'C':
        value = ' '
    elif callback_q.data == '▬':
        value = ' '

    elif callback_q.data == '<=':
        if value != ' ':
            try:
                value = value[:len(value) - 1]
            except:
                value = value
    elif callback_q.data == '=':
        try:
            value = calcFlat(value, userStorage[chat_id].grade_value)
        except:
            value = 'Mistake'
    else:
        value += data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if (value != old_value and value != ' ') or ('0' != old_value and value == ' '):
        if value == ' ':
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text='0', reply_markup=kb.flat())
            old_value = '0'
        else:
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text=value, reply_markup=kb.flat())
            old_value = value
        if old_value == 'Mistake':
            value = ' '
    userStorageUpdate(chat_id, value, old_value, grade_value)


# Функция обработки данных квадрата, прямоугольника, листа и полосы:
def calcFlat(param, grade_value):
    values = param.split("*")
    res = 0
    constanta = grade_value
    # Для листа или полосы длиной 1 м.
    if len(values) == 2:
        res1 = float(values[0])
        res2 = float(values[1])
        res = ((res1 / 1000) * (res2 / 1000)) * int(constanta)
        return '%.2f' % res + ' кг./м.'
    # Для листа или полосы длиной больше 1 м.
    elif len(values) == 3:
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = float(values[2])
        if res2 != res1:
            res = ((res1 / 1000) * (res2 / 1000)) * int(constanta) * res3
            return '%.2f' % res + ' кг.'
    else:
        return ('Mistake. Try again')


# Обработчик для калькулятора кругов и колец
@dp.callback_query_handler(state='A')
async def roundCalc(callback_q: types.CallbackQuery):
    global grades
    new_data = get_new_data()
    chat_id = callback_q.from_user.id
    value = userStorage[chat_id].value
    old_value = userStorage[chat_id].old_value
    grade_value = 0
    grades = new_data
    for item in grades:
        if callback_q.data in item:
            grade_value = item[callback_q.data][0]['grade_value']
    if callback_q.data == 'Main' or callback_q.data == 'Main menu' \
            or callback_q.data == '/menu' or callback_q.data == '/start' \
            or callback_q.data == '/restart' or callback_q.data == 'Главное меню':
        chat_id = callback_q.from_user.id
        state = dp.current_state(user=chat_id)
        await state.set_state(MyStates.all()[4])
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='Keyboard hidden. To open press Menu',
                               reply_markup=types.ReplyKeyboardRemove())
    elif callback_q.data == 'All metals':
        # elif callback_q.data in metalls:
        chat_id = callback_q.from_user.id
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='All metals',
                               reply_markup=kb.allMetals())
    # elif callback_q.data == 'All grades':
    #     await bot.answer_callback_query(callback_q.id, text='This is operation manual')
    data = callback_q.data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if callback_q.data == ' ':
        pass
    elif callback_q.data == 'C':
        value = ' '
    elif callback_q.data == 'Ø':
        value = ' '

    elif callback_q.data == '<=':
        if value != ' ':
            try:
                value = value[:len(value) - 1]
            except:
                value = value
    elif callback_q.data == '=':
        try:
            value = calcRound(value, userStorage[chat_id].grade_value)
        except:
            value = 'Mistake'
    else:
        value += data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if (value != old_value and value != ' ') or ('0' != old_value and value == ' '):
        if value == ' ':
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text='0', reply_markup=kb.roundCircle())
            old_value = '0'
        else:
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text=value, reply_markup=kb.roundCircle())
            old_value = value
        if old_value == 'Mistake':
            value = ' '
    userStorageUpdate(chat_id, value, old_value, grade_value)


def calcRound(param, grade_value):
    values = param.split("*")
    res = 0
    constanta = grade_value
    pi = 3.141592653
    if len(values) == 1:
        a = values[0]
        res1 = float(a)
        res = ((res1 / 1000) ** 2) * pi / 4 * int(constanta)
        return '%.3f' % res + ' kg./m.'
    elif len(values) == 2:
        res1 = float(values[0])
        res2 = float(values[1])
        res = ((res1 / 1000) ** 2) * pi / 4 * int(constanta) * res2
        return '%.3f' % res + ' kg.'
    elif len(values) == 3:
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = float(values[2])
        if res2 < res1 and res2 != res1 and (res1 - res2) != 0:
            res = (((res1 / 1000) ** 2) - ((res2 / 1000) ** 2)) * pi / 4 * int(constanta) * res3
            return '%.3f' % res + ' kg.'
        elif res3 == 1:
            return '%.3f' % res + ' kg./m.'
        else:
            return 'Mistake, with the entered parameters, the inner diameter is missing'

    else:
        return ('Mistake. Try again')


@dp.callback_query_handler(state='B')
async def sphereCalc(callback_q: types.CallbackQuery):
    global grades
    new_data = get_new_data()
    chat_id = callback_q.from_user.id
    value = userStorage[chat_id].value
    old_value = userStorage[chat_id].old_value
    grade_value = 0
    grades = new_data
    for item in grades:
        if callback_q.data in item:
            grade_value = item[callback_q.data][0]['grade_value']
    if callback_q.data == 'Main' or callback_q.data == 'Main menu' \
            or callback_q.data == '/menu' or callback_q.data == '/start' \
            or callback_q.data == '/restart' or callback_q.data == 'Главное меню':
        chat_id = callback_q.from_user.id
        state = dp.current_state(user=chat_id)
        await state.set_state(MyStates.all()[4])
    elif callback_q.data == 'Hide keyboard':
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='Keyboard hidden. To open press Menu',
                               reply_markup=types.ReplyKeyboardRemove())
    elif callback_q.data == 'All metals':
        chat_id = callback_q.from_user.id
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='All metals',
                               reply_markup=kb.allMetals())
    elif callback_q.data == 'All grades':
        await bot.answer_callback_query(callback_q.id, text='This is operation manual')

    data = callback_q.data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if callback_q.data == ' ':
        pass
    elif callback_q.data == 'C':
        value = ' '
    elif callback_q.data == 'Ø':
        value = ' '

    elif callback_q.data == '<=':
        if value != ' ':
            try:
                value = value[:len(value) - 1]
            except:
                value = value
    elif callback_q.data == '=':
        try:
            value = calcSphere(value, userStorage[chat_id].grade_value)
        except:
            value = 'Mistake'
    else:
        value += data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if (value != old_value and value != ' ') or ('0' != old_value and value == ' '):
        if value == ' ':
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text='0', reply_markup=kb.roundCircle())
            old_value = '0'
        else:
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text=value, reply_markup=kb.roundCircle())
            old_value = value
        if old_value == 'Mistake':
            value = ' '
    userStorageUpdate(chat_id, value, old_value, grade_value)


def calcSphere(param, grade_value):
    values = param.split("*")
    # res = 0
    const = 1.333333333333333333333
    constanta = grade_value
    pi = 3.141592653
    if len(values) == 1:
        res1 = float(values[0])
        res = (const * pi * (((res1 / 2) ** 3) / 1000000000)) * int(constanta)
        v = (const * pi * (((res1 / 2) ** 3) / 1000))
        s = ((res1 / 2) ** 2) * pi
        return 'Weight - ' + '%.3f' % res + ' kg.\n' + 'Volume - ' + str('%.3f' % v) + ' cm3\n' + 'Square - ' + str(
            '%.3f' % s) + ' mm2'
    else:
        return ('Mistake. Try again')


@dp.callback_query_handler(state='C')
async def beamCalc(callback_q: types.CallbackQuery):
    global grades
    new_data = get_new_data()
    chat_id = callback_q.from_user.id
    value = userStorage[chat_id].value
    old_value = userStorage[chat_id].old_value
    grade_value = 0
    grades = new_data
    for item in grades:
        if callback_q.data in item:
            grade_value = item[callback_q.data][0]['grade_value']
    if callback_q.data == 'Main' or callback_q.data == 'Main menu' \
            or callback_q.data == '/menu' or callback_q.data == '/start' \
            or callback_q.data == '/restart' or callback_q.data == 'Главное меню' \
            or callback_q.data == 'Expand keyboard':
        chat_id = callback_q.from_user.id
        state = dp.current_state(user=chat_id)
        await state.set_state(MyStates.all()[4])
        await bot.answer_callback_query(callback_q.id, text=callback_q.data)
    elif callback_q.data == 'Hide keyboard':
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='Keyboard hidden. To open press Menu',
                               reply_markup=types.ReplyKeyboardRemove())
    elif callback_q.data == 'All metals':
        # elif callback_q.data in metalls:
        chat_id = callback_q.from_user.id
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='All metals',
                               reply_markup=kb.allMetals())
    elif callback_q.data == 'All grades':
        # await bot.answer_callback_query(callback_q.id, text=callback_q.data)
        await bot.answer_callback_query(callback_q.id, text='This is operation manual')

    data = callback_q.data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if callback_q.data == ' ':
        pass
    elif callback_q.data == 'C':
        value = ' '
    elif callback_q.data == 'H':
        value = ' '

    elif callback_q.data == '<=':
        if value != ' ':
            try:
                value = value[:len(value) - 1]
            except:
                value = value
    elif callback_q.data == '=':
        try:
            value = calcBeam(value, userStorage[chat_id].grade_value)
        except:
            value = 'Mistake'
    else:
        value += data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if (value != old_value and value != ' ') or ('0' != old_value and value == ' '):
        if value == ' ':
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text='0', reply_markup=kb.beam())
            old_value = '0'

        else:
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text=value, reply_markup=kb.beam())
            old_value = value
        if old_value == 'Mistake':
            value = ' '
    userStorageUpdate(chat_id, value, old_value, grade_value)


# Функция обработки данных балки:
def calcBeam(param, grade_value):
    values = param.split("*")
    res = 0
    constanta = grade_value
    # Для длины 1 м.
    if len(values) == 4:
        k = 1.05
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = float(values[2])
        res4 = float(values[3])
        res = ((((res1 - (res4 * 2)) / 1000) * (res3 / 1000))
               + (((res2 / 1000) * (res4 / 1000)) * 2)) * int(constanta) * k
        return '%.3f' % res + ' кг./м.'
    # Для длины больше 1 м.
    elif len(values) == 5:
        k = 1.05
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = float(values[2])
        res4 = float(values[3])
        res5 = float(values[4])
        res = ((((res1 - (res4 * 2)) / 1000) * (res3 / 1000))
               + (((res2 / 1000) * (res4 / 1000)) * 2)) * int(constanta) * k * res5
        return '%.3f' % res + ' кг./м.'
    else:
        return ('Mistake. Try again')


@dp.callback_query_handler(state='D')
async def channelCalc(callback_q: types.CallbackQuery):
    global grades
    new_data = get_new_data()
    chat_id = callback_q.from_user.id
    value = userStorage[chat_id].value
    old_value = userStorage[chat_id].old_value
    grade_value = 0
    grades = new_data
    for item in grades:
        if callback_q.data in item:
            grade_value = item[callback_q.data][0]['grade_value']
    if callback_q.data == 'Main' or callback_q.data == 'Main menu' \
            or callback_q.data == '/menu' or callback_q.data == '/start' \
            or callback_q.data == '/restart' or callback_q.data == 'Главное меню' \
            or callback_q.data == 'Expand keyboard':
        chat_id = callback_q.from_user.id
        state = dp.current_state(user=chat_id)
        await state.set_state(MyStates.all()[4])
        await bot.answer_callback_query(callback_q.id, text=callback_q.data)
    elif callback_q.data == 'Hide keyboard':
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='Keyboard hidden. To open press Menu',
                               reply_markup=types.ReplyKeyboardRemove())
    elif callback_q.data == 'All metals':
        # elif callback_q.data in metalls:
        chat_id = callback_q.from_user.id
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='All metals',
                               reply_markup=kb.allMetals())
    elif callback_q.data == 'All grades':
        await bot.answer_callback_query(callback_q.id, text='This is operation manual')

    data = callback_q.data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if callback_q.data == ' ':
        pass
    elif callback_q.data == 'C':
        value = ' '
    elif callback_q.data == 'H':
        value = ' '

    elif callback_q.data == '<=':
        if value != ' ':
            try:
                value = value[:len(value) - 1]
            except:
                value = value
    elif callback_q.data == '=':
        try:
            value = calcChannel(value, userStorage[chat_id].grade_value)
        except:
            value = 'Mistake'
    else:
        value += data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if (value != old_value and value != ' ') or ('0' != old_value and value == ' '):
        if value == ' ':
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text='0', reply_markup=kb.beam())
            old_value = '0'

        else:
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text=value, reply_markup=kb.beam())
            old_value = value
        if old_value == 'Mistake':
            value = ' '
    userStorageUpdate(chat_id, value, old_value, grade_value)


# Функция обработки данных балки:
def calcChannel(param, grade_value):
    values = param.split("*")
    res = 0
    constanta = grade_value
    # Для длины 1 м.
    if len(values) == 3:
        # k = 1.014
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = float(values[2])
        res = (((res1 / 1000) * (res3 / 1000)) + ((((res2 - res3) / 1000) * (res3 / 1000)) * 2)) * int(constanta)
        return '%.3f' % res + ' кг./м.'
    # Для длины больше 1 м.
    elif len(values) == 4:
        # k = 1.014
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = float(values[2])
        res4 = float(values[3])
        res = (((res1 / 1000) * (res3 / 1000))
               + ((((res2 - res3) / 1000) * (res4 / 1000)) * 2)) * int(constanta)
        return '%.3f' % res + ' кг./м.'
    elif len(values) == 5:
        # k = 1.014
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = float(values[2])
        res4 = float(values[3])
        res5 = float(values[4])
        res = (((res1 / 1000) * (res3 / 1000))
               + ((((res2 - res3) / 1000) * (res4 / 1000)) * 2)) * int(constanta) * res5
        return '%.3f' % res + ' кг.'
    else:
        return ('Mistake. Try again')


@dp.callback_query_handler(state='E')
async def cornerCalc(callback_q: types.CallbackQuery):
    global grades
    new_data = get_new_data()
    chat_id = callback_q.from_user.id
    value = userStorage[chat_id].value
    old_value = userStorage[chat_id].old_value
    grade_value = 0
    grades = new_data
    for item in grades:
        if callback_q.data in item:
            grade_value = item[callback_q.data][0]['grade_value']
    if callback_q.data == 'Main' or callback_q.data == 'Main menu' \
            or callback_q.data == '/menu' or callback_q.data == '/start' \
            or callback_q.data == '/restart' or callback_q.data == 'Главное меню' \
            or callback_q.data == 'Expand keyboard':
        chat_id = callback_q.from_user.id
        state = dp.current_state(user=chat_id)
        await state.set_state(MyStates.all()[4])
        await bot.answer_callback_query(callback_q.id, text=callback_q.data)
    elif callback_q.data == 'Hide keyboard':
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='Keyboard hidden. To open press Menu',
                               reply_markup=types.ReplyKeyboardRemove())
    elif callback_q.data == 'All metals':
        # elif callback_q.data in metalls:
        chat_id = callback_q.from_user.id
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='All metals',
                               reply_markup=kb.allMetals())
    elif callback_q.data == 'All grades':
        await bot.answer_callback_query(callback_q.id, text='This is operation manual')

    data = callback_q.data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if callback_q.data == ' ':
        pass
    elif callback_q.data == 'C':
        value = ' '
    elif callback_q.data == 'H':
        value = ' '

    elif callback_q.data == '<=':
        if value != ' ':
            try:
                value = value[:len(value) - 1]
            except:
                value = value
    elif callback_q.data == '=':
        try:
            value = calcCorner(value, userStorage[chat_id].grade_value)
        except:
            value = 'Mistake'
    else:
        value += data
    if (value != old_value and value != ' ') or ('0' != old_value and value == ' '):
        if value == ' ':
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text='0', reply_markup=kb.corner())
            old_value = '0'

        else:
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text=value, reply_markup=kb.corner())
            old_value = value
        if old_value == 'Mistake':
            value = ' '
    userStorageUpdate(chat_id, value, old_value, grade_value)


# Функция обработки данных уголка:
def calcCorner(param, grade_value):
    values = param.split("*")
    res = 0
    constanta = grade_value
    # Для длины 1 м.
    if len(values) == 2:
        # k = 1.014
        res1 = float(values[0])
        res2 = float(values[1])
        res = (((res1 / 1000) * (res2 / 1000)) + ((res1 - res2) / 1000)) * int(constanta)
        return '%.3f' % res + ' кг./м.'
    elif len(values) == 3:
        # k = 1.014
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = float(values[2])
        res = (((res1 / 1000) * (res3 / 1000)) + ((res2 - res3) / 1000)) * int(constanta)
        return '%.3f' % res + ' кг./м.'
    # Для длины больше 1 м.
    elif len(values) == 4:
        # k = 1.014
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = float(values[2])
        res4 = float(values[3])
        res = (((res1 / 1000) * (res3 / 1000)) + ((res2 - res3) / 1000)) * int(constanta) * res4
        return '%.3f' % res + ' кг.'
    else:
        return ('Mistake. Try again')


@dp.callback_query_handler(state='F')
async def hexagonCalc(callback_q: types.CallbackQuery):
    global grades
    new_data = get_new_data()
    chat_id = callback_q.from_user.id
    value = userStorage[chat_id].value
    old_value = userStorage[chat_id].old_value
    grade_value = 0
    grades = new_data
    for item in grades:
        if callback_q.data in item:
            grade_value = item[callback_q.data][0]['grade_value']
    if callback_q.data == 'Main' or callback_q.data == 'Main menu' \
            or callback_q.data == '/menu' or callback_q.data == '/start' \
            or callback_q.data == '/restart' or callback_q.data == 'Главное меню' \
            or callback_q.data == 'Expand keyboard':
        chat_id = callback_q.from_user.id
        state = dp.current_state(user=chat_id)
        await state.set_state(MyStates.all()[4])
        await bot.answer_callback_query(callback_q.id, text=callback_q.data)
    elif callback_q.data == 'Hide keyboard':
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='Keyboard hidden. To open press Menu',
                               reply_markup=types.ReplyKeyboardRemove())
    elif callback_q.data == 'All metals':
        # elif callback_q.data in metalls:
        chat_id = callback_q.from_user.id
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='All metals',
                               reply_markup=kb.allMetals())
    elif callback_q.data == 'All grades':
        await bot.answer_callback_query(callback_q.id, text='This is operation manual')

    data = callback_q.data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if callback_q.data == ' ':
        pass
    elif callback_q.data == 'C':
        value = ' '
    elif callback_q.data == 'H':
        value = ' '

    elif callback_q.data == '<=':
        if value != ' ':
            try:
                value = value[:len(value) - 1]
            except:
                value = value
    elif callback_q.data == '=':
        try:
            value = calcHexagon(value, userStorage[chat_id].grade_value)
        except:
            value = 'Mistake'
    else:
        value += data
    if (value != old_value and value != ' ') or ('0' != old_value and value == ' '):
        if value == ' ':
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text='0', reply_markup=kb.corner())
            old_value = '0'

        else:
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text=value, reply_markup=kb.corner())
            old_value = value
        if old_value == 'Mistake':
            value = ' '
    userStorageUpdate(chat_id, value, old_value, grade_value)


# Функция обработки данных уголка:
def calcHexagon(param, grade_value):
    values = param.split("*")
    res = 0
    constanta = grade_value
    # Для длины 1 м.
    if len(values) == 2:
        # k = 1.014
        res1 = float(values[0])
        res2 = float(values[1])
        res = (((res1 / 1000) * (res2 / 1000)) + ((res1 - res2) / 1000)) * int(constanta)
        return '%.3f' % res + ' кг./м.'
    elif len(values) == 3:
        # k = 1.014
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = float(values[2])
        res = (((res1 / 1000) * (res3 / 1000)) + ((res2 - res3) / 1000)) * int(constanta)
        return '%.3f' % res + ' кг./м.'
    # Для длины больше 1 м.
    elif len(values) == 4:
        # k = 1.014
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = float(values[2])
        res4 = float(values[3])
        res = (((res1 / 1000) * (res3 / 1000)) + ((res2 - res3) / 1000)) * int(constanta) * res4
        return '%.3f' % res + ' кг.'
    else:
        return ('Mistake. Try again')


@dp.callback_query_handler(state='G')
async def armatureCalc(callback_q: types.CallbackQuery):
    global grades
    new_data = get_new_data()
    chat_id = callback_q.from_user.id
    value = userStorage[chat_id].value
    old_value = userStorage[chat_id].old_value
    grade_value = 0
    grades = new_data
    for item in grades:
        if callback_q.data in item:
            grade_value = item[callback_q.data][0]['grade_value']
    if callback_q.data == 'Main' or callback_q.data == 'Main menu' \
            or callback_q.data == '/menu' or callback_q.data == '/start' \
            or callback_q.data == '/restart' or callback_q.data == 'Главное меню' \
            or callback_q.data == 'Expand keyboard':
        chat_id = callback_q.from_user.id
        state = dp.current_state(user=chat_id)
        await state.set_state(MyStates.all()[4])
        await bot.answer_callback_query(callback_q.id, text=callback_q.data)
    elif callback_q.data == 'Hide keyboard':
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='Keyboard hidden. To open press Menu',
                               reply_markup=types.ReplyKeyboardRemove())
    elif callback_q.data == 'All metals':
        # elif callback_q.data in metalls:
        chat_id = callback_q.from_user.id
        await bot.send_message(chat_id=callback_q.from_user.id,
                               text='All metals',
                               reply_markup=kb.allMetals())
    elif callback_q.data == 'All grades':
        # await bot.answer_callback_query(callback_q.id, text=callback_q.data)
        await bot.answer_callback_query(callback_q.id, text='This is operation manual')

    data = callback_q.data
    userStorageUpdate(chat_id, value, old_value, grade_value)
    if callback_q.data == ' ':
        pass
    elif callback_q.data == 'C':
        value = ' '
    elif callback_q.data == 'H':
        value = ' '

    elif callback_q.data == '<=':
        if value != ' ':
            try:
                value = value[:len(value) - 1]
            except:
                value = value
    elif callback_q.data == '=':
        try:
            value = calcArmature(value, userStorage[chat_id].grade_value)
        except:
            value = 'Mistake'
    else:
        value += data
    if (value != old_value and value != ' ') or ('0' != old_value and value == ' '):
        if value == ' ':
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text='0', reply_markup=kb.corner())
            old_value = '0'

        else:
            await bot.edit_message_text(chat_id=callback_q.message.chat.id, message_id=callback_q.message.message_id,
                                        text=value, reply_markup=kb.corner())
            old_value = value
        if old_value == 'Mistake':
            value = ' '
    userStorageUpdate(chat_id, value, old_value, grade_value)


# Функция обработки данных уголка:
def calcArmature(param, grade_value):
    values = param.split("*")
    res = 0
    constanta = grade_value
    # Для длины 1 м.
    if len(values) == 2:
        # k = 1.014
        res1 = float(values[0])
        res2 = float(values[1])
        res = (((res1 / 1000) * (res2 / 1000)) + ((res1 - res2) / 1000)) * int(constanta)
        return '%.3f' % res + ' кг./м.'
    elif len(values) == 3:
        # k = 1.014
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = float(values[2])
        res = (((res1 / 1000) * (res3 / 1000)) + ((res2 - res3) / 1000)) * int(constanta)
        return '%.3f' % res + ' кг./м.'
    # Для длины больше 1 м.
    elif len(values) == 4:
        # k = 1.014
        res1 = float(values[0])
        res2 = float(values[1])
        res3 = float(values[2])
        res4 = float(values[3])
        res = (((res1 / 1000) * (res3 / 1000)) + ((res2 - res3) / 1000)) * int(constanta) * res4
        return '%.3f' % res + ' кг.'
    else:
        return ('Mistake. Try again')


@dp.message_handler()
async def default(message: types.Message):
    chat_id = message.from_user.id
    userStorage[chat_id] = Storage()
    user = get_user_by_id(message.from_user.id)
    print(user)
    if chat_id not in USERS.keys():
        USERS.update({chat_id: User(chat_id)})
        state = dp.current_state(user=chat_id)
        await state.set_state(MyStates.all()[1])
        print(await state.get_state())
    if (len(user) == 0):
        await bot.send_message(chat_id=message.from_user.id, text=f'{MESSAGES["start"]}\n{MESSAGES["name"]}')
    else:
        USERS.update({chat_id: User(chat_id)})
        state = dp.current_state(user=chat_id)
        await state.set_state(MyStates.all()[4])
        await menu(message)


# Переход между клавиатурами меню

@dp.message_handler(state='*')
async def all(message: types.Message):
    chat_id = message.from_user.id
    state = dp.current_state(user=chat_id)
    await state.set_state(MyStates.all()[4])
    await menu(message)


# Данные для внесения в базу данных
@dp.message_handler()
async def recording(message: types.Message):
    print(message)
    user = get_user_by_id(message.from_user.id)
    if len(user) == 0:
        insert_user({"UserID": message.from_user.id, "Firstname": message.from_user.first_name,
                     "Lastname": message.from_user.last_name, "Birthday": None,
                     "Phone": None, "Mail": None})
    insert_message({"UserID": message.from_user.id, "TextMessage": message.text})
    print('\n', 'User ID:', message.from_user.id, '\n',
          'User name:', message.from_user.first_name,
          message.from_user.last_name, '\n',
          'Wrote:', message.text, '\n',
          'ChatID:', message.message_id, '\n',
          'Language:', message.from_user.language_code)
    users.update({message.from_user.id: message.from_user.first_name})


if __name__ == '__main__':
    data = get_round_pipe_data_analysis()
    # round_pipe_data_preparation()
    if not data.empty:
        round_pipe_data_preparation()
        forecast.train_all_models(data)
        # round_pipe_data_preparation()
    else:
        # print("Нет данных для обучения моделей при запуске.")
        print("No data available for training the models at startup.")
    from aiogram import executor

    executor.start_polling(dp, skip_updates=False)
