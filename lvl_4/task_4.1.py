# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


import sqlite3

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """CREATE TABLE IF NOT EXISTS School (
School_Id INTEGER NOT NULL PRIMARY KEY,
School_Name TEXT NOT NULL,
Place_Count INTEGER NOT NULL);"""
query2 = """CREATE TABLE IF NOT EXISTS Students (
Student_Id INTEGER NOT NULL,
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL PRIMARY KEY);"""
query3 = """INSERT or REPLACE INTO School (School_Id, School_Name, Place_Count)
VALUES
(1,'Протон',200),
(2,'Преспектива',300),
(3,'Спектр',400),
(4,'Содружество',500);"""
query4 = """INSERT or REPLACE INTO Students (Student_Id, Student_Name, School_Id)
VALUES
(201,'Иван',1),
(202,'Петр',2),
(203,'Анастасия',3),
(204,'Игорь',4);"""
query5 = 'DROP TABLE Students;'
query6 = 'DROP TABLE School;'
cursor.execute(query)
cursor.execute(query2)
cursor.execute(query3)
cursor.execute(query4)
connection.commit()
connection.close()



def get_conn():
  connection = sqlite3.connect("teachers.db")
  return connection

def close_conn(connection):
  if connection:
    connection.close()

def get_student_info(Student_Id):
  try:
    connection = get_conn()
    cursor = connection.cursor()
    sql_query = """SELECT Students.Student_Id, Students.Student_Name, School.School_Id, School.School_Name
                   FROM Students
                   JOIN School ON Students.School_Id = School.School_Id
                   WHERE Student_Id = ?;"""
    cursor.execute(sql_query, (Student_Id,))
    result = cursor.fetchone()
    close_conn(connection)
    print ("ID Студента:", result[0])
    print ("Имя студента:", result[1])
    print ("ID школы:", result[2])
    print ("Название школы:", result[3])
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка: ", error)

