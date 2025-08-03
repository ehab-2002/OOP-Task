def sort_numbers():
    l = []
    for _ in range(5):
        l.append(int(input("Enter a number: ")))
    l.sort()
    print("Ascending order:", l)
    l.sort(reverse=True)
    print("Descending order:", l)


def find_i_locations():
    input_string = input("Enter a string: ")
    locations = []
    for i in range(len(input_string)):
        if input_string[i] == 'i' or input_string[i] == 'I':
            locations += [i]
            print("Location of 'i':", i)