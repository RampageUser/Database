from sql import add_data, show_all_info, find_info, delete_info, change_info
from lexicon import lexicon_inter, lexicon_notification


def department_db() -> None:
    submenu_department()
    from config import choice_option
    user_option: int = choice_option(max=5)
    if user_option == 1:
        show_all_info(table='Department')
    elif user_option == 2:
        add_department()
    elif user_option == 3:
        delete_department()
    elif user_option == 4:
        change_department()
    elif user_option == 5:
        return
    department_db()


def submenu_department() -> None:
    print()
    print('-' * 35)
    print('Department database.')
    print()
    print('1. Show all.')
    print('2. Add new department.')
    print('3. Delete department.')
    print('4. Change info about department.')
    print('5. Back.')
    print('-' * 35)
    print()


def add_department() -> None:
    department: str = input(lexicon_inter['New name'])
    add_data(table='Department', name=department)


def delete_department() -> None:
    department: str = input(lexicon_inter['Remove'])
    result = find_info(table='Department', name=department)
    if result:
        id: int = int(input(lexicon_inter['ID']))
        if id in result:
            delete_info(table='Majors', id=id)
        else:
            print(lexicon_notification['ID'])


def change_department() -> None:
    department: str = input(lexicon_inter['Change'])
    result = find_info(table='Department', name=department)
    if result:
        new_department: str = input(lexicon_inter['New name'])
        if len(result) == 1:
            change_info(table='Department', id=result[0], name=new_department)
        else:
            try:
                id: int = int(input(lexicon_inter['ID']))
                if id in result:
                    change_info(table='Department', id=id, name=new_department)
                else:
                    print(lexicon_notification['ID'])
            except ValueError:
                print('~' * 40)
                print(lexicon_notification['Value err'])
                print('~' * 40)
    else:
        print(lexicon_notification['Not find'])