from sql import add_data, show_all_info, find_info, delete_info, change_info
from lexicon import lexicon_inter, lexicon_notification


def student_db() -> None:
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
        change_student()
    elif user_option == 5:
        find_student()
    elif user_option == 6:
        return
    student_db()


def submenu_student() -> None:
    print()
    print('-' * 35)
    print('Students database.')
    print()
    print('1. Show all students.')
    print('2. Add new student.')
    print('3. Remove student.')
    print('4. Change info about student.')
    print('5. Find student.')
    print('6. Back.')
    print('-' * 35)
    print()


def add_student() -> None:
    try:
        student_name: str = input(lexicon_inter['Name'])
        majors_id = show_all_info(table='Majors')
        major: int = int(input(lexicon_inter['Exist ID']))
        departments_id = show_all_info(table='Department')
        department: int = int(input(lexicon_inter['Exist ID']))
        if (major in majors_id) and (department in departments_id):
            add_data(table='Students', name=student_name, major_id=major, department_id=department)
        else:
            print(lexicon_notification['ID'])
    except ValueError:
        print('~' * 40)
        print(lexicon_notification['Value err'])
        print('~' * 40)


def delete_student() -> None:
    student: str = input(lexicon_inter['Remove'])
    result = find_info(table='Students', name=student)
    if result:
        id: int = int(input(lexicon_inter['ID']))
        if id in result:
            delete_info(table='Students', id=id)
        else:
            print(lexicon_notification['ID'])


def find_student() -> None:
    student: str = input(lexicon_inter['Name'])
    result = find_info(table='Students', name=student)
    if not result:
        print(lexicon_notification['Not find'])


def change_student() -> None:
    student: str = input(lexicon_inter['Name'])
    result = find_info(table='Students', name=student)
    if result:
        if len(result) == 1:
            change_student_info(id=result[0])
        else:
            correct_id: int = int(input(lexicon_inter['ID to change']))
            if correct_id in result:
                change_student_info(id=correct_id)
            else:
                print(lexicon_notification['ID'])
    else:
        print(lexicon_notification['Not find'])


def change_student_info(id: int) -> None:
    try:
        name: str = input(lexicon_inter['New name'])
        id_major = show_all_info(table='Majors')
        new_id_major: int = int(input(lexicon_inter['ID']))
        id_department = show_all_info(table='Department')
        new_id_department: int = int(input(lexicon_inter['ID']))
        if (new_id_major in id_major) and (new_id_department in id_department):
            change_info(table='Students', id=id, name=name,
                        speciality=new_id_major, department=new_id_department)
        else:
            print(lexicon_notification['ID'])
    except ValueError:
        print('~' * 40)
        print(lexicon_notification['Value err'])
        print('~' * 40)