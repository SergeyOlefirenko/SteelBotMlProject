from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import os


class ProductForecast:
    def __init__(self, model_dir='models'):
        self.model_dir = model_dir
        os.makedirs(self.model_dir, exist_ok=True)
        self.regressor = self.load_model('regressor.pkl')
        self.classifiers = {
            'nomenclature': self.load_model('classifier_nomenclature.pkl'),
            'material': self.load_model('classifier_material.pkl'),
            'diameter': self.load_model('classifier_diameter.pkl'),
            'wall_thickness': self.load_model('classifier_wall_thickness.pkl')
        }

    def load_model(self, filename):
        path = os.path.join(self.model_dir, filename)
        if os.path.exists(path):
            return joblib.load(path)
        return None

    def save_model(self, model, filename):
        path = os.path.join(self.model_dir, filename)
        joblib.dump(model, path)
        print(f"Model {filename} saved.")

    def train_regressor(self, data):
        # Checking for required columns
        required_columns = ['nomenclature', 'material', 'diameter', 'wall_thickness', 'count', 'weight']
        missing_columns = set(required_columns) - set(data.columns)
        if missing_columns:
            print(f"Missing columns: {missing_columns}")
            return

        # Checking for sufficient data
        if len(data) < 10:
            print("Insufficient data for training regressor. A minimum of 10 records is required.")
            return

        print("Data for regressor training:", data.head())

        # Features and target variable
        X = data[['nomenclature', 'material', 'diameter', 'wall_thickness', 'count']]
        y = data['weight']

        # Preprocessor
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', 'passthrough', ['count']),
                ('cat', OneHotEncoder(handle_unknown='ignore'),
                 ['nomenclature', 'material', 'diameter', 'wall_thickness'])
            ]
        )

        # Pipeline
        pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
        ])

        # Data splitting
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Training
        pipeline.fit(X_train, y_train)

        # Saving the model
        self.save_model(pipeline, 'regressor.pkl')

        self.regressor = pipeline

    def train_classifier(self, data, target):
        # Checking for required columns
        required_columns = ['weight', 'count', target]
        missing_columns = set(required_columns) - set(data.columns)
        if missing_columns:
            print(f"Missing columns: {missing_columns}")
            return

        # Checking for sufficient data
        if len(data) < 10:
            print(f"Insufficient data for training classifier '{target}'. A minimum of 10 records is required.")
            return

        print(f"Data for classifier '{target}' training:", data.head())

        # Features and target variable
        X = data[['weight', 'count']]
        y = data[target]

        # If the target variable is numeric, convert it to a string for classification
        if data[target].dtype != 'object':
            y = y.astype(str)

        # Preprocessor
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', 'passthrough', ['weight', 'count'])
            ]
        )

        # Pipeline
        pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
        ])

        # Data splitting
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Training
        pipeline.fit(X_train, y_train)

        # Saving the model
        filename = f'classifier_{target}.pkl'
        self.save_model(pipeline, filename)

        self.classifiers[target] = pipeline

    def train_all_models(self, data):
        # Training the regressor
        self.train_regressor(data)

        # Training classifiers
        targets = ['nomenclature', 'material', 'diameter', 'wall_thickness']
        for target in targets:
            self.train_classifier(data, target)

    def predict_weight(self, new_data):
        if self.regressor is None:
            self.regressor = self.load_model('regressor.pkl')
            if self.regressor is None:
                raise ValueError("The regressor model is not trained.")

        # Checking for required columns
        required_columns = ['nomenclature', 'material', 'diameter', 'wall_thickness', 'count']
        if not all(col in new_data.columns for col in required_columns):
            raise ValueError(f"Missing columns: {set(required_columns) - set(new_data.columns)}")

        predictions = self.regressor.predict(new_data)
        # Rounding predicted values to 3 decimal places
        predictions = [round(pred, 3) for pred in predictions]
        return predictions

    def predict_class(self, new_data, target):
        if target not in self.classifiers:
            raise ValueError(f"Target variable '{target}' is not supported.")

        classifier = self.classifiers[target]
        if classifier is None:
            classifier = self.load_model(f'classifier_{target}.pkl')
            if classifier is None:
                raise ValueError(f"Classifier for '{target}' is not trained.")

        # Checking for required columns
        required_columns = ['weight', 'count']
        if not all(col in new_data.columns for col in required_columns):
            raise ValueError(f"Missing columns: {set(required_columns) - set(new_data.columns)}")

        return classifier.predict(new_data)


# Create a global instance of the class
forecast = ProductForecast()

# Russian language
# from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline
# import joblib
# import os
#
#
# class ProductForecast:
#     def __init__(self, model_dir='models'):
#         self.model_dir = model_dir
#         os.makedirs(self.model_dir, exist_ok=True)
#         self.regressor = self.load_model('regressor.pkl')
#         self.classifiers = {
#             'nomenclature': self.load_model('classifier_nomenclature.pkl'),
#             'material': self.load_model('classifier_material.pkl'),
#             'diameter': self.load_model('classifier_diameter.pkl'),
#             'wall_thickness': self.load_model('classifier_wall_thickness.pkl')
#         }
#
#     def load_model(self, filename):
#         path = os.path.join(self.model_dir, filename)
#         if os.path.exists(path):
#             return joblib.load(path)
#         return None
#
#     def save_model(self, model, filename):
#         path = os.path.join(self.model_dir, filename)
#         joblib.dump(model, path)
#         print(f"Модель {filename} сохранена.")
#
#     def train_regressor(self, data):
#         # Проверка наличия необходимых колонок
#         required_columns = ['nomenclature', 'material', 'diameter', 'wall_thickness', 'count', 'weight']
#         missing_columns = set(required_columns) - set(data.columns)
#         if missing_columns:
#             print(f"Отсутствуют колонки: {missing_columns}")
#             return
#
#         # Проверка достаточности данных
#         if len(data) < 10:
#             print("Недостаточно данных для обучения регрессора. Необходимо минимум 10 записей.")
#             return
#
#         print("Данные для обучения регрессора:", data.head())
#
#         # Признаки и целевая переменная
#         X = data[['nomenclature', 'material', 'diameter', 'wall_thickness', 'count']]
#         y = data['weight']
#
#         # Препроцессор
#         preprocessor = ColumnTransformer(
#             transformers=[
#                 ('num', 'passthrough', ['count']),
#                 ('cat', OneHotEncoder(handle_unknown='ignore'),
#                  ['nomenclature', 'material', 'diameter', 'wall_thickness'])
#             ]
#         )
#
#         # Pipeline
#         pipeline = Pipeline(steps=[
#             ('preprocessor', preprocessor),
#             ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
#         ])
#
#         # Разделение данных
#         X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
#         # Обучение
#         pipeline.fit(X_train, y_train)
#
#         # Сохранение модели
#         self.save_model(pipeline, 'regressor.pkl')
#
#         self.regressor = pipeline
#
#     def train_classifier(self, data, target):
#         # Проверка наличия необходимых колонок
#         required_columns = ['weight', 'count', target]
#         missing_columns = set(required_columns) - set(data.columns)
#         if missing_columns:
#             print(f"Отсутствуют колонки: {missing_columns}")
#             return
#
#         # Проверка достаточности данных
#         if len(data) < 10:
#             print(f"Недостаточно данных для обучения классификатора '{target}'. Необходимо минимум 10 записей.")
#             return
#
#         print(f"Данные для обучения классификатора '{target}':", data.head())
#
#         # Признаки и целевая переменная
#         X = data[['weight', 'count']]
#         y = data[target]
#
#         # Если целевая переменная числовая, преобразуем её в строку для классификации
#         if data[target].dtype != 'object':
#             y = y.astype(str)
#
#         # Препроцессор
#         preprocessor = ColumnTransformer(
#             transformers=[
#                 ('num', 'passthrough', ['weight', 'count'])
#             ]
#         )
#
#         # Pipeline
#         pipeline = Pipeline(steps=[
#             ('preprocessor', preprocessor),
#             ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
#         ])
#
#         # Разделение данных
#         X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
#         # Обучение
#         pipeline.fit(X_train, y_train)
#
#         # Сохранение модели
#         filename = f'classifier_{target}.pkl'
#         self.save_model(pipeline, filename)
#
#         self.classifiers[target] = pipeline
#
#     def train_all_models(self, data):
#         # Обучение регрессора
#         self.train_regressor(data)
#
#         # Обучение классификаторов
#         targets = ['nomenclature', 'material', 'diameter', 'wall_thickness']
#         for target in targets:
#             self.train_classifier(data, target)
#
#     def predict_weight(self, new_data):
#         if self.regressor is None:
#             self.regressor = self.load_model('regressor.pkl')
#             if self.regressor is None:
#                 raise ValueError("Модель регрессора не обучена.")
#
#         # Проверка наличия необходимых колонок
#         required_columns = ['nomenclature', 'material', 'diameter', 'wall_thickness', 'count']
#         if not all(col in new_data.columns for col in required_columns):
#             raise ValueError(f"Отсутствуют колонки: {set(required_columns) - set(new_data.columns)}")
#
#         predictions = self.regressor.predict(new_data)
#         # Округляем предсказанные значения до 3 знаков после запятой
#         predictions = [round(pred, 3) for pred in predictions]
#         return predictions
#
#     def predict_class(self, new_data, target):
#         if target not in self.classifiers:
#             raise ValueError(f"Целевая переменная '{target}' не поддерживается.")
#
#         classifier = self.classifiers[target]
#         if classifier is None:
#             classifier = self.load_model(f'classifier_{target}.pkl')
#             if classifier is None:
#                 raise ValueError(f"Классификатор для '{target}' не обучен.")
#
#         # Проверка наличия необходимых колонок
#         required_columns = ['weight', 'count']
#         if not all(col in new_data.columns for col in required_columns):
#             raise ValueError(f"Отсутствуют колонки: {set(required_columns) - set(new_data.columns)}")
#
#         return classifier.predict(new_data)
#
#
# # Создание глобального экземпляра класса
# forecast = ProductForecast()
