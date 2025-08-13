# Employee Management System (In-Memory Version)

employees = []  # List to store employee records

# -------------------- FUNCTIONS --------------------
def add_employee(employee_id, first_name, last_name, job_title, salary):
    employees.append({
        "employee_id": employee_id,
        "first_name": first_name,
        "last_name": last_name,
        "job_title": job_title,
        "salary": salary
    })
    print("Employee added successfully.")

def list_employees():
    if not employees:
        print("No employees found.")
    else:
        for emp in employees:
            print(emp)

def find_employee(employee_id):
    for emp in employees:
        if emp["employee_id"] == employee_id:
            print(emp)
            return
    print("Employee not found.")

def update_employee(employee_id, first_name, last_name, job_title, salary):
    for emp in employees:
        if emp["employee_id"] == employee_id:
            emp["first_name"] = first_name
            emp["last_name"] = last_name
            emp["job_title"] = job_title
            emp["salary"] = salary
            print("Employee information updated successfully.")
            return
    print("Employee not found.")

def increase_salary(employee_id, salary_increase):
    for emp in employees:
        if emp["employee_id"] == employee_id:
            emp["salary"] += salary_increase
            print("Salary increased successfully.")
            return
    print("Employee not found.")

def delete_employee(employee_id):
    global employees
    employees = [emp for emp in employees if emp["employee_id"] != employee_id]
    print("Employee deleted successfully.")

def display_filtered_employees(filtered_employees):
    if not filtered_employees:
        print("No employees found based on the specified criteria.")
    else:
        print("Employee_ID | First_Name | Last_Name | Job_Title | Salary")
        print("-" * 60)
        for emp in filtered_employees:
            print(f"{emp['employee_id']:11} | {emp['first_name']:10} | {emp['last_name']:9} | {emp['job_title']:9} | {emp['salary']:.2f}")

def filter_employees():
    print("\nFilter Employees:")
    print("1. Filter by First Name")
    print("2. Filter by Last Name")
    print("3. Filter by Job Title")
    print("4. Filter by Salary Range")
    print("5. Back to Main Menu")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        first_name = input("Enter First Name: ")
        filtered = [emp for emp in employees if emp["first_name"].lower() == first_name.lower()]
        display_filtered_employees(filtered)

    elif choice == '2':
        last_name = input("Enter Last Name: ")
        filtered = [emp for emp in employees if emp["last_name"].lower() == last_name.lower()]
        display_filtered_employees(filtered)

    elif choice == '3':
        job_title = input("Enter Job Title: ")
        filtered = [emp for emp in employees if emp["job_title"].lower() == job_title.lower()]
        display_filtered_employees(filtered)

    elif choice == '4':
        try:
            min_salary = float(input("Enter Minimum Salary: "))
            max_salary = float(input("Enter Maximum Salary: "))
            filtered = [emp for emp in employees if min_salary <= emp["salary"] <= max_salary]
            display_filtered_employees(filtered)
        except ValueError:
            print("Invalid salary input.")

    elif choice == '5':
        return
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

# -------------------- MAIN MENU --------------------
while True:
    print("\nEmployment Management System")
    print("1. Add Employee")
    print("2. List Employees")
    print("3. Find Employee by ID")
    print("4. Update Employee Information")
    print("5. Delete Employee")
    print("6. Give Salary Increase")
    print("7. Filter and List Employees")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter employee ID: ")
        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        job = input("Enter job title: ")
        try:
            sal = float(input("Enter salary: "))
            add_employee(emp_id, fname, lname, job, sal)
        except ValueError:
            print("Invalid salary input.")
    elif choice == "2":
        list_employees()
    elif choice == "3":
        emp_id = input("Enter employee ID: ")
        find_employee(emp_id)
    elif choice == "4":
        emp_id = input("Enter employee ID to update: ")
        fname = input("Enter updated first name: ")
        lname = input("Enter updated last name: ")
        job = input("Enter updated job title: ")
        try:
            sal = float(input("Enter updated salary: "))
            update_employee(emp_id, fname, lname, job, sal)
        except ValueError:
            print("Invalid salary input.")
    elif choice == "5":
        emp_id = input("Enter employee ID to delete: ")
        delete_employee(emp_id)
    elif choice == "6":
        emp_id = input("Enter employee ID for salary increase: ")
        try:
            inc = float(input("Enter increase amount: "))
            increase_salary(emp_id, inc)
        except ValueError:
            print("Invalid salary increase amount.")
    elif choice == "7":
        filter_employees()
    elif choice == "8":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
