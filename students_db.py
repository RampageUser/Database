from sql import add_data


def student_db():
    submenu_student()
    from main import choice_option
    user_option: int = choice_option(max=5)
    if user_option == 1:
        pass
    elif user_option == 2:
        add_student()
    elif user_option == 3:
        pass
    elif user_option == 4:
        pass
    elif user_option == 5:
        pass
    elif user_option == 6:
        pass
    else:
        pass

def submenu_student() -> None:
    print('-' * 35)
    print('Students database')
    print('1. Show all')
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