# bot.py
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
)
from main import log_result, analyze_data, forecast, get_data_analysis
from visualization import create_forecast_chart
import pandas as pd
from io import BytesIO

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# Функция для старта бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Show Forecast", callback_data='show_forecast')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)


# Функция для обработки нажатий кнопок
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    # Первоначальная клавиатура для выбора номенклатуры
    if data == 'show_forecast':
        keyboard = [
            [InlineKeyboardButton("Труба", callback_data='nomenclature_tube')],
            [InlineKeyboardButton("Круг", callback_data='nomenclature_circle')],
            [InlineKeyboardButton("Квадрат", callback_data='nomenclature_square')],
            [InlineKeyboardButton("Прямоугольник", callback_data='nomenclature_rectangle')],
            [InlineKeyboardButton("Лист", callback_data='nomenclature_sheet')],
            [InlineKeyboardButton("Полоса", callback_data='nomenclature_strip')],
            [InlineKeyboardButton("Балка", callback_data='nomenclature_beam')],
            [InlineKeyboardButton("Уголок", callback_data='nomenclature_angle')],
            [InlineKeyboardButton("Арматура", callback_data='nomenclature_rebar')],
            [InlineKeyboardButton("Швеллер", callback_data='nomenclature_channel')],
            [InlineKeyboardButton("Шестигранник", callback_data='nomenclature_hex')],
            [InlineKeyboardButton("Сферы/шар", callback_data='nomenclature_sphere')],
            [InlineKeyboardButton("Поковка", callback_data='nomenclature_forging')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Выберите номенклатуру:", reply_markup=reply_markup)

    # Обработка выбора номенклатуры "Труба"
    elif data.startswith('nomenclature_tube'):
        keyboard = [
            [InlineKeyboardButton("Круглая труба", callback_data='tube_round')],
            [InlineKeyboardButton("Профильная труба", callback_data='tube_profile')],
            [InlineKeyboardButton("Квадратная труба", callback_data='tube_square')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Выберите тип трубы:", reply_markup=reply_markup)

    # Аналогично обрабатываем другие номенклатуры
    elif data.startswith('nomenclature_circle'):
        keyboard = [
            [InlineKeyboardButton("Stainless Steel", callback_data='material_circle_Stainless Steel')],
            [InlineKeyboardButton("Carbon Steel", callback_data='material_circle_Carbon Steel')],
            # Добавьте остальные материалы по аналогии
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Выберите материал для Круга:", reply_markup=reply_markup)

    elif data.startswith('tube_round') or data.startswith('tube_profile') or data.startswith('tube_square'):
        # Извлекаем номенклатуру из callback_data
        if data.startswith('tube_round'):
            nomenclature = 'Круглая труба'
        elif data.startswith('tube_profile'):
            nomenclature = 'Профильная труба'
        elif data.startswith('tube_square'):
            nomenclature = 'Квадратная труба'

        # Переход к выбору материала
        keyboard = [
            [InlineKeyboardButton("Stainless Steel", callback_data=f'material_{nomenclature}_Stainless Steel')],
            [InlineKeyboardButton("Carbon Steel", callback_data=f'material_{nomenclature}_Carbon Steel')],
            [InlineKeyboardButton("High speed steel", callback_data=f'material_{nomenclature}_High speed steel')],
            [InlineKeyboardButton("Nickel heat resistant alloys",
                                  callback_data=f'material_{nomenclature}_Nickel heat resistant alloys')],
            [InlineKeyboardButton("Iron nickel heat resistant alloys",
                                  callback_data=f'material_{nomenclature}_Iron nickel heat resistant alloys')],
            [InlineKeyboardButton("Titanium alloys", callback_data=f'material_{nomenclature}_Titanium alloys')],
            [InlineKeyboardButton("Aluminium alloys", callback_data=f'material_{nomenclature}_Aluminium alloys')],
            [InlineKeyboardButton("Beryllium bronzes", callback_data=f'material_{nomenclature}_Beryllium bronzes')],
            [InlineKeyboardButton("Brass", callback_data=f'material_{nomenclature}_Brass')],
            [InlineKeyboardButton("Copper", callback_data=f'material_{nomenclature}_Copper')],
            [InlineKeyboardButton("Copper-nickel alloys",
                                  callback_data=f'material_{nomenclature}_Copper-nickel alloys')],
            [InlineKeyboardButton("Magnesium alloys", callback_data=f'material_{nomenclature}_Magnesium alloys')],
            [InlineKeyboardButton("Tin bronzes", callback_data=f'material_{nomenclature}_Tin bronzes')],
            [InlineKeyboardButton("Tinless bronzes", callback_data=f'material_{nomenclature}_Tinless bronzes')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=f"Выберите материал для {nomenclature}:", reply_markup=reply_markup)

    # Обработка выбора материала
    elif data.startswith('material_'):
        parts = data.split('_')
        if len(parts) >= 3:
            nomenclature = parts[1]
            material = '_'.join(parts[2:])  # Обработка материалов с пробелами

            # Получение данных для построения графика
            data_analysis = get_data_analysis()

            # Фильтрация данных по выбранным номенклатуре и материалу
            filtered_data = data_analysis[
                (data_analysis['nomenclature'] == nomenclature) &
                (data_analysis['material'] == material)
                ]

            if filtered_data.empty:
                await query.edit_message_text(text="Нет данных для отображения.")
                return

            # Подготовка данных для прогнозирования
            filtered_data['diameter'] = filtered_data['diameter'].astype(float)
            filtered_data['wall_thickness'] = filtered_data['wall_thickness'].astype(float)

            features = filtered_data[['diameter', 'wall_thickness', 'material']]

            try:
                # Прогнозирование
                predictions = forecast.predict(features)

                # Создание графика с использованием визуализации
                # Добавляем столбец с прогнозируемым спросом
                filtered_data = filtered_data.copy()
                filtered_data['predicted_count'] = predictions

                # Создаём график
                fig = px.bar(
                    filtered_data,
                    x='dimensions',
                    y=['count', 'predicted_count'],
                    title=f"Прогноз спроса для {nomenclature} из {material}",
                    labels={'value': 'Спрос', 'dimensions': 'Геометрические размеры'},
                    barmode='group',
                    color='dimensions',
                    opacity=0.6
                )

                # Конвертация графика в изображение
                img_bytes = fig.to_image(format="png")
                bio = BytesIO(img_bytes)
                bio.name = 'forecast.png'
                bio.seek(0)

                # Отправка графика пользователю
                await query.message.reply_photo(photo=bio)

                # Добавление кнопок под графиком
                keyboard = [
                    [InlineKeyboardButton("Change material", callback_data=f'change_material_{nomenclature}')],
                    [InlineKeyboardButton("New search", callback_data='new_search')]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                await query.message.reply_text(text="Что хотите сделать дальше?", reply_markup=reply_markup)

            except Exception as e:
                await query.edit_message_text(text=f"Ошибка при прогнозировании: {e}")

    # Обработка кнопки "Change material"
    elif data.startswith('change_material_'):
        nomenclature = data.split('_')[-1]
        keyboard = [
            [InlineKeyboardButton("Stainless Steel", callback_data=f'material_{nomenclature}_Stainless Steel')],
            [InlineKeyboardButton("Carbon Steel", callback_data=f'material_{nomenclature}_Carbon Steel')],
            [InlineKeyboardButton("High speed steel", callback_data=f'material_{nomenclature}_High speed steel')],
            [InlineKeyboardButton("Nickel heat resistant alloys",
                                  callback_data=f'material_{nomenclature}_Nickel heat resistant alloys')],
            [InlineKeyboardButton("Iron nickel heat resistant alloys",
                                  callback_data=f'material_{nomenclature}_Iron nickel heat resistant alloys')],
            [InlineKeyboardButton("Titanium alloys", callback_data=f'material_{nomenclature}_Titanium alloys')],
            [InlineKeyboardButton("Aluminium alloys", callback_data=f'material_{nomenclature}_Aluminium alloys')],
            [InlineKeyboardButton("Beryllium bronzes", callback_data=f'material_{nomenclature}_Beryllium bronzes')],
            [InlineKeyboardButton("Brass", callback_data=f'material_{nomenclature}_Brass')],
            [InlineKeyboardButton("Copper", callback_data=f'material_{nomenclature}_Copper')],
            [InlineKeyboardButton("Copper-nickel alloys",
                                  callback_data=f'material_{nomenclature}_Copper-nickel alloys')],
            [InlineKeyboardButton("Magnesium alloys", callback_data=f'material_{nomenclature}_Magnesium alloys')],
            [InlineKeyboardButton("Tin bronzes", callback_data=f'material_{nomenclature}_Tin bronzes')],
            [InlineKeyboardButton("Tinless bronzes", callback_data=f'material_{nomenclature}_Tinless bronzes')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=f"Выберите новый материал для {nomenclature}:", reply_markup=reply_markup)

    # Обработка кнопки "New search"
    elif data == 'new_search':
        keyboard = [
            [InlineKeyboardButton("Труба", callback_data='nomenclature_tube')],
            [InlineKeyboardButton("Круг", callback_data='nomenclature_circle')],
            [InlineKeyboardButton("Квадрат", callback_data='nomenclature_square')],
            [InlineKeyboardButton("Прямоугольник", callback_data='nomenclature_rectangle')],
            [InlineKeyboardButton("Лист", callback_data='nomenclature_sheet')],
            [InlineKeyboardButton("Полоса", callback_data='nomenclature_strip')],
            [InlineKeyboardButton("Балка", callback_data='nomenclature_beam')],
            [InlineKeyboardButton("Уголок", callback_data='nomenclature_angle')],
            [InlineKeyboardButton("Арматура", callback_data='nomenclature_rebar')],
            [InlineKeyboardButton("Швеллер", callback_data='nomenclature_channel')],
            [InlineKeyboardButton("Шестигранник", callback_data='nomenclature_hex')],
            [InlineKeyboardButton("Сферы/шар", callback_data='nomenclature_sphere')],
            [InlineKeyboardButton("Поковка", callback_data='nomenclature_forging')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Выберите номенклатуру:", reply_markup=reply_markup)

    # Обработка других номенклатур аналогично

    else:
        await query.edit_message_text(text="Неизвестная команда.")


# Функция для обработки команды /showforecast
async def show_forecast_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Труба", callback_data='nomenclature_tube')],
        [InlineKeyboardButton("Круг", callback_data='nomenclature_circle')],
        [InlineKeyboardButton("Квадрат", callback_data='nomenclature_square')],
        [InlineKeyboardButton("Прямоугольник", callback_data='nomenclature_rectangle')],
        [InlineKeyboardButton("Лист", callback_data='nomenclature_sheet')],
        [InlineKeyboardButton("Полоса", callback_data='nomenclature_strip')],
        [InlineKeyboardButton("Балка", callback_data='nomenclature_beam')],
        [InlineKeyboardButton("Уголок", callback_data='nomenclature_angle')],
        [InlineKeyboardButton("Арматура", callback_data='nomenclature_rebar')],
        [InlineKeyboardButton("Швеллер", callback_data='nomenclature_channel')],
        [InlineKeyboardButton("Шестигранник", callback_data='nomenclature_hex')],
        [InlineKeyboardButton("Сферы/шар", callback_data='nomenclature_sphere')],
        [InlineKeyboardButton("Поковка", callback_data='nomenclature_forging')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text="Выберите номенклатуру:", reply_markup=reply_markup)


# Функция для запуска бота
def main():
    application = ApplicationBuilder().token('YOUR_TELEGRAM_BOT_TOKEN').build()

    # Обработчики команд
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('showforecast', show_forecast_command))
    application.add_handler(CallbackQueryHandler(button))


