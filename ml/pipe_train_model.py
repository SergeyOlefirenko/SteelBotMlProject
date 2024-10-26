from database import (
    get_user_by_id,
    insert_user,
    insert_message,
    insert_result,
    get_user_actions_by_id,
    update_round_pipe_data_analysis,
    get_round_pipe_data_analysis,
    get_nomenclature_id,
    update_time_table_data,
)
from ml import forecast


def analyze_data(result):
    try:
        # Process a single record
        if 'dimensions' not in result:
            print("Column 'dimensions' is missing.")
            return

        # Extract diameter and wall thickness from the string representation of dimensions
        dimensions_parts = result['dimensions'].split('x')
        if len(dimensions_parts) >= 3:
            diameter = dimensions_parts[0].replace('Ø', '').strip()
            wall_thickness = dimensions_parts[1].strip()
            length = dimensions_parts[2].replace('m', '').strip() if len(dimensions_parts) > 2 else "1"

            material = result['material'].strip()
            nomenclature = result['nomenclature']

            try:
                length_value = float(length)
            except ValueError:
                length_value = 1.0

            try:
                weight_value = float(result['weight'].replace('kg.', '').strip())
            except ValueError:
                weight_value = 0.0

            # Round weight value to 3 decimal places
            weight_value = round(weight_value, 3)

            # Get nomenclature_id
            nomenclature_id = get_nomenclature_id(nomenclature, diameter, wall_thickness, material)

            # Update time_table_data based on timestamp and count=1
            timestamp = result['timestamp']
            count = 1  # Each record in results represents 1 count
            update_time_table_data(nomenclature_id, timestamp, count)

            # Prepare data for round_pipe_data_analysis
            data_entry = {
                'nomenclature': nomenclature,
                'diameter': float(diameter),
                'wall_thickness': float(wall_thickness),
                'material': material,
                'nomenclature_id': nomenclature_id,
                'length': length_value,  # Store as a number
                'weight': weight_value,  # Rounded weight value
                'count': count
            }

            print(f"Inserting/updating data in round_pipe_data_analysis: {data_entry}")
            update_round_pipe_data_analysis(data_entry)

        else:
            print("Invalid dimensions format.")
            return

        print("Analysis data successfully updated in the database.")

        # Train the model on updated data
        train_model()

    except Exception as e:
        print(f"Error during data analysis: {e}")  # Print error


def train_model():
    data = get_round_pipe_data_analysis()

    if data.empty:
        print("No data available to train the model.")
        return

    # Data transformation
    if data['length'].dtype == object:
        data['length'] = data['length'].astype(float)
    if data['weight'].dtype == object:
        data['weight'] = data['weight'].astype(float)

    # Train the model (including classifiers)
    forecast.train_all_models(data)

# Russian language
# from database import (get_user_by_id, insert_user, insert_message, insert_result, get_user_actions_by_id,
#                       update_round_pipe_data_analysis,
#                       get_round_pipe_data_analysis,
#                       get_nomenclature_id,
#                       update_time_table_data,
#                       )
# from ml import forecast
#
#
# def analyze_data(result):
#     try:
#         # Обработка одной записи
#         if 'dimensions' not in result:
#             print("Отсутствует колонка 'dimensions'.")
#             return
#
#         # Извлекаем диаметр и толщину стенки из строкового представления размеров
#         dimensions_parts = result['dimensions'].split('x')
#         if len(dimensions_parts) >= 3:
#             diameter = dimensions_parts[0].replace('Ø', '').strip()
#             wall_thickness = dimensions_parts[1].strip()
#             length = dimensions_parts[2].replace('m', '').strip() if len(dimensions_parts) > 2 else "1"
#
#             material = result['material'].strip()
#             nomenclature = result['nomenclature']
#
#             try:
#                 length_value = float(length)
#             except ValueError:
#                 length_value = 1.0
#
#             try:
#                 weight_value = float(result['weight'].replace('kg.', '').strip())
#             except ValueError:
#                 weight_value = 0.0
#
#             # Округляем значение веса до 3 знаков после запятой
#             weight_value = round(weight_value, 3)
#
#             # Получение nomenclature_id
#             nomenclature_id = get_nomenclature_id(nomenclature, diameter, wall_thickness, material)
#
#             # Обновление time_table_data на основе timestamp и count=1
#             timestamp = result['timestamp']
#             count = 1  # Каждая запись в results представляет 1 count
#             update_time_table_data(nomenclature_id, timestamp, count)
#
#             # Подготовка данных для round_pipe_data_analysis
#             data_entry = {
#                 'nomenclature': nomenclature,
#                 'diameter': float(diameter),
#                 'wall_thickness': float(wall_thickness),
#                 'material': material,
#                 'nomenclature_id': nomenclature_id,
#                 'length': length_value,  # Храним как число
#                 'weight': weight_value,  # Округленное значение веса
#                 'count': count
#             }
#
#             print(f"Вставляем/обновляем данные в round_pipe_data_analysis: {data_entry}")
#             update_round_pipe_data_analysis(data_entry)
#
#         else:
#             print("Неверный формат dimensions.")
#             return
#
#         print("Данные анализа успешно обновлены в базе данных.")
#
#         # Обучение модели на обновленных данных
#         train_model()
#
#     except Exception as e:
#         print(f"Ошибка при анализе данных: {e}")  # Вывод ошибки
#
#
# def train_model():
#     data = get_round_pipe_data_analysis()
#
#     if data.empty:
#         print("Нет данных для обучения модели.")
#         return
#
#     # Преобразование данных
#     if data['length'].dtype == object:
#         data['length'] = data['length'].astype(float)
#     if data['weight'].dtype == object:
#         data['weight'] = data['weight'].astype(float)
#
#     # Обучение модели (включая классификаторы)
#     forecast.train_all_models(data)
