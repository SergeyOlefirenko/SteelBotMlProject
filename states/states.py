from aiogram.utils.helper import Helper, ListItem, HelperMode

USERS = {}


class MyStates(Helper):
    mode = HelperMode.CamelCase
    STATE_0 = ListItem()
    STATE_1 = ListItem()
    STATE_2 = ListItem()
    STATE_3 = ListItem()
    STATE_4 = ListItem()
    STATE_5 = ListItem()
    STATE_6 = ListItem()
    STATE_7 = ListItem()
    STATE_8 = ListItem()
    STATE_9 = ListItem()
    STATE_BIRTHDAY = ListItem()


class User:
    telegram_id = 0
    name = 'name'
    age = 0
    email = 'email'
    phone = r'^\d{10}$'
    state = ''

    def __init__(self, telegram_id: int):
        self.state = MyStates.STATE_0
        self.telegram_id = telegram_id

    def __int__(self):
        return self.telegram_id

    def __str__(self):
        return f'{self.name} {self.age} {self.email} {self.phone}'

    def __eq__(self, other):
        return other == self.telegram_id


# if __name__ == '__main__':
#     print(MyStates.all())

start_message = 'Пожалуйста пройдите регистрацию чтобы начать пользоваться '
get_name_message = 'Введите имя'
get_birthday_message = 'Введите дату вашего рождения'
get_email_message = 'Введите действующий адрес электронной почты'
get_phone_message = 'Введите действующий номер телефона'

user = {
    'UserID': ' ',
    'Firstname': '',
    'Lastname': '',
    'Birthday': '',
    'Mail': '',
    'Phone': ''
}

MESSAGES = {
    'start': start_message,
    'name': get_name_message,
    'age': get_birthday_message,
    'email': get_email_message,
    'phone': get_phone_message
}
