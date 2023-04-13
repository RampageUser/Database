from sql import add_data, show_all_info, find_info, delete_info

def major_db():
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
        pass
    elif user_option == 5:
        return
    major_db()


def submenu_major() -> None:
    print()
    print('-' * 35)
    print('Major database')
    print('1. Show all speciality')
    print('2. Add new speciality')
    print('3. Delete speciality')
    print('4. Change info about speciality')
    print('5. Back')
    print('-' * 35)
    print()


def add_speciality():
    speciality: str = input('Inter new speciality: ')
    add_data(table='Majors', name=speciality)


def delete_speciality():
    speciality: str = input('Inter a speciality what you want to remove: ')
    result = find_info(table='Majors', name=speciality)
    if result:
        id: int = int(input('Inter ID: '))
        if id in result:
            delete_info(table='Majors', id=id)
        else:
            print('Incorrect ID, please try later')