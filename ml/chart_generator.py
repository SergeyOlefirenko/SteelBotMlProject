import matplotlib.pyplot as plt
import seaborn as sns


def create_forecast_chart(data):
    """
    Creates a forecast chart based on the data and predicted values.
    :param data: DataFrame with top products and their predicted 'predicted_weight'
    :return: Path to the saved chart image
    """
    # Check if there is enough data to create a chart
    if data.empty:
        print("No data available to create the chart.")
        return None

    # Sort data by 'predicted_weight' in descending order
    data_sorted = data.sort_values(by='predicted_weight', ascending=False)

    # Create labels for the X-axis
    data_sorted['label'] = data_sorted.apply(
        # lambda row: f"Ø{int(row['diameter'])}x{int(row['wall_thickness'])}\n{row['material']}",
        lambda x: f"Ø{int(x['diameter'])}x{int(x['wall_thickness'])}\n{x['material']}",
        axis=1
    )

    plt.figure(figsize=(15, 10))
    sns.barplot(
        x='label',
        y='predicted_weight',
        data=data_sorted,
        palette='viridis'
    )
    plt.xlabel('Round pipe (diameter x wall thickness, material)')
    plt.ylabel('Predicted product weight, kg')
    plt.title('Forecast of the most in-demand assortment of round pipes')
    plt.xticks(rotation=0, ha='center')  # Label alignment

    # Add 'predicted_weight' values above the bars with a margin
    for index, row in enumerate(data_sorted.itertuples(), start=0):
        plt.text(
            index,
            row.predicted_weight + 0.5,  # Offset text above the bar
            f"{row.predicted_weight:.3f} kg",
            color='black',
            ha="center",
            va="bottom"
        )

    plt.tight_layout()

    # Save chart to a temporary file
    chart_path = 'forecast_chart.png'
    plt.savefig(chart_path)
    plt.close()

    return chart_path

# Russian language
# import matplotlib.pyplot as plt
# import seaborn as sns
#
#
# def create_forecast_chart(data):
#     """
#     Создаем график прогноза на основе данных и предсказанных значений.
#     :param data: DataFrame с топовыми продуктами и их предсказанными 'predicted_weight'
#     :return: Путь к сохраненному изображению графика
#     """
#     # Проверка, что данных достаточно для построения графика
#     if data.empty:
#         print("Нет данных для построения графика.")
#         return None
#
#     # Сортировка данных по 'predicted_weight' в порядке убывания
#     data_sorted = data.sort_values(by='predicted_weight', ascending=False)
#
#     # Создаем лейблы для оси X
#     data_sorted['label'] = data_sorted.apply(
#         lambda row: f"Ø{int(row['diameter'])}x{int(row['wall_thickness'])}\n{row['material']}",
#         axis=1
#     )
#
#     plt.figure(figsize=(15, 10))
#     sns.barplot(
#         x='label',
#         y='predicted_weight',
#         data=data_sorted,
#         palette='viridis'
#     )
#     plt.xlabel('Round pipe (diameter x wall thickness, material)')
#     plt.ylabel('Predicted product weight, kg')
#     plt.title('Forecast of the most in-demand assortment of round pipes')
#     plt.xticks(rotation=0, ha='center')  # Расположение подписей
#
#     # Добавление значений 'predicted_weight' на столбцы с отступом
#     for index, row in enumerate(data_sorted.itertuples(), start=0):
#         plt.text(
#             index,
#             row.predicted_weight + 0.5,  # Смещаем текст вверх от столбца
#             f"{row.predicted_weight:.3f} kg",
#             color='black',
#             ha="center",
#             va="bottom"
#         )
#
#     plt.tight_layout()
#
#     # Сохранение графика во временный файл
#     chart_path = 'forecast_chart.png'
#     plt.savefig(chart_path)
#     plt.close()
#
#     return chart_path
