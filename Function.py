import Note
import View
import File_operations

# Минимальное количество знаков в тексте заметки
number = 8


def add():
    note = View.create_note(number)
    array = File_operations.read_file()
    for notes in array:
        if Note.get_id(note) == Note.Note.get_id(notes):
            Note.set_id(note)
    array.append(note)
    File_operations.write_file(array, 'a')
    print('Заметка добавлена...')


def show(text):
    logic = True
    array = File_operations.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.get_date(notes):
                print(Note.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = File_operations.read_file()
    logic = True
    for notes in array:
        if id == Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = View.create_note(number)
                Note.set_title(notes, note.get_title())
                Note.set_body(notes, note.get_body())
                Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет. Проверьте правильность введенного id')
    File_operations.write_file(array, 'a')