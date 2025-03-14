"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длину получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r') as file:
        text = file.read()
    str_len = len(text)
    print(f"Длина строки: {str_len}")

    token_count = len(text.split())
    print(f"Количество слов: {token_count}")

    new_text = text.replace('.', '!')

    with open('referat2.txt', 'w') as file:
        file.write(new_text)


if __name__ == "__main__":
    main()
