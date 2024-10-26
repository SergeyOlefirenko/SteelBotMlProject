import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from database import (client, db, round_pipe_data_analysis_collection, get_round_pipe_data_analysis)


def round_pipe_data_preparation():
    """
    Retrieves data from round_pipe_data_analysis and returns it as a DataFrame.
    """
    df = pd.DataFrame(list(round_pipe_data_analysis_collection.find({}, {'_id': 0})))
    print("Analysis data retrieved from MongoDB:", df.head())

    # Save data to a CSV file only if it is not empty
    if not df.empty:
        df.to_csv("round_pipe_data_analysis.csv", index=False)
        print("Data successfully saved to round_pipe_data_analysis.csv")
    else:
        print("No data available to save to CSV.")

    return df


# Check if CSV file exists and load data
data = pd.DataFrame()  # Initialize data as an empty DataFrame

if os.path.exists("round_pipe_data_analysis.csv"):
    # Load data from existing CSV file
    try:
        data = pd.read_csv("round_pipe_data_analysis.csv")
        if data.empty:
            raise ValueError("Loaded CSV file is empty.")
        print("Data loaded from existing file round_pipe_data_analysis.csv")
    except pd.errors.EmptyDataError:
        print("CSV file is empty, no data loaded.")
    except ValueError as ve:
        print(ve)
else:
    # Otherwise, fetch data from MongoDB and save to CSV
    data = round_pipe_data_preparation()  # Теперь используем функцию
    print("Data loaded from MongoDB and saved to round_pipe_data_analysis.csv")

# At this point, we should check if data is not empty before proceeding
if data.empty:
    print("No data available for further processing.")
else:
    # Data cleaning
    data.fillna(0, inplace=True)

    # Check if required columns are present
    required_columns = ['length', 'weight', 'diameter', 'wall_thickness', 'count']
    missing_columns = [col for col in required_columns if col not in data.columns]

    if missing_columns:
        print(f"Missing columns: {', '.join(missing_columns)}")
        print("Exiting the program due to missing required data.")
        raise ValueError("Required columns are missing from the data.")

    # Data type conversion
    data['length'] = data['length'].astype(float)
    data['weight'] = data['weight'].astype(float)
    data['diameter'] = data['diameter'].astype(float)
    data['wall_thickness'] = data['wall_thickness'].astype(float)
    data['count'] = data['count'].astype(int)

    # Outlier detection and management
    for column in ['length', 'weight', 'diameter', 'wall_thickness']:
        median = data[column].median()
        std_dev = data[column].std()
        upper_limit = median + 3 * std_dev
        data.loc[data[column] > upper_limit, column] = median

    # Descriptive statistics for key variables
    description = data[['length', 'weight', 'diameter', 'wall_thickness']].describe()
    print("Descriptive statistics for key variables:\n", description)

    # Additional descriptive statistics
    print("Mean for key variables:\n", data[['length', 'weight', 'diameter', 'wall_thickness']].mean())
    print("Median for key variables:\n", data[['length', 'weight', 'diameter', 'wall_thickness']].median())
    print("Standard deviation for key variables:\n", data[['length', 'weight', 'diameter', 'wall_thickness']].std())

    # Determine mode based on most common diameter and wall thickness combinations
    mode_data = data.groupby(['diameter', 'wall_thickness'])['count'].sum()
    most_common = mode_data.idxmax()
    most_common_count = mode_data.max()

    print("Most common diameter and wall thickness combination (mode):\n", most_common)
    print("Count for this combination:", most_common_count)

    # Visualization of pipe length distribution based on request count
    plt.figure(figsize=(10, 6))

    # Group data by length and sum request counts
    length_counts = data.groupby('length')['count'].sum().reset_index()

    # Create color palette
    colors = sns.color_palette("husl", len(length_counts))

    # Use hue for length and remove legend
    sns.barplot(x='length', y='count', data=length_counts, hue='length', palette=colors, legend=False)

    plt.title("Request Count by Pipe Length")
    plt.xlabel("Pipe Length")
    plt.ylabel("Request Count")
    plt.xticks(rotation=45)
    plt.show()

    # Visualization of diameter and wall thickness distribution based on request count
    plt.figure(figsize=(12, 8))

    # Group data by diameter and wall thickness, summing request counts
    diameter_thickness_counts = data.groupby(['diameter', 'wall_thickness'])['count'].sum().reset_index()

    # Unique values for wall thickness
    unique_wall_thickness = diameter_thickness_counts['wall_thickness'].unique()

    # Create color palette
    colors = sns.color_palette("husl", len(unique_wall_thickness))

    # Create columns with appropriate spacing
    sns.barplot(x='diameter', y='count', hue='wall_thickness', data=diameter_thickness_counts, palette=colors,
                dodge=True)

    plt.title("Request Frequency by Diameter and Wall Thickness")
    plt.xlabel("Pipe Diameter")
    plt.ylabel("Request Count")
    plt.xticks(rotation=45)

    # Configure legend positioning
    plt.legend(title="Wall Thickness", bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    plt.show()

    # # Exploring the relationship between pipe weight, diameter, and wall thickness

    # Check data types and NaN values
    print("Data types in loaded data:\n", data.dtypes)
    print("NaN values count per column:\n", data.isna().sum())

    # Create a new column for weight per meter with precision control
    data['weight_per_meter'] = data['weight'] / data['length']

    # Check values in the new column
    print("Data with calculated weight_per_meter column:")
    print(data[['weight', 'length', 'weight_per_meter']])

    # Plotting
    if 'material' in data.columns:
        plt.figure(figsize=(14, 8))

        # Group data by diameter, wall thickness, and material, summing weight and length
        weight_counts = data.groupby(['diameter', 'wall_thickness', 'material']).agg(
            total_weight=('weight', 'sum'),
            total_length=('length', 'sum')
        ).reset_index()

        # Add weight per meter
        weight_counts['weight_per_meter'] = weight_counts['total_weight'] / weight_counts['total_length']

        # Create labels for x-axis
        weight_counts['label'] = weight_counts.apply(
            lambda x: f"Ø{int(x['diameter'])}x{int(x['wall_thickness'])}\n{x['material']}",
            axis=1
        )

        # Plot bar chart
        sns.barplot(x='label', y='weight_per_meter', data=weight_counts, palette='viridis', hue='material', dodge=True)

        plt.title("Pipe Weight per Meter by Diameter, Wall Thickness, and Material")
        plt.xlabel("Round Pipe (Diameter x Wall Thickness, Material)")
        plt.ylabel("Weight per Meter, kg")

        # Rotate labels for readability
        plt.xticks(rotation=45, ha='right')

        # Add values on bars
        for index, row in enumerate(weight_counts.itertuples(), start=0):
            plt.text(
                index,
                row.weight_per_meter + 0.5,
                f"{row.weight_per_meter:.2f} kg",
                color='black',
                ha="center",
                va="bottom"
            )

        plt.tight_layout()

    plt.show()

    # Correlation matrix for numerical columns
    numeric_data = data[['length', 'weight', 'diameter', 'wall_thickness']]
    correlation_matrix = numeric_data.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f",
                cbar_kws={'shrink': .8}, annot_kws={"size": 8})
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()

# Russian language
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os
# from database import (client, db, round_pipe_data_analysis_collection, get_round_pipe_data_analysis)
#
#
# # Получение данных из MongoDB
# def round_pipe_data_preparation():
#     """
#     Получаем данные из round_pipe_data_analysis и возвращает их как DataFrame.
#     """
#     # from pymongo import MongoClient
#     # client = MongoClient("mongodb://localhost:27017/")
#     # db = client["database"]
#     # round_pipe_data_analysis_collection = db["round_pipe_data_analysis"]
#
#     # Получение данных из MongoDB и преобразование в DataFrame
#     df = pd.DataFrame(list(round_pipe_data_analysis_collection.find({}, {'_id': 0})))
#     print("Полученные данные анализа из MongoDB:", df.head())
#
#     # Сохранение данных в CSV файл
#     df.to_csv("round_pipe_data_analysis.csv", index=False)
#     print("Данные успешно сохранены в round_pipe_data_analysis.csv")
#
#     return df
#
#
# # Проверка существования CSV файла и загрузка данных
# if os.path.exists("round_pipe_data_analysis.csv"):
#     # Если CSV файл существует, загружаем данные из него
#     data = pd.read_csv("round_pipe_data_analysis.csv")
#     print("Данные загружены из существующего файла round_pipe_data_analysis.csv")
# else:
#     # В противном случае получаем данные из MongoDB и сохраняем их в CSV
#     data = get_round_pipe_data_analysis()
#     print("Данные загружены из MongoDB и сохранены в round_pipe_data_analysis.csv")
#
#
# # Очистка данных
# data.fillna(0, inplace=True)
#
# # Приведение типов данных
# data['length'] = data['length'].astype(float)
# data['weight'] = data['weight'].astype(float)
# data['diameter'] = data['diameter'].astype(float)
# data['wall_thickness'] = data['wall_thickness'].astype(float)
# data['count'] = data['count'].astype(int)
#
# # Обнаружение и управление выбросами
# for column in ['length', 'weight', 'diameter', 'wall_thickness']:
#     median = data[column].median()
#     std_dev = data[column].std()
#     upper_limit = median + 3 * std_dev
#     data.loc[data[column] > upper_limit, column] = median
#
# # Описательная статистика для ключевых переменных
# description = data[['length', 'weight', 'diameter', 'wall_thickness']].describe()
# print("Описательная статистика для ключевых переменных:\n", description)
#
# # Дополнительная описательная статистика
# print("Среднее значение для ключевых переменных:\n", data[['length', 'weight', 'diameter', 'wall_thickness']].mean())
# print("Медиана для ключевых переменных:\n", data[['length', 'weight', 'diameter', 'wall_thickness']].median())
# print("Стандартное отклонение для ключевых переменных:\n",
#       data[['length', 'weight', 'diameter', 'wall_thickness']].std())
#
# # Определение моды на основе наиболее популярных комбинаций диаметра и толщины стенки
# mode_data = data.groupby(['diameter', 'wall_thickness'])['count'].sum()
# most_common = mode_data.idxmax()
# most_common_count = mode_data.max()
#
# print("Наиболее популярная комбинация диаметра и толщины стенки (мода):\n", most_common)
# print("Количество запросов для этой комбинации:", most_common_count)
#
# # Визуализация
# # Визуализация распределения длины труб на основании количества запросов
# plt.figure(figsize=(10, 6))
#
# # Группируем данные по длине и суммируем количество запросов
# length_counts = data.groupby('length')['count'].sum().reset_index()
#
# # Создаем палитру цветов
# colors = sns.color_palette("husl", len(length_counts))  # "husl" generates a variety of colors
#
# # Используем параметр hue для отображения длины и убираем легенду
# sns.barplot(x='length', y='count', data=length_counts, hue='length', palette=colors, legend=False)
#
# plt.title("Количество запросов по длине труб")
# plt.xlabel("Длина трубы")
# plt.ylabel("Количество запросов")
# plt.xticks(rotation=45)
# plt.show()
#
# # Визуализация распределения диаметра и толщины стенки на основании количества запросов
# plt.figure(figsize=(12, 8))
#
# # Группируем данные по диаметру и толщине стенки, суммируя количество запросов
# diameter_thickness_counts = data.groupby(['diameter', 'wall_thickness'])['count'].sum().reset_index()
#
# # Уникальные значения для толщины стенки
# unique_wall_thickness = diameter_thickness_counts['wall_thickness'].unique()
#
# # Создаем палитру цветов
# colors = sns.color_palette("husl", len(unique_wall_thickness))  # Генерация цветов по количеству уникальных значений
#
# # Создаем столбцы для отображения с правильным смещением
# sns.barplot(x='diameter', y='count', hue='wall_thickness', data=diameter_thickness_counts, palette=colors, dodge=True)
#
# plt.title("Частота запросов по диаметру и толщине стенки")
# plt.xlabel("Диаметр трубы")
# plt.ylabel("Количество запросов")
# plt.xticks(rotation=45)
#
# # Настройка расположения легенды
# plt.legend(title="Толщина стенки", bbox_to_anchor=(1.05, 1), loc='upper left')
#
# plt.tight_layout()  # Чтобы предотвратить наложение графиков и меток
# plt.show()
#
# # #Исследование зависимости веса трубы от диаметра и толщины стенки
#
# # Проверка типов данных и наличие NaN значений
# print("Типы данных в загруженных данных:\n", data.dtypes)
# print("Количество NaN значений в каждом столбце:\n", data.isna().sum())
#
# # Создаем новый столбец с весом на метр с контролем точности
# data['weight_per_meter'] = data['weight'] / data['length']
#
# # Проверка значений в новом столбце
# print("Данные с рассчитанным столбцом weight_per_meter:")
# print(data[['weight', 'length', 'weight_per_meter']])
#
# # Построение графика
# if 'material' in data.columns:
#     plt.figure(figsize=(14, 8))
#
#     # Группируем данные по диаметру, толщине стенки и материалу, вычисляя суммарный вес и длину
#     weight_counts = data.groupby(['diameter', 'wall_thickness', 'material']).agg(
#         total_weight=('weight', 'sum'),
#         total_length=('length', 'sum')
#     ).reset_index()
#
#     # Добавляем вес на метр
#     weight_counts['weight_per_meter'] = weight_counts['total_weight'] / weight_counts['total_length']
#
#     # Создаем метки для оси X
#     weight_counts['label'] = weight_counts.apply(
#         lambda x: f"Ø{int(x['diameter'])}x{int(x['wall_thickness'])}\n{x['material']}",
#         axis=1
#     )
#
#     # Строим гистограмму
#     sns.barplot(x='label', y='weight_per_meter', data=weight_counts, palette='viridis', hue='material', dodge=True)
#
#     plt.title("Вес 1 метра трубы в зависимости от диаметра, толщины стенки и материала")
#     plt.xlabel("Круглая труба (диаметр x толщина стенки, материал)")
#     plt.ylabel("Вес на метр, кг")
#
#     # Поворот меток для лучшей читаемости
#     plt.xticks(rotation=45, ha='right')
#
#     # Добавление значений на столбцы
#     for index, row in enumerate(weight_counts.itertuples(), start=0):
#         plt.text(
#             index,
#             row.weight_per_meter + 0.5,
#             f"{row.weight_per_meter:.2f} кг",
#             color='black',
#             ha="center",
#             va="bottom"
#         )
#
#     plt.tight_layout()  # Предотвращение наложений элементов графика
#
# plt.show()
#
# # Корреляционная матрица для числовых столбцов
# numeric_data = data[['length', 'weight', 'diameter', 'wall_thickness']]
# correlation_matrix = numeric_data.corr()
#
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f",
#             cbar_kws={'shrink': .8}, annot_kws={"size": 8})
# plt.xticks(rotation=45, ha='right')
# plt.yticks(rotation=0)
# plt.title("Корреляционная матрица")
# plt.tight_layout()
# plt.show()
