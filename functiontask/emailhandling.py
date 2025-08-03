
def is_valid_email(email):
    if '@' in email and '.' in email:
        try:
            username, domain = email.split('@')
            x, y = domain.split('.')
            return username != '' and x != '' and y != ''
        except ValueError:
            return False
    return False


for i in range(5):
    email = input("Enter your email: ").strip()
    if is_valid_email(email):
        print(" Valid email")
        break
    else:
        print("Invalid email")
else:
    raise ValueError("you enter over 5 time ")
