# Задание №4
# 📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# 📌 Преобразуйте его в дату в текущем году.
# 📌 Логируйте ошибки, если текст не соответсвует формату.

import logging
from datetime import datetime, date


def date_func(date_text):
    number = date_text[0]
    my_year = datetime.now().year
    number_date, week_day, month = date_text.split()
    number_date = int(number_date[0])
    week_day = week_day[0:3]
    my_month = month[0:3]
    week_day_list_rus = ['пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос']
    week_day_list_eng = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    month_list = [' ',"янв", "фев", "мар", "апр", "мая", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
    count = 0
    for i in range(1,32):
        temp = date(my_year, month_list.index(my_month), i)
        if temp.weekday() == week_day_list_rus.index(week_day):
            count += 1
        if count == number_date:
            return temp


my_text = '3-й пятница ноября'
print(date_func(my_text))