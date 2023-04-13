from sql import add_data, show_all_info, find_info, delete_info


def department_db():
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
        pass
    elif user_option == 5:
        return
    department_db()


def submenu_department() -> None:
    print()
    print('-' * 35)
    print('Department database')
    print('1. Show all')
    print('2. Add new department')
    print('3. Delete department')
    print('4. Change info about department')
    print('5. Back')
    print('-' * 35)
    print()


def add_department():
    department: str = input('Inter new department: ')
    add_data(table='Department', name=department)


def delete_department():
    department: str = input('Inter a department what you want to remove: ')
    result = find_info(table='Department', name=department)
    if result:
        id: int = int(input('Inter ID: '))
        if id in result:
            delete_info(table='Majors', id=id)
        else:
            print('Incorrect ID, please try later')