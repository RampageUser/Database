from sql import create_db
from students_db import student_db
from major_db import major_db
from department_db import department_db


def main():
    is_work: bool = True
    if is_work:
        create_db()

        while True:
            main_menu()
            user_option: int = choice_option(max=4)
            if user_option == 1:
                student_db()
            elif user_option == 2:
                major_db()
            elif user_option == 3:
                department_db()
            else:
                print('Shutdown')
                is_work = False
                break


def choice_option(max: int, min=1) -> int:
    try:
        user_option = int(input('Inter number of menu: '))
        while user_option < min or user_option > max:
            user_option = int(input('Inter correct number of menu: '))
        return user_option
    except Exception:
        print('~' * 40)
        print('incorrect value, please try again later.')
        print('~' * 40)
        main()

def main_menu() -> None:
    print('-' * 35)
    print('Main menu')
    print('1. Work with students database')
    print('2. Work with majors database')
    print('3. Work with department database')
    print('4. Exit')
    print('-' * 35)
    print()


if __name__ == '__main__':
    main()