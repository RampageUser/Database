from sql import add_data, show_all_info


def major_db():
    submenu_major()
    from config import choice_option
    user_option: int = choice_option(max=5)
    if user_option == 1:
        show_all_info(table='Majors')
    elif user_option == 2:
        add_speciality()
    elif user_option == 3:
        pass
    elif user_option == 4:
        pass
    elif user_option == 5:
        return
    major_db()


def submenu_major() -> None:
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