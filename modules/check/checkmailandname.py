
def is_valid_email(email):
    if '@' in email and '.' in email:
        try:
            username, domain = email.split('@')
            x, y = domain.split('.')
            return username != '' and x != '' and y != ''
        except ValueError:
            return False
    return False





def validate_name():
    user_input = input("Enter name: ")
    
    if user_input.isalpha():
        print("Valid name")
        return
    else:
        for i in range(4):  
            user_input = input("Invalid name. Try again: ")
        print("Out of range")