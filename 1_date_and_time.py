"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, datetime, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = date.today()
    yesterday = today - timedelta(days=1)
    month_ago = today - timedelta(days=30)

    today_str = f"Дата сегодня: {today}"
    yesterday_str = f"Дата вчера: {yesterday}"
    month_ago_str = f"Дата 30 дней назад: {month_ago}"

    return today_str, yesterday_str, month_ago_str

print(*[d for d in print_days()], sep='\n')


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    try:
        str_to_date = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
        return str_to_date
    except ValueError:
        print(f"Ошибка: строка '{date_string}' не может быть преобразована в дату!")
        return None


if __name__ == "__main__":
    print_days()
    print("\nДата:", str_2_datetime("01/01/20 12:10:03.234567"))
