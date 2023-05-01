import Function
import View

def run():
    input_from_user = ''
    while input_from_user != '7':
        View.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            Function.show('all')
        if input_from_user == '2':
            Function.add()
        if input_from_user == '3':
            Function.show('all')
            Function.id_edit_del_show('del')
        if input_from_user == '4':
            Function.show('all')
            Function.id_edit_del_show('edit')
        if input_from_user == '5':
            Function.show('date')
        if input_from_user == '6':
            Function.show('id')
            Function.id_edit_del_show('show')
        if input_from_user == '7':
            View.parting()
            break