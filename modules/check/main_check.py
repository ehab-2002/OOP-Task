from checkmailandname import is_valid_email
for i in range(5):
    email = input("Enter your email: ").strip()
    if is_valid_email(email):
        print(" Valid email")
        break
    else:
        print("Invalid email")
else:
    raise ValueError("you enter over 5 time ")

from checkmailandname import validate_name
validate_name()