import datetime
import pandas as pd
from pymongo import MongoClient

# Connecting to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # MongoDB port
# Creating or selecting a database
db = client['database']
# Creating collections
users_collection = db['Users']
messages_collection = db['Messages']
results_collection = db['results']
round_pipe_data_analysis_collection = db['round_pipe_data_analysis']
time_table_data_collection = db['time_table_data']  # New collection


# Functions for working with MongoDB

def insert_user(user):
    users_collection.insert_one(user)


def get_user_by_id(user_id):
    return users_collection.find_one({'UserID': user_id})


def update_user_by_id(user_id, text_message):
    users_collection.update_one({'UserID': user_id},
                                {'$set': {'TextMessage': text_message}})


def insert_message(message):
    messages_collection.insert_one(message)


def get_message_by_id(user_id):
    return messages_collection.find({'UserID': user_id})


def insert_result(result_data):
    """
    Inserts data into the results collection.
    """
    db.results.insert_one(result_data)


def get_user_actions_by_id(user_id):
    actions = list(db.results.find({'user_id': str(user_id)}))
    print(f"Retrieved actions for {user_id}: {actions}")  # Printing results
    return actions


def get_results():
    return list(results_collection.find())


###########################################################

def update_round_pipe_data_analysis(data_entry):
    """
    Updates or inserts a record into round_pipe_data_analysis.
    Increments count, length, and weight accordingly.
    """
    existing_entry = round_pipe_data_analysis_collection.find_one({
        'nomenclature_id': data_entry['nomenclature_id']
    })
    if existing_entry:
        # Retrieve current values
        current_length = existing_entry['length']  # Stored as a number
        current_weight = existing_entry['weight']  # Stored as a number

        # Update values
        new_length = current_length + data_entry['length']
        new_weight = current_weight + data_entry['weight']

        # Round new values to 3 decimal places
        new_length = round(new_length, 3)
        new_weight = round(new_weight, 3)

        round_pipe_data_analysis_collection.update_one(
            {'nomenclature_id': data_entry['nomenclature_id']},
            {
                '$inc': {'count': data_entry['count']},
                '$set': {
                    'length': new_length,
                    'weight': new_weight
                }
            }
        )
    else:
        # Insert a new record
        # Round 'length' and 'weight' values to 3 decimal places
        data_entry['length'] = round(data_entry['length'], 3)
        data_entry['weight'] = round(data_entry['weight'], 3)
        round_pipe_data_analysis_collection.insert_one(data_entry)


def clear_round_pipe_data_analysis():
    """
    Clears the round_pipe_data_analysis collection.
    """
    round_pipe_data_analysis_collection.delete_many({})


def get_round_pipe_data_analysis():
    """
    Retrieves data from round_pipe_data_analysis and returns it as a DataFrame.
    """
    data = pd.DataFrame(list(round_pipe_data_analysis_collection.find({}, {'_id': 0})))
    print("Retrieved analysis data:", data.head())
    return data


# Methods for working with time_table_data
def get_nomenclature_id(nomenclature, diameter, wall_thickness, material):
    """
    Retrieves or creates a unique nomenclature_id based on the combination of nomenclature, diameter, wall_thickness, and material.
    """
    # Searching for existing nomenclature_id in round_pipe_data_analysis
    existing = round_pipe_data_analysis_collection.find_one({
        'nomenclature': nomenclature,
        'diameter': float(diameter),
        'wall_thickness': float(wall_thickness),
        'material': material
    })
    if existing:
        return existing['nomenclature_id']
    else:
        # Generate a new nomenclature_id
        last_entry = round_pipe_data_analysis_collection.find_one(sort=[("nomenclature_id", -1)])
        new_id = last_entry['nomenclature_id'] + 1 if last_entry else 1
        # Insert a new record in round_pipe_data_analysis with zero values
        new_round_pipe_entry = {
            'nomenclature_id': new_id,
            'nomenclature': nomenclature,
            'diameter': float(diameter),
            'wall_thickness': float(wall_thickness),
            'material': material,
            'length': 0.0,  # Stored as a number
            'weight': 0.0,  # Stored as a number
            'count': 0
        }
        round_pipe_data_analysis_collection.insert_one(new_round_pipe_entry)
        # Insert a new record in time_table_data
        new_time_table_entry = {
            'nomenclature_id': new_id,
            'nomenclature': nomenclature,
            'material': material,
            'year': datetime.datetime.now().year,
            'january': 0,
            'february': 0,
            'march': 0,
            'april': 0,
            'may': 0,
            'jun': 0,
            'july': 0,
            'august': 0,
            'september': 0,
            'october': 0,
            'november': 0,
            'december': 0,
            'total_count': 0
        }
        time_table_data_collection.insert_one(new_time_table_entry)
        return new_id


def update_time_table_data(nomenclature_id, timestamp, count):
    """
    Updates a record in time_table_data based on nomenclature_id, timestamp, and count.
    """
    # Extracting year and month from timestamp
    year = timestamp.year
    month = timestamp.month
    month_mapping = {
        1: 'january',
        2: 'february',
        3: 'march',
        4: 'april',
        5: 'may',
        6: 'jun',
        7: 'july',
        8: 'august',
        9: 'september',
        10: 'october',
        11: 'november',
        12: 'december'
    }
    month_name = month_mapping.get(month)
    if month_name:
        # Updating the record in time_table_data
        query = {'nomenclature_id': nomenclature_id, 'year': year}
        update = {
            '$inc': {
                month_name: count,
                'total_count': count
            }
        }
        time_table_data_collection.update_one(query, update, upsert=True)
    else:
        print(f"Invalid month: {month}")


def get_profile_pipe_data_analysis():
    """
    Retrieves data from get_profile_pipe_data_analysis and returns it as a DataFrame.
    """
    # data = pd.DataFrame(list(get_profile_pipe_data_analysis_collection.find({}, {'_id': 0})))
    # print("Retrieved analysis data:", data.head())
    # return data


def get_round_bar_data_analysis():
    """
    Retrieves data from get_round_bar_data_analysis and returns it as a DataFrame.
    """
    # data = pd.DataFrame(list(get_round_bar_data_analysis_collection.find({}, {'_id': 0})))
    # print("Retrieved analysis data:", data.head())
    # return data


def get_square_data_analysis():
    """
    Retrieves data from get_square_data_analysis and returns it as a DataFrame.
    """
    # data = pd.DataFrame(list(get_square_data_analysis_collection.find({}, {'_id': 0})))
    # print("Retrieved analysis data:", data.head())
    # return data


def get_rectangle_data_analysis():
    """
    Retrieves data from get_rectangle_data_analysis and returns it as a DataFrame.
    """
    # data = pd.DataFrame(list(get_rectangle_data_analysis_collection.find({}, {'_id': 0})))
    # print("Retrieved analysis data:", data.head())
    # return data


def get_round_bar_forging_data_analysis():
    """
    Retrieves data from get_round_bar_forging_data_analysis and returns it as a DataFrame.
    """
    # data = pd.DataFrame(list(get_round_bar_forging_data_analysis_collection.find({}, {'_id': 0})))
    # print("Retrieved analysis data:", data.head())
    # return data


def get_square_forging_data_analysis():
    """
    Retrieves data from get_square_forging_data_analysis and returns it as a DataFrame.
    """
    # data = pd.DataFrame(list(get_square_forging_data_analysis_collection.find({}, {'_id': 0})))
    # print("Retrieved analysis data:", data.head())
    # return data


def get_rectangle_forging_data_analysis():
    """
    Retrieves data from get_rectangle_forging_data_analysis and returns it as a DataFrame.
    """
    # data = pd.DataFrame(list(get_rectangle_forging_data_analysis_collection.find({}, {'_id': 0})))
    # print("Retrieved analysis data:", data.head())
    # return data


def get_ring_forging_data_analysis():
    """
    Retrieves data from get_ring_forging_data_analysis and returns it as a DataFrame.
    """
    # data = pd.DataFrame(list(get_ring_forging_data_analysis_collection.find({}, {'_id': 0})))
    # print("Retrieved analysis data:", data.head())
    # return data

# Russian language
# import datetime
# import pandas as pd
# from pymongo import MongoClient
#
# # Подключение к MongoDB
# client = MongoClient('mongodb://localhost:27017/')  # порт MongoDB
# # Создание или выбор базы данных
# db = client['database']
# # Создание коллекций
# users_collection = db['Users']
# messages_collection = db['Messages']
# results_collection = db['results']
# round_pipe_data_analysis_collection = db['round_pipe_data_analysis']
# time_table_data_collection = db['time_table_data']  # Новая коллекция
#
#
# # Функции для работы с MongoDB
#
# def insert_user(user):
#     users_collection.insert_one(user)
#
#
# def get_user_by_id(user_id):
#     return users_collection.find_one({'UserID': user_id})
#
#
# def update_user_by_id(user_id, text_message):
#     users_collection.update_one({'UserID': user_id},
#                                 {'$set': {'TextMessage': text_message}})
#
#
# def insert_message(message):
#     messages_collection.insert_one(message)
#
#
# def get_message_by_id(user_id):
#     return messages_collection.find({'UserID': user_id})
#
#
# def insert_result(result_data):
#     """
#     Вставляет данные в коллекцию results.
#     """
#     db.results.insert_one(result_data)
#
#
# def get_user_actions_by_id(user_id):
#     actions = list(db.results.find({'user_id': str(user_id)}))
#     print(f"Полученные действия для {user_id}: {actions}")  # вывод результатов
#     return actions
#
#
# def get_results():
#     return list(results_collection.find())
#
#
# ###########################################################
#
# def update_round_pipe_data_analysis(data_entry):
#     """
#     Обновляет или вставляет запись в round_pipe_data_analysis.
#     Увеличивает count, length и weight соответствующим образом.
#     """
#     existing_entry = round_pipe_data_analysis_collection.find_one({
#         'nomenclature_id': data_entry['nomenclature_id']
#     })
#     if existing_entry:
#         # Извлекаем текущие значения
#         current_length = existing_entry['length']  # Храним как число
#         current_weight = existing_entry['weight']  # Храним как число
#
#         # Обновляем значения
#         new_length = current_length + data_entry['length']
#         new_weight = current_weight + data_entry['weight']
#
#         # Округляем новые значения до 3 знаков после запятой
#         new_length = round(new_length, 3)
#         new_weight = round(new_weight, 3)
#
#         round_pipe_data_analysis_collection.update_one(
#             {'nomenclature_id': data_entry['nomenclature_id']},
#             {
#                 '$inc': {'count': data_entry['count']},
#                 '$set': {
#                     'length': new_length,
#                     'weight': new_weight
#                 }
#             }
#         )
#     else:
#         # Вставляем новую запись
#         # Округляем значения 'length' и 'weight' до 3 знаков после запятой
#         data_entry['length'] = round(data_entry['length'], 3)
#         data_entry['weight'] = round(data_entry['weight'], 3)
#         round_pipe_data_analysis_collection.insert_one(data_entry)
#
#
# def clear_round_pipe_data_analysis():
#     """
#     Очищает коллекцию round_pipe_data_analysis.
#     """
#     round_pipe_data_analysis_collection.delete_many({})
#
#
# def get_round_pipe_data_analysis():
#     """
#     Получает данные из round_pipe_data_analysis и возвращает их как DataFrame.
#     """
#     data = pd.DataFrame(list(round_pipe_data_analysis_collection.find({}, {'_id': 0})))
#     print("Полученные данные анализа:", data.head())
#     return data
#
#
# # Методы для работы с time_table_data
# def get_nomenclature_id(nomenclature, diameter, wall_thickness, material):
#     """
#     Получает или создает уникальный nomenclature_id на основе комбинации nomenclature, diameter, wall_thickness и material.
#     """
#     # Поиск существующего nomenclature_id в round_pipe_data_analysis
#     existing = round_pipe_data_analysis_collection.find_one({
#         'nomenclature': nomenclature,
#         'diameter': float(diameter),
#         'wall_thickness': float(wall_thickness),
#         'material': material
#     })
#     if existing:
#         return existing['nomenclature_id']
#     else:
#         # Генерация нового nomenclature_id
#         last_entry = round_pipe_data_analysis_collection.find_one(sort=[("nomenclature_id", -1)])
#         new_id = last_entry['nomenclature_id'] + 1 if last_entry else 1
#         # Вставка новой записи в round_pipe_data_analysis с нулевыми значениями
#         new_round_pipe_entry = {
#             'nomenclature_id': new_id,
#             'nomenclature': nomenclature,
#             'diameter': float(diameter),
#             'wall_thickness': float(wall_thickness),
#             'material': material,
#             'length': 0.0,  # Храним как число
#             'weight': 0.0,  # Храним как число
#             'count': 0
#         }
#         round_pipe_data_analysis_collection.insert_one(new_round_pipe_entry)
#         # Вставка новой записи в time_table_data
#         new_time_table_entry = {
#             'nomenclature_id': new_id,
#             'nomenclature': nomenclature,
#             'material': material,
#             'year': datetime.datetime.now().year,
#             'january': 0,
#             'february': 0,
#             'march': 0,
#             'april': 0,
#             'may': 0,
#             'jun': 0,
#             'july': 0,
#             'august': 0,
#             'september': 0,
#             'october': 0,
#             'november': 0,
#             'december': 0,
#             'total_count': 0
#         }
#         time_table_data_collection.insert_one(new_time_table_entry)
#         return new_id
#
#
# def update_time_table_data(nomenclature_id, timestamp, count):
#     """
#     Обновляет запись в time_table_data на основе nomenclature_id, timestamp и count.
#     """
#     # Извлечение года и месяца из timestamp
#     year = timestamp.year
#     month = timestamp.month
#     month_mapping = {
#         1: 'january',
#         2: 'february',
#         3: 'march',
#         4: 'april',
#         5: 'may',
#         6: 'jun',
#         7: 'july',
#         8: 'august',
#         9: 'september',
#         10: 'october',
#         11: 'november',
#         12: 'december'
#     }
#     month_name = month_mapping.get(month)
#     if month_name:
#         # Обновление записи в time_table_data
#         query = {'nomenclature_id': nomenclature_id, 'year': year}
#         update = {
#             '$inc': {
#                 month_name: count,
#                 'total_count': count
#             }
#         }
#         time_table_data_collection.update_one(query, update, upsert=True)
#     else:
#         print(f"Некорректный месяц: {month}")
#
#
# def get_profile_pipe_data_analysis():
#     """
#     Получает данные из get_profile_pipe_data_analysis и возвращает их как DataFrame.
#     """
#     # data = pd.DataFrame(list(get_profile_pipe_data_analysis_collection.find({}, {'_id': 0})))
#     # print("Полученные данные анализа:", data.head())
#     # return data
#
#
# def get_round_bar_data_analysis():
#     """
#     Получает данные из get_round_bar_data_analysis и возвращает их как DataFrame.
#     """
#     # data = pd.DataFrame(list(get_round_bar_data_analysis_collection.find({}, {'_id': 0})))
#     # print("Полученные данные анализа:", data.head())
#     # return data
#
#
# def get_square_data_analysis():
#     """
#     Получает данные из get_round_bar_data_analysis и возвращает их как DataFrame.
#     """
#     # data = pd.DataFrame(list(get_square_data_analysis_collection.find({}, {'_id': 0})))
#     # print("Полученные данные анализа:", data.head())
#     # return data
#
#
# def get_rectangle_data_analysis():
#     """
#     Получает данные из get_rectangle_data_analysis и возвращает их как DataFrame.
#     """
#     # data = pd.DataFrame(list(get_rectangle_data_analysis_collection.find({}, {'_id': 0})))
#     # print("Полученные данные анализа:", data.head())
#     # return data
#
#
# def get_round_bar_forging_data_analysis():
#     """
#     Получает данные из get_round_bar_forging_data_analysis и возвращает их как DataFrame.
#     """
#     # data = pd.DataFrame(list(get_round_bar_forging_data_analysis_collection.find({}, {'_id': 0})))
#     # print("Полученные данные анализа:", data.head())
#     # return data
#
#
# def get_square_forging_data_analysis():
#     """
#     Получает данные из get_square_forging_data_analysis и возвращает их как DataFrame.
#     """
#     # data = pd.DataFrame(list(get_square_forging_data_analysis_collection.find({}, {'_id': 0})))
#     # print("Полученные данные анализа:", data.head())
#     # return data
#
#
# def get_rectangle_forging_data_analysis():
#     """
#     Получает данные из get_rectangle_forging_data_analysis и возвращает их как DataFrame.
#     """
#     # data = pd.DataFrame(list(get_rectangle_forging_data_analysis_collection.find({}, {'_id': 0})))
#     # print("Полученные данные анализа:", data.head())
#     # return data
#
#
# def get_ring_forging_data_analysis():
#     """
#     Получает данные из   get_ring_forging_data_analysis и возвращает их как DataFrame.
#     """
#     # data = pd.DataFrame(list(get_ring_forging_data_analysis_collection.find({}, {'_id': 0})))
#     # print("Полученные данные анализа:", data.head())
#     # return data
