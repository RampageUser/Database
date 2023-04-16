from sql import add_data, show_all_info, find_info, delete_info, change_info
from lexicon import lexicon_notification, lexicon_inter

def major_db() -> None:
    submenu_major()
    from config import choice_option
    user_option: int = choice_option(max=5)
    if user_option == 1:
        show_all_info(table='Majors')
    elif user_option == 2:
        add_speciality()
    elif user_option == 3:
        delete_speciality()
    elif user_option == 4:
        change_speciality()
    elif user_option == 5:
        return
    major_db()


def submenu_major() -> None:
    print()
    print('-' * 35)
    print('Major database.')
    print()
    print('1. Show all speciality.')
    print('2. Add new speciality.')
    print('3. Delete speciality.')
    print('4. Change info about speciality.')
    print('5. Back.')
    print('-' * 35)
    print()


def add_speciality() -> None:
    speciality: str = input(lexicon_inter['New name'])
    add_data(table='Majors', name=speciality)


def delete_speciality() -> None:
    speciality: str = input(lexicon_inter['Remove'])
    result = find_info(table='Majors', name=speciality)
    if result:
        id: int = int(input(lexicon_inter['ID']))
        if id in result:
            delete_info(table='Majors', id=id)
        else:
            print(lexicon_notification['ID'])


def change_speciality() -> None:
    speciality: str = input(lexicon_inter['Change'])
    result = find_info(table='Majors', name=speciality)
    if result:
        new_speciality: str = input(lexicon_inter['New name'])
        if len(result) == 1:
            change_info(table='Majors', id=result[0], name=new_speciality)
        else:
            try:
                id: int = int(input(lexicon_inter['ID']))
                if id in result:
                    change_info(table='Majors', id=id, name=new_speciality)
                else:
                    print(lexicon_notification['ID'])
            except ValueError:
                print('~' * 40)
                print(lexicon_notification['Value err'])
                print('~' * 40)
    else:
        print(lexicon_notification['Not find'])
