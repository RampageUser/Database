import sqlite3


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


def show_info(table) -> None:
    with sqlite3.connect('student_info.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''select * from ?''', (table,))
        result = cursor.fetchall()


def show_all_info(table: str) -> None:
    with sqlite3.connect('student_info.db') as conn:
        cursor = conn.cursor()
        if table == 'Students':
            cursor.execute('''select Students.Name, Majors.Name, Department.Name 
                                          from Students, Majors, Department
                                          where Students.MajorID = Majors.MajorID
                                          and Students.DepartmentID = Department.DepartmentID''')
            print()
            for counter, i in enumerate(cursor.fetchall(), start=1):
                print(f'{counter:>3}. {i[0]:15}{i[1]:15}{i[2]:15}')
                print()
        else:
            if table == 'Department':
                cursor.execute('''select Name from Department''')
            elif table == 'Majors':
                cursor.execute('''select Name from Majors''')
            print()
            for counter, i in enumerate(cursor.fetchall(), start=1):
                print(f'{counter:>3}. {i[0]}')
                print()


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
        print('Incorrect value, you should inter en existed ID!')
        print('~' * 48)
    else:
        print('Info has been added')


def find_info(table: str, name: str):
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
            print(f'Was found:')
            id = []
            for i in result:
                print(f'{i[0]:>3}: {i[1]}')
                id.append(i[0])
            return id
        else:
            return False


def delete_info(table: str, id: int) -> None:
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