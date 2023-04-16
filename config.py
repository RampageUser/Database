from sql import create_db
from students_db import student_db
from major_db import major_db
from department_db import department_db
from lexicon import lexicon_notification, lexicon_inter, lexicon_success


def main() -> None:
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
                print(lexicon_success['Shutdown'])
                break


def choice_option(max: int, min=1) -> int or None:
    try:
        user_option = int(input(lexicon_inter['Menu']))
        while user_option < min or user_option > max:
            user_option = int(input(lexicon_inter['Correct menu']))
        return user_option
    except Exception:
        print('~' * 40)
        print(lexicon_notification['Value err'])
        print('~' * 40)
        return None

def main_menu() -> None:
    print()
    print('-' * 35)
    print('Main menu.')
    print()
    print('1. Work with students database.')
    print('2. Work with majors database.')
    print('3. Work with department database.')
    print('4. Exit.')
    print('-' * 35)
    print()


if __name__ == '__main__':
    main()