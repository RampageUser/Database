import sqlite3


def main():
    is_work: bool = True
    create_db()

    while is_work:
        main_menu()
        user_option: int = choice_option(max=4)
        if user_option == 1:
            submenu_student()
        elif user_option == 2:
            submenu_major()
        elif user_option == 3:
            submenu_department()
        else:
            is_work = False


def choice_option(max: int, min=1) -> int:
    try:
        user_option = int(input('Inter number of menu: '))
        while user_option < min or user_option > max:
            user_option = int(input('Inter correct number of menu: '))
        return user_option
    except Exception:
        print('incorrect value, please try again later.')
        return 0


def main_menu() -> None:
    print('-' * 35)
    print('Main menu')
    print('1. Work with students database')
    print('2. Work with majors database')
    print('3. Work with department database')
    print('4. Exit')
    print('-' * 35)
    print()


def submenu_student() -> None:
    print('-' * 35)
    print('Students database')
    print('1. Show all')
    print('2. Add new student')
    print('3. Remove student')
    print('4. Change info about student')
    print('5. Find student')
    print('-' * 35)
    print()
    user_option: int = choice_option(max=5)


def submenu_major() -> None:
    print('-' * 35)
    print('Major database')
    print('1. Show all speciality')
    print('2. Add new speciality')
    print('3. Delete speciality')
    print('4. Change info about speciality')
    print('-' * 35)
    print()
    user_option: int = choice_option(max=4)


def submenu_department() -> None:
    print('-' * 35)
    print('Department database')
    print('1. Show all')
    print('2. Add new department')
    print('3. Delete department')
    print('4. Change info about department')
    print('-' * 35)
    print()
    user_option: int = choice_option(max=4)



def create_db() -> None:
    with sqlite3.connect('student_info.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''create table if not exists Majors (MajorID integer primary key not null,
                                                             Name text)''')
        cursor.execute('''create table if not exists Department (DepartmentID integer primary key not null,
                                                                 Name text)''')
        cursor.execute('''create table if not exists Students (StudentID integer primary key not null,
                                                               Name text,
                                                               MajorID integer,
                                                               DepartmentId integer,
                                                               foreign key (MajorID) references Majors(MajorID),
                                                               foreign key (DepartmentID) references Department(DepartmentID))''')
        conn.commit()


if __name__ == '__main__':
    main()