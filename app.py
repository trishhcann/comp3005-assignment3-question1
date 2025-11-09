import psycopg2

# Database Connection Helper 

def get_connection():
    """
    Returns a connection object to the PostgreSQL database.
    Update the database, user, and password to match the setup.
    """
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="studentdb",      
        user="postgres",          
        password="postgres"  
    )



def getAllStudents():
    # Retrieves and displays all records from the students table
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT student_id, first_name, last_name, email, enrollment_date FROM students;")
    rows = cur.fetchall()

    print("\n--- All Students ---")
    for row in rows:
        student_id, first_name, last_name, email, enrollment_date = row
        print(f"{student_id}: {first_name} {last_name}, {email}, enrolled {enrollment_date}")

    cur.close()
    conn.close()


def addStudent(first_name, last_name, email, enrollment_date):
    # Inserts a new student record into the students table.
    conn = get_connection()
    cur = conn.cursor()

    sql = """
        INSERT INTO students (first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s);
    """
    cur.execute(sql, (first_name, last_name, email, enrollment_date))
    conn.commit()

    print("Student added successfully.")

    cur.close()
    conn.close()


def updateStudentEmail(student_id, new_email):
    # Updates the email address for a student with the specified student ID
    conn = get_connection()
    cur = conn.cursor()

    sql = "UPDATE students SET email = %s WHERE student_id = %s;"
    cur.execute(sql, (new_email, student_id))
    conn.commit()

    if cur.rowcount == 0:
        print("No student found with that ID.")
    else:
        print("Email updated successfully.")

    cur.close()
    conn.close()


def deleteStudent(student_id):
    # Deletes the record of the student with the specified student ID
    conn = get_connection()
    cur = conn.cursor()

    sql = "DELETE FROM students WHERE student_id = %s;"
    cur.execute(sql, (student_id,))
    conn.commit()

    if cur.rowcount == 0:
        print("No student found with that ID.")
    else:
        print("Student deleted successfully.")

    cur.close()
    conn.close()


# Menu Interface

def main():
    while True:
        print("\nStudent Management Menu")
        print("Please make a choice: ")
        print("     1. View all students")
        print("     2. Add a student")
        print("     3. Update a student's email")
        print("     4. Delete a student")
        print("     5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            getAllStudents()

        elif choice == "2":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            email = input("Email: ")
            enrollment_date = input("Enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)

        elif choice == "3":
            student_id = int(input("Student ID to update: "))
            new_email = input("New email: ")
            updateStudentEmail(student_id, new_email)

        elif choice == "4":
            student_id = int(input("Student ID to delete: "))
            deleteStudent(student_id)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
