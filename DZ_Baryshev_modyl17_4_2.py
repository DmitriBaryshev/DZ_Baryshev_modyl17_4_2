import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('Academy.db')
cursor = conn.cursor()

# Запрос 1: Вывести количество преподавателей кафедры "Software Development"
cursor.execute("SELECT COUNT(*) FROM Employees e JOIN Departments d ON e.department_id = d.department_id WHERE d.department_name = 'Software Development'")
count = cursor.fetchone()[0]
print("Запрос 1:")
print(f"Количество преподавателей на кафедре 'Software Development': {count}")

# Запрос 2: Вывести количество лекций, которые читает преподаватель “Dave McQueen”
cursor.execute("SELECT COUNT(*) FROM Lectures l JOIN Employees e ON l.employee_id = e.employee_id WHERE e.first_name = 'Dave' AND e.last_name = 'McQueen'")
count = cursor.fetchone()[0]
print("\nЗапрос 2:")
print(f"Количество лекций, которые читает преподаватель Dave McQueen: {count}")

# Запрос 3: Вывести количество занятий, проводимых в аудитории “D201”
cursor.execute("SELECT COUNT(*) FROM Lectures WHERE classroom = 'D201'")
count = cursor.fetchone()[0]
print("\nЗапрос 3:")
print(f"Количество занятий, проводимых в аудитории D201: {count}")

# Запрос 4: Вывести названия аудиторий и количество лекций, проводимых в них
cursor.execute("SELECT classroom, COUNT(*) FROM Lectures GROUP BY classroom")
rows = cursor.fetchall()
print("\nЗапрос 4:")
for row in rows:
    print(row)

# Запрос 5: Вывести количество студентов, посещающих лекции преподавателя “Jack Underhill”
cursor.execute("SELECT COUNT(DISTINCT s.student_id) FROM Students s JOIN Enrollments e ON s.student_id = e.student_id JOIN Lectures l ON e.lecture_id = l.lecture_id JOIN Employees emp ON l.employee_id = emp.employee_id WHERE emp.first_name = 'Jack' AND emp.last_name = 'Underhill'")
count = cursor.fetchone()[0]
print("\nЗапрос 5:")
print(f"Количество студентов, посещающих лекции преподавателя Jack Underhill: {count}")

# Запрос 6: Вывести среднюю ставку преподавателей факультета “Computer Science”
cursor.execute("SELECT AVG(hourly_rate) FROM Employees e JOIN Departments d ON e.department_id = d.department_id JOIN Faculties f ON d.faculty_id = f.faculty_id WHERE f.faculty_name = 'Computer Science'")
avg_rate = cursor.fetchone()[0]
print("\nЗапрос 6:")
print(f"Средняя ставка преподавателей факультета Computer Science: {avg_rate}")

# Запрос 7: Вывести минимальное и максимальное количество студентов среди всех групп
cursor.execute("SELECT MIN(num_students), MAX(num_students) FROM Groups")
min_max_students = cursor.fetchone()
print("\nЗапрос 7:")
print(f"Минимальное количество студентов среди всех групп: {min_max_students[0]}")
print(f"Максимальное количество студентов среди всех групп: {min_max_students[1]}")

# Запрос 8: Вывести средний фонд финансирования кафедр
cursor.execute("SELECT AVG(funding) FROM Departments")
avg_funding = cursor.fetchone()[0]
print("\nЗапрос 8:")
print(f"Средний фонд финансирования кафедр: {avg_funding}")

# Запрос 9: Вывести полные имена преподавателей и количество читаемых ими дисциплин
cursor.execute("SELECT e.first_name || ' ' || e.last_name, COUNT(DISTINCT l.lecture_id) FROM Employees e JOIN Lectures l ON e.employee_id = l.employee_id GROUP BY e.employee_id")
rows = cursor.fetchall()
print("Запрос 9:")
for row in rows:
    print(row)

# Запрос 10: Вывести количество лекций в каждый день недели
cursor.execute("SELECT day_of_week, COUNT(*) FROM Lectures GROUP BY day_of_week")
rows = cursor.fetchall()
print("\nЗапрос 10:")
for row in rows:
    print(row)

# Запрос 11: Вывести номера аудиторий и количество кафедр, чьи лекции в них читаются
cursor.execute("SELECT classroom, COUNT(DISTINCT d.department_id) FROM Lectures l JOIN Departments d ON l.department_id = d.department_id GROUP BY classroom")
rows = cursor.fetchall()
print("\nЗапрос 11:")
for row in rows:
    print(row)

# Запрос 12: Вывести названия факультетов и количество дисциплин, которые на них читаются
cursor.execute("SELECT f.faculty_name, COUNT(DISTINCT l.lecture_id) FROM Faculties f JOIN Departments d ON f.faculty_id = d.faculty_id JOIN Lectures l ON d.department_id = l.department_id GROUP BY f.faculty_name")
rows = cursor.fetchall()
print("\nЗапрос 12:")
for row in rows:
    print(row)

# Запрос 13: Вывести количество лекций для каждой пары преподаватель-аудитория
cursor.execute("SELECT e.first_name || ' ' || e.last_name, l.classroom, COUNT(*) FROM Employees e JOIN Lectures l ON e.employee_id = l.employee_id GROUP BY e.employee_id, l.classroom")
rows = cursor.fetchall()
print("\nЗапрос 13:")
for row in rows:
    print(row)

# Закрытие соединения с базой данных
conn.close()
