import sqlite3
from lexicon import lexicon_error, lexicon_success


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
        print(lexicon_success['Created'])


def show_all_info(table: str) -> None or list:
    with sqlite3.connect('student_info.db') as conn:
        cursor = conn.cursor()
        if table == 'Students':
            cursor.execute('''select Students.Name, Majors.Name, Department.Name 
                                          from Students, Majors, Department
                                          where Students.MajorID = Majors.MajorID
                                          and Students.DepartmentID = Department.DepartmentID''')
            print()
            for counter, i in enumerate(cursor.fetchall(), start=1):
                print(f'{counter:>3}.\n{"Name:":20}{i[0]}\n{"Major:":20}{i[1]}\n{"Department:":20}{i[2]}')
                print()
        else:
            id = []
            if table == 'Department':
                cursor.execute('''select DepartmentID, Name from Department''')
            elif table == 'Majors':
                cursor.execute('''select MajorID, Name from Majors''')
            print()
            print(f'{"ID":15}Name')
            print('-' * 25)
            for i in cursor.fetchall():
                id.append(i[0])
                print(f'{i[0]:<15}{i[1]}')
            print()
            return id


def add_data(table: str, name: str, major_id=None, department_id=None) -> None:
    try:
        with sqlite3.connect('student_info.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''pragma foreign_keys = on''')
            if table == 'Majors':
                cursor.execute('''insert into Majors (Name) values (?)''', (name,))
            elif table == 'Department':
                cursor.execute('''insert into Department (Name) values (?)''', (name,))
            elif table == 'Students':
                cursor.execute('''insert into Students (Name, MajorID, DepartmentID) 
                                  values (?,?,?)''', (name, major_id, department_id))
            conn.commit()
    except sqlite3.IntegrityError:
        print('~'* 48)
        print(lexicon_error['ID'])
        print('~' * 48)
    else:
        print(lexicon_success['Added'])


def find_info(table: str, name: str) -> False or list:
    with sqlite3.connect('student_info.db') as conn:
        cursor = conn.cursor()
        if table == 'Students':
            cursor.execute('''select StudentId, Name from Students where Name = ?''', (name,))
        elif table == 'Majors':
            cursor.execute('''select MajorID, Name from Majors where Name = ?''', (name,))
        else:
            cursor.execute('''select DepartmentID, Name from Department where Name = ?''', (name,))
        result = cursor.fetchall()
        if result:
            print('Was found:')
            id = []
            for i in result:
                print(f'{i[0]:>3}: {i[1]}')
                id.append(i[0])
            return id
        else:
            return False


def delete_info(table: str, id: int) -> None:
    try:
        with sqlite3.connect('student_info.db') as conn:
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys = on')
            if table == 'Students':
                cursor.execute('''delete from Students where StudentID = ?''', (id,))
            elif table == 'Majors':
                cursor.execute('''delete from Majors where MajorID = ?''', (id,))
            else:
                cursor.execute('''delete from Department where DepartmentID = ?''', (id,))
            count = cursor.rowcount
            print(f'was removed {count} row from {table}')
    except sqlite3.IntegrityError:
        print('~' * 54)
        print(lexicon_error['Reference'])
        print('~' * 54)


def change_info(table: str, id: int, name: str, speciality = None, department = None):
    with sqlite3.connect('student_info.db') as conn:
        cursor = conn.cursor()
        if table == 'Students':
            cursor.execute('''update Students set Name = ?, MajorID = ?, DepartmentID = ?
                              where StudentID = ?''', (name, speciality, department, id))
        elif table == 'Majors':
            cursor.execute('''update Majors set Name = ? where MajorID = ?''', (name, id))
        else:
            cursor.execute('''update Department set Name = ? where DepartmentID = ?''', (name, id))
        conn.commit()
        print(lexicon_success['Changed'])
