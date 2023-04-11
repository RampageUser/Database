from sql import add_data


def major_db():
    submenu_major()
    from main import choice_option
    user_option: int = choice_option(max=5)
    if user_option == 1:
        pass
    elif user_option == 2:
        add_speciality()
    elif user_option == 3:
        pass
    elif user_option == 4:
        pass
    elif user_option == 5:
        pass
    else:
        pass


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