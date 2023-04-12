from sql import add_data, show_all_info


def student_db():
    submenu_student()
    from config import choice_option
    user_option: int = choice_option(max=6)
    if user_option == 1:
        show_all_info(table='Students')
    elif user_option == 2:
        add_student()
    elif user_option == 3:
        pass
    elif user_option == 4:
        pass
    elif user_option == 5:
        pass
    elif user_option == 6:
        return
    student_db()


def submenu_student() -> None:
    print('-' * 35)
    print('Students database')
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