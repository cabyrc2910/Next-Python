# Задача 7
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.

def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def valid_date(date_str):
    day, month, year = map(int, date_str.split('.'))
    if month < 1 or month > 12:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 29 if leap_year(year) else 28
    return False if day < 1 or day > max_day else year >= 1 and year <= 9999


if __name__ == "__main__":
    date_str = "31.12.2022"
    if valid_date(date_str):
        print(f"{date_str} - Дата существует")
    else:
        print(f"{date_str} - Дата не существует")


