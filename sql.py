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


def show_info(table):
    with sqlite3.connect('student_info.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''select * from ?''', (table,))
        result = cursor.fetchall()


def add_data(table, name, major_id=None, department_id=None):
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