import Note


def create_note(number):
    title = check_len_text_input(
        input('Введите название заметки: '), number)
    body = check_len_text_input(
        input('Введите описание заметки: '), number)
    return Note(title=title, body=body)



def menu():
    print("\nПеред Вами программа 'Заметки'. Вы можете воспользоваться слудующими функциями:\n\n"
          "1 - вывод всех заметок из файла\n 2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n"
          "5 - выборка заметок по дате\n6 - показать заметку по id\n7 - выход\n\nВведите номер функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def parting():
    print("Спасибо за то, что воспользовались нашей программой!")