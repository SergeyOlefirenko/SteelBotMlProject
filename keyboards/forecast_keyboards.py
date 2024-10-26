from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Keyboard for selecting product category
def main_product_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton(text="Pipe", callback_data="category_pipe"),
        InlineKeyboardButton(text="Circle", callback_data="category_circle"),
        InlineKeyboardButton(text="Square/Rectangle", callback_data="category_square"),
        InlineKeyboardButton(text="Forging", callback_data="category_forging"),
        InlineKeyboardButton(text="Sheet/Strip", callback_data="category_sheet"),
        InlineKeyboardButton(text="Channel", callback_data="category_channel"),
        InlineKeyboardButton(text="Hexagon", callback_data="category_hexagon"),
        InlineKeyboardButton(text="Beam", callback_data="category_beam"),
        InlineKeyboardButton(text="Angle", callback_data="category_angle"),
        InlineKeyboardButton(text="Rebar", callback_data="category_rebar"),
        InlineKeyboardButton(text="Sphere/Ball", callback_data="category_sphere"),
    ]
    keyboard.add(*buttons)
    return keyboard


# Keyboard for selecting pipe type
def pipe_type_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton(text="Round", callback_data="pipe_round"),
        InlineKeyboardButton(text="Profile", callback_data="pipe_profile"),
    ]
    keyboard.add(*buttons)
    return keyboard


def square_rectangle_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton(text="Square", callback_data="Square"),
        InlineKeyboardButton(text="Rectangle", callback_data="Rectangle"),
    ]
    keyboard.add(*buttons)
    return keyboard


def forging_type_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton(text="Round Forging", callback_data="Round Forging"),
        InlineKeyboardButton(text="Square Forging", callback_data="Square Forging"),
        InlineKeyboardButton(text="Rectangular Forging", callback_data="Rectangular Forging"),
        InlineKeyboardButton(text="Ring", callback_data="Ring"),
    ]
    keyboard.add(*buttons)
    return keyboard

# Russian language
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#
#
# # Клавиатура для выбора категории продукта
# def main_product_keyboard():
#     keyboard = InlineKeyboardMarkup(row_width=2)
#     buttons = [
#         InlineKeyboardButton(text="Труба", callback_data="category_pipe"),
#         InlineKeyboardButton(text="Круг", callback_data="category_circle"),
#         InlineKeyboardButton(text="Квадрат/Прямоугольник", callback_data="category_square"),
#         InlineKeyboardButton(text="Поковка", callback_data="category_forging"),
#         InlineKeyboardButton(text="Лист/полоса", callback_data="category_sheet"),
#         InlineKeyboardButton(text="Швеллер", callback_data="category_channel"),
#         InlineKeyboardButton(text="Шестигранник", callback_data="category_hexagon"),
#         InlineKeyboardButton(text="Балка", callback_data="category_beam"),
#         InlineKeyboardButton(text="Уголок", callback_data="category_angle"),
#         InlineKeyboardButton(text="Арматура", callback_data="category_rebar"),
#         InlineKeyboardButton(text="Сфера/шар", callback_data="category_sphere"),
#     ]
#     keyboard.add(*buttons)
#     return keyboard
#
#
# # Клавиатура для выбора номенклатуры трубы
# def pipe_type_keyboard():
#     keyboard = InlineKeyboardMarkup(row_width=2)
#     buttons = [
#         InlineKeyboardButton(text="Круглая", callback_data="pipe_round"),
#         InlineKeyboardButton(text="Профильная", callback_data="pipe_profile"),
#     ]
#     keyboard.add(*buttons)
#     return keyboard
#
#
# def square_rectangle_keyboard():
#     keyboard = InlineKeyboardMarkup(row_width=2)
#     buttons = [
#         InlineKeyboardButton(text="Квадрат", callback_data="Квадрат"),
#         InlineKeyboardButton(text="Прямоугольник", callback_data="Прямоугольник"),
#     ]
#     keyboard.add(*buttons)
#     return keyboard
#
#
# def forging_type_keyboard():
#     keyboard = InlineKeyboardMarkup(row_width=2)
#     buttons = [
#         InlineKeyboardButton(text="Круглая поковка", callback_data="Круглая поковка"),
#         InlineKeyboardButton(text="Квадратная поковка", callback_data="Квадратная поковка"),
#         InlineKeyboardButton(text="Прямоугольная поковка", callback_data="Прямоугольная поковка"),
#         InlineKeyboardButton(text="Кольцо", callback_data="Кольцо"),
#     ]
#     keyboard.add(*buttons)
#     return keyboard
