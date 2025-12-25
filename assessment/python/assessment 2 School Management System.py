class SchoolManagement:
    def __init__(self):
        self.students = {}
        self.student_id=1    
        

    def newAdmission(self):
        name = input("Enter Student Name: ")

        # Validate Age
        try:
            age = int(input("Enter Age (5-18): "))
            if age < 5 or age > 18:
                print(" Age must be between 5 and 18!")
                return

        except ValueError:
            print(" Age must be a number!")
            return

        # Validate Class
        try:
            student_class = int(input("Enter Class (1-12): "))
            if student_class <1 or student_class >12:
                print(" Class must be between 1 and 12!")
                return
        except ValueError:
            print(" Class must be a number!")
            return

        # Validate Mobile
        mobile = input("Enter Guardian Mobile :")
        if len(mobile) != 10 or not  mobile.isdigit():
            print(" Invalid Mobile Number!")
            return


        # Assign Unique ID
        student_id = self.student_id
        self.student_id += 1
        self.students[student_id] = {
    "name": name,
    "age": age,
    "class": student_class,
    "mobile": mobile
}

        print("\n Admission Successful!")
        print(f"Student ID: {student_id}")
        print(f"Name: {name}, Age: {age}, Class: {student_class}, Mobile: {mobile}")

    def viewStudent(self):
        try:
            Student_id = int(input("Enter Student ID to view details: "))
        except ValueError:
            print(" Invalid ID!")
            return

        if Student_id in self.students:
            data = self.students[Student_id]
            print("\ Student Details:")
            print(f"ID: {Student_id}")
            print(f"Name: {data['name']}")
            print(f"Age: {data['age']}")
            print(f"Class: {data['class']}")
            print(f"Mobile: {data['mobile']}")
        else:            
            print(" Student not found!")
        #print(self.students)

    def updateStudent(self):
        try:
            student_id = int(input("Enter Student ID to update: "))
        except ValueError:
            print(" Invalid ID!")
            return

        if student_id not in self.students:
            print(" Student not found!")
            return

        print("\n1) Update Mobile Number")
        print("2) Update Class")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print(" Enter a valid option!")
            return

        if choice == 1:
            new_mobile = input("Enter new Mobile (10 digits): ")
            if new_mobile.isdigit() and len(new_mobile) == 10:
                self.students[student_id]["mobile"] = new_mobile
                print(" Mobile updated successfully!")
            else:
                print(" Invalid Mobile Number!")

        elif choice == 2:
            try:
                new_class = int(input("Enter new Class (1-12): "))
                if 1 <= new_class <= 12:
                    self.students[student_id]["class"] = new_class
                    print("Class updated successfully!")
                else:
                    print(" Class must be between 1-12!")
            except ValueError:
                print(" Invalid Class Value!")
        else:
            print(" Invalid Choice!")

    def removeStudent(self):
        try:
            student_id = int(input("Enter Student ID to remove: "))
        except ValueError:
            print(" Invalid ID!")
            return

        if student_id in self.students:
            del self.students[student_id]
            print("Student record removed successfully!")
        else:
            print(" Student not found!")


# -------- Main Code --------
obj = SchoolManagement()

while True:
    print("\n--- School Management Menu ---")
    print("1. New Admission")
    print("2. View Student Details")
    print("3. Update Student Info")
    print("4. Remove Student Record")
    print("5. Exit")

    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print(" Please enter a valid number!")
        continue

    match ch:
        case 1: obj.newAdmission()
        case 2: obj.viewStudent()
        case 3: obj.updateStudent()
        case 4: obj.removeStudent()
        case 5:
            print("Exiting System...")
            break
        case _:
            print("Invalid Choice!")
