attended=int(input("Enter classes attended: "))
total=int(input("Enter total classes conducted: "))

if total<=0 or attended<0 or attended>total:
    print("Invalid attendance details.")
else:
    percentage=(attended/total)*100
    print(f"Current attendance:{percentage:.2f}%" )
    required=75
    if percentage>=required:
        print("You have the required attendance.")
        print("Additional classes needed:0")
    else:
        extra=0
        while((attended+extra)/(total+extra))*100<required:
            extra+=1
        print("Attendance is below 75%.")
        print("Additional consecutive classes needed:",extra)
        final_percentage=(attended+extra)/(total+extra)*100
        print(f"Final attendance:{final_percentage:.2f}%")