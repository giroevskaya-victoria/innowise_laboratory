import sqlite3

connection = sqlite3.connect('school.db')
cursor = connection.cursor()

cursor.execute(  # Create table "students"
    '''
    CREATE TABLE students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        birth_year INTEGER
    );
    '''
)

cursor.execute(  # Create table "grades"
    '''
    CREATE TABLE grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject TEXT,
        grade INTEGER,
        FOREIGN KEY (student_id) REFERENCES students (id)
    );
    '''
)

cursor.execute(  # Insert data into table "students"
    '''
    INSERT INTO students (full_name, birth_year) VALUES 
        ('Alice Johnson', 2005),
        ('Brian Smith', 2004),  
        ('Carla Reyes', 2006),
        ('Daniel Kim', 2005),
        ('Eva Thompson', 2003),
        ('Felix Nguyen', 2007),
        ('Grace Patel', 2005),
        ('Henry Lopez', 2004),
        ('Isabella Martinez', 2006);
    '''
)

cursor.execute(  # Insert data into table "grades"
    '''
    INSERT INTO grades (student_id, subject, grade) VALUES 
        (1, 'Math', 88),  
        (1, 'English', 92),  
        (1, 'Science', 85),  
        
        (2, 'Math', 75),  
        (2, 'History', 83),  
        (2, 'English', 79), 
         
        (3, 'Science', 95),  
        (3, 'Math', 91),  
        (3, 'Art', 89),  
        
        (4, 'Math', 84),  
        (4, 'Science', 88),  
        (4, 'Physical Education', 93),  
        
        (5, 'English', 90),  
        (5, 'History', 85),  
        (5, 'Math', 88),  
        
        (6, 'Science', 72),  
        (6, 'Math', 78),  
        (6, 'English', 81),
          
        (7, 'Art', 94),
        (7, 'Science', 87),  
        (7, 'Math', 90), 
         
        (8, 'History', 77),  
        (8, 'Math', 83),  
        (8, 'Science', 80),  
        
        (9, 'English', 96),  
        (9, 'Math', 89),  
        (9, 'Art', 92);
    '''
)

cursor.execute("SELECT * FROM students")
all_students = cursor.fetchall()
print(f"1. {all_students}")

cursor.execute("SELECT * FROM grades")
all_grades = cursor.fetchall()
print(f"2. {all_grades}")


cursor.execute(  # pick out Alice's grades
    '''
    SELECT grade 
    FROM students LEFT JOIN grades ON grades.student_id = students.id
    WHERE full_name = 'Alice Johnson';
    '''
)
alice_grades = cursor.fetchall()
print(f"3. Alice's grades: {alice_grades}")

cursor.execute(  # pick out average student's grades
    '''
    SELECT full_name, ROUND(AVG(grade), 1)
    FROM students LEFT JOIN grades ON grades.student_id = students.id
    GROUP BY 1;
    '''
)
avg_grade = cursor.fetchall()
print(f"4. Average student's grades: {avg_grade}")

cursor.execute(  # pick out students born after 2004
    '''
    SELECT full_name
    FROM students LEFT JOIN grades ON grades.student_id = students.id
    WHERE birth_year > 2004
    GROUP BY 1;
    '''
)
students_2004 = cursor.fetchall()
print(f"5. Students born after 2004: {students_2004}")

cursor.execute(  # pick out subjects and their average grades
    '''
    SELECT subject, ROUND(AVG(grade), 1)
    FROM students RIGHT JOIN grades ON grades.student_id = students.id
    GROUP BY 1;
    '''
)
subjects_avg_grades = cursor.fetchall()
print(f"6. Subjects and their average grades: {subjects_avg_grades}")

cursor.execute(  # pick out top 3 students
    '''
    SELECT full_name, ROUND(AVG(grade), 1)
    FROM students LEFT JOIN grades ON grades.student_id = students.id
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 3;
    '''
)
top_3 = cursor.fetchall()
print(f"7. Top 3 students with highest average grades: {top_3}")

cursor.execute(  # pick out students with grates below 80
    '''
    SELECT full_name
    FROM students LEFT JOIN grades ON grades.student_id = students.id
    WHERE grade < 80
    GROUP BY 1
    '''
)
below_80 = cursor.fetchall()
print(f"7. Students who have scored below 80 in any subject: {below_80}")

connection.close()
