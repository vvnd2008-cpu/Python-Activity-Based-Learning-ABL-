n = int(input("Enter number of student records: "))

if n <= 0:
    print("Enter a positive number of records.")
else:
    records = []
    for i in range(n):
        print("\nStudent", i + 1)
        student_id = input("Enter student ID: ").strip()
        name = input("Enter student name: ").strip()
        email = input("Enter student email: ").strip()
        marks = float(input("Enter marks (0-100): "))
        records.append([student_id, name, email, marks])

    error_count = 0
    print("\nStudent Record Validation Report")
    for record in records:
        student_id, name, email, marks = record
        errors = []

        if not (student_id.startswith("STU") and student_id[3:].isdigit()):
            errors.append("Invalid student ID")

        parts = email.split("@")
        email_valid = (
                len(parts) == 2 and parts[0] != "" and parts[1] != ""
                and " " not in email and "." in parts[1]
                and not parts[1].startswith(".") and not parts[1].endswith(".")
        )
        if not email_valid:
            errors.append("Invalid email")
        if marks < 0 or marks > 100:
            errors.append("Invalid marks")

        id_count = 0
        for other_record in records:
            if other_record[0] == student_id:
                id_count += 1
        if id_count > 1:
            errors.append("Duplicate student ID")

        print("\nName:", name)
        print("Student ID:", student_id)
        if errors:
            print("Status: Inconsistent")
            for error in errors:
                print("-", error)
            error_count += 1
        else:
            print("Status: Valid")

    print("\nTotal records:", len(records))
    print("Records with errors:", error_count)
    print("Records without errors:", len(records) - error_count)