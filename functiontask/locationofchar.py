def find_i_locations():
    input_string = input("Enter a string: ")
    locations = []
    for i in range(len(input_string)):
        if input_string[i] == 'i' or input_string[i] == 'I':
            locations += [i]
            print("Location of 'i':", i)
find_i_locations()
