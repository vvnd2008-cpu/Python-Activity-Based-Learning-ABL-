# Project 9: Integrated University Fee and Eligibility Audit
student_name = input("Enter student name: ").strip()
total_fee = float(input("Enter total fee: "))
fee_paid = float(input("Enter fee paid: "))
attendance = float(input("Enter attendance percentage: "))
if ( total_fee <= 0
    or fee_paid < 0
    or fee_paid > total_fee
    or attendance < 0
    or attendance > 100 ):
    print("Invalid student details.")
else:
    pending_fee = total_fee - fee_paid
    print("\nStudent Name:", student_name)
    print("Total Fee:", total_fee)
    print("Fee Paid:", fee_paid)
    print("Pending Fee:", round(pending_fee, 2))
    print("Attendance:", attendance, "%")
    if pending_fee == 0 and attendance >= 75:
        print("Eligible for examination.")
    else:
        print("Not eligible for examination.")
        if pending_fee > 0:
            print("Reason: Fee payment incomplete.")
        if attendance < 75:
            print("Reason: Attendance below 75%.")
