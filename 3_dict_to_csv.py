"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    people = [
        {'name': 'Александр', 'age': 35, 'job': 'Инженер'},
        {'name': 'Иван', 'age': 30, 'job': 'Программист'},
        {'name': 'Мария', 'age': 28, 'job': 'Преподаватель'},
        {'name': 'Сергей', 'age': 32, 'job': 'Аналитик'},
        {'name': 'Ольга', 'age': 37, 'job': 'Руководитель'}
    ]
    # writing csv-file
    col_names = list(people[0].keys())
    
    try:
        with open('3_people.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=col_names, delimiter=';')
            writer.writeheader()
            writer.writerows(people)
    except PermissionError:
        print('Ошибка: файл занят и не может быть записан!')
        return None


if __name__ == "__main__":
    main()
