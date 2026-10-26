email = input("Enter student email: ").strip()
student_id = input("Enter student ID: ").strip()

parts = email.split("@")
email_valid = (
        len(parts) == 2
        and parts[0] != ""
        and parts[1] != ""
        and " " not in email
        and "." in parts[1]
        and not parts[1].startswith(".")
        and not parts[1].endswith(".")
)
id_valid = (
        student_id.startswith("STU")
        and student_id[3:].isdigit()
        and len(student_id) > 3
)
print("Email:", "Valid" if email_valid else "Invalid")
print("Student ID:", "Valid" if id_valid else "Invalid")
