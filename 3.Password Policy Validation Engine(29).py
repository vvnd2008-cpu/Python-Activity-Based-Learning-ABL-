# Password Policy Validation Engine
password = input("Enter a password to check: ")
length_ok = len(password) >= 8
has_upper = False
has_lower = False
has_digit = False
has_special = False
for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_special = True
print("At least 8 characters:", length_ok)
print("Contains uppercase:", has_upper)
print("Contains lowercase:", has_lower)
print("Contains a digit:", has_digit)
print("Contains a special character:", has_special)
if (length_ok and has_upper and has_lower
        and has_digit and has_special):
    print("Password meets the policy.")
else:
    print("Password does not meet the policy.")
