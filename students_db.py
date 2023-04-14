from sql import add_data, show_all_info, find_info, delete_info


def student_db():
    submenu_student()
    from config import choice_option
    user_option: int = choice_option(max=6)
    if user_option == 1:
        show_all_info(table='Students')
    elif user_option == 2:
        add_student()
    elif user_option == 3:
        delete_student()
    elif user_option == 4:
        pass
    elif user_option == 5:
        find_student()
    elif user_option == 6:
        return
    student_db()


def submenu_student() -> None:
    print()
    print('-' * 35)
    print('Students database')
    print()
    print('1. Show all students')
    print('2. Add new student')
    print('3. Remove student')
    print('4. Change info about student')
    print('5. Find student')
    print('6. Back')
    print('-' * 35)
    print()


def add_student():
    student_name: str = input('Inter name of student: ')
    major: str = input('Inter en existed Major ID: ')
    department: str = input('Inter en existed Department ID: ')
    add_data(table='Students', name=student_name, major_id=major, department_id=department)


def delete_student():
    student: str = input('Inter a student name what you want to remove: ')
    result = find_info(table='Students', name=student)
    if result:
        id: int = int(input('Inter ID: '))
        if id in result:
            delete_info(table='Students', id=id)
        else:
            print('Incorrect ID, please try later')


def find_student():
    student: str = input('Inter a student name: ')
    find_info(table='Students', name=student)