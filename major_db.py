from sql import add_data, show_all_info, find_info, delete_info, change_info

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
        change_speciality()
    elif user_option == 5:
        return
    major_db()


def submenu_major() -> None:
    print()
    print('-' * 35)
    print('Major database')
    print()
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


def change_speciality():
    speciality: str = input('Inter speciality what do you want to change: ')
    result = find_info(table='Majors', name=speciality)
    if result:
        new_speciality: str = input('Inter a new name for speciality: ')
        if len(result) == 1:
            change_info(table='Majors', id=result[0], name=new_speciality)
        else:
            try:
                id: int = int(input('Inter a correct ID of speciality: '))
                if id in result:
                    change_info(table='Majors', id=id, name=new_speciality)
                else:
                    print('Incorrect ID, please try again later.')
            except ValueError:
                print('Incorrect value.')
    else:
        print("Speciality didn't found")
