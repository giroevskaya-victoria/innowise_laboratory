def add_student():  # function 1. Add a new student
    new_name = input("What's new student's name? ").title()
    is_student = False
    for i in students:
        if i['name'] == new_name:
            is_student = True
    if is_student:
        print("Such user already exists")
    else:
        list_grades = []
        students.append({'name': new_name, 'grades': list_grades})
        print(f'New student ({new_name}) added')


def add_grades():  # function 2. Add a grades for a student
    stud_name = input("Enter a student's name: ").title()
    is_student = False
    for i in students:
        if i['name'] == stud_name:
            is_student = True
            done = True
            while done:
                try:
                    grade = input("Enter a grade (or 'done' to finish it): ")
                    if grade.lower() == 'done':
                        done = False
                    else:
                        grade = int(grade)
                        if (grade >= 0) and (grade <= 100):
                            i['grades'].append(grade)
                        else:
                            print("Grades only can be between 0 and 100")
                except ValueError:
                    print("Error: Input an integer number[0; 100] or 'done'")
                except Exception as ex:
                    print(f"Something went wrong. Error: {ex}")
    if not is_student:
        print("There's no student with such name")


def show_reports():  # function 3. Show report (all students)

    avg_stud_grades = []

    if not students:
        print("There's no students")
    else:
        for i in students:
            try:
                average = round(sum(i['grades'])/len(i['grades']), 1)
                avg_stud_grades.append(average)
                print(f"{i['name']}'s average grade is {average}")
            except ZeroDivisionError:
                print(f"{i['name']}'s average grade is N/A")
            except Exception as ex:
                print(f"Something went wrong. Error: {ex}")

        if not avg_stud_grades:
            print("All the students have no grades")
        else:
            print('-' * 30)
            print(f"Max Average: {max(avg_stud_grades)}")
            print(f"Min Average: {min(avg_stud_grades)}")
            print(f"Overall Average: {round(sum(avg_stud_grades)/len(avg_stud_grades), 1)}")
            print('-' * 30)


def top_performer():  # Function 4. Find top performer
    if not students:
        print("There's no students")
    else:
        students_with_grades = [i for i in students if i['grades']]
        if not students_with_grades:
            print("All the students have no grades")
        else:
            top_student = max(students_with_grades, key=lambda x: round(sum(x['grades'])/len(x['grades']), 1))
            print(f"The student with the highest average is {top_student['name']} "
                  f"with a grade of {round(sum(top_student['grades'])/len(top_student['grades']), 1)}")


students = []

is_exit = True
while is_exit:  # a menu loop
    try:
        print('-' * 31)
        choice = int(input("Type number to choose function: "
                           "\n\t1. Add a new student\n\t2. Add a grades for a student"
                           "\n\t3. Show report(all students)\n\t4. Find top performer\n\t5. Exit\n"))
        match choice:
            case 1:
                add_student()
            case 2:
                add_grades()
            case 3:
                show_reports()
            case 4:
                top_performer()
            case 5:  # Function 5. Exit
                is_exit = False














                print("The program is finished")
            case _:
                print('Choose one of these numbers (1-5)')

    except ValueError:
        print('Error: Input a number(1-5)')
    except Exception as error:
        print(f"Something went wrong. Error: {error}")
