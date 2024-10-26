from aiogram import types

from database import (
    get_round_pipe_data_analysis,
    get_profile_pipe_data_analysis,
    get_round_bar_data_analysis,
    get_square_data_analysis,
    get_rectangle_data_analysis,
    get_round_bar_forging_data_analysis,
    get_square_forging_data_analysis,
    get_rectangle_forging_data_analysis,
    get_ring_forging_data_analysis
)
from ml import (create_forecast_chart, forecast)


async def cmd_show_round_pipe_forecast(callback_query: types.CallbackQuery):
    """
    Logic for displaying forecast for round pipes.
    """
    # Get message object from callback_query
    message = callback_query.message

    # Retrieve data for analysis
    data = get_round_pipe_data_analysis()

    if data.empty:
        await message.reply("No data available for analysis.")
        return

    # Check if the model is trained
    if forecast.regressor is None:
        await message.reply("The regressor model is not trained.")
        return

    # Forecast and send the chart to the user
    top_products = data.nlargest(10, 'count').copy()

    if top_products.empty:
        await message.reply("Insufficient data to generate a forecast.")
        return

    # Predict weight for selected products
    try:
        X_new = top_products[['nomenclature', 'material', 'diameter', 'wall_thickness', 'count']]
        predictions = forecast.predict_weight(X_new)
        top_products['predicted_weight'] = predictions
    except Exception as e:
        await message.reply(f"Error during weight prediction: {e}")
        return

    # Round predicted values to 3 decimal places
    top_products['predicted_weight'] = top_products['predicted_weight'].round(3)

    # Create chart for selected products
    chart = create_forecast_chart(top_products)

    if chart:
        # Send the chart to the user using the Bot object
        with open(chart, 'rb') as photo:
            await message.bot.send_photo(chat_id=message.chat.id, photo=photo,
                                         caption="Forecast of the most in-demand products")
    else:
        await message.reply("Failed to create the forecast chart.")


# Similar methods for other product types (mock)

async def cmd_show_profile_pipe_forecast(message):
    data = get_profile_pipe_data_analysis()
    # Logic similar to cmd_show_round_pipe_forecast


async def cmd_show_round_bar_forecast(message):
    data = get_round_bar_data_analysis()
    # Logic similar to cmd_show_round_pipe_forecast


async def cmd_show_square_forecast(message):
    data = get_square_data_analysis()
    # Logic similar to cmd_show_round_pipe_forecast


async def cmd_show_rectangle_forecast(message):
    data = get_square_data_analysis()
    # Logic similar to cmd_show_round_pipe_forecast


async def cmd_show_round_bar_forging_forecast(message):
    data = get_square_data_analysis()
    # Logic similar to cmd_show_round_pipe_forecast


async def cmd_show_square_forging_forecast(message):
    data = get_square_data_analysis()
    # Logic similar to cmd_show_round_pipe_forecast


async def cmd_show_rectangle_forging_forecast(message):
    data = get_square_data_analysis()
    # Logic similar to cmd_show_round_pipe_forecast


async def cmd_show_ring_forging_forecast(message):
    data = get_square_data_analysis()
    # Logic similar to cmd_show_round_pipe_forecast

# Russian language
# from aiogram import types
#
# from database import (
#     get_round_pipe_data_analysis,
#     get_profile_pipe_data_analysis,
#     get_round_bar_data_analysis,
#     get_square_data_analysis,
#     get_rectangle_data_analysis,
#     get_round_bar_forging_data_analysis,
#     get_square_forging_data_analysis,
#     get_rectangle_forging_data_analysis,
#     get_ring_forging_data_analysis
# )
# from ml import (create_forecast_chart, forecast)
#
#
# async def cmd_show_round_pipe_forecast(callback_query: types.CallbackQuery):
#     """
#     Логика отображения прогноза для круглой трубы.
#     """
#     # Получаем объект сообщения из callback_query
#     message = callback_query.message
#
#     # Получение данных для анализа
#     data = get_round_pipe_data_analysis()
#
#     if data.empty:
#         await message.reply("Нет данных для анализа.")
#         return
#
#     # Проверка обученности модели
#     if forecast.regressor is None:
#         await message.reply("Модель регрессора не обучена.")
#         return
#
#     # Прогноз и отправка графика пользователю
#     top_products = data.nlargest(10, 'count').copy()
#
#     if top_products.empty:
#         await message.reply("Недостаточно данных для формирования прогноза.")
#         return
#
#     # Прогноз веса для выбранных продуктов
#     try:
#         X_new = top_products[['nomenclature', 'material', 'diameter', 'wall_thickness', 'count']]
#         predictions = forecast.predict_weight(X_new)
#         top_products['predicted_weight'] = predictions
#     except Exception as e:
#         await message.reply(f"Ошибка при прогнозировании веса: {e}")
#         return
#
#     # Округляем предсказанные значения до 3 знаков после запятой
#     top_products['predicted_weight'] = top_products['predicted_weight'].round(3)
#
#     # Создание графика для выбранных продуктов
#     chart = create_forecast_chart(top_products)
#
#     if chart:
#         # Отправка графика пользователю с помощью объекта Bot
#         with open(chart, 'rb') as photo:
#             await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption="Прогноз наиболее востребованных продуктов")
#     else:
#         await message.reply("Не удалось создать график прогноза.")
#
# # Аналогичные методы для других типов продуктов (mock)
#
# async def cmd_show_profile_pipe_forecast(message):
#     data = get_profile_pipe_data_analysis()
#     # Логика аналогична cmd_show_round_pipe_forecast
#
#
# async def cmd_show_round_bar_forecast(message):
#     data = get_round_bar_data_analysis()
#     # Логика аналогична cmd_show_round_pipe_forecast
#
#
# async def cmd_show_square_forecast(message):
#     data = get_square_data_analysis()
#     # Логика аналогична cmd_show_round_pipe_forecast
#
#
# async def cmd_show_rectangle_forecast(message):
#     data = get_square_data_analysis()
#     # Логика аналогична cmd_show_round_pipe_forecast
#
#
# async def cmd_show_round_bar_forging_forecast(message):
#     data = get_square_data_analysis()
#     # Логика аналогична cmd_show_round_pipe_forecast
#
#
# async def cmd_show_square_forging_forecast(message):
#     data = get_square_data_analysis()
#     # Логика аналогична cmd_show_round_pipe_forecast
#
#
# async def cmd_show_rectangle_forging_forecast(message):
#     data = get_square_data_analysis()
#     # Логика аналогична cmd_show_round_pipe_forecast
#
#
# async def cmd_show_ring_forging_forecast(message):
#     data = get_square_data_analysis()
#     # Логика аналогична cmd_show_round_pipe_forecast
