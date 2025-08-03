def validate_name():
    user_input = input("Enter name: ")
    
    if user_input.isalpha():
        print("Valid name")
        return
    else:
        for i in range(4):  
            user_input = input("Invalid name. Try again: ")
        print("Out of range")
validate_name()