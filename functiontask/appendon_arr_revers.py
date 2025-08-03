def sort_numbers():
    l = []
    for _ in range(5):
        l.append(int(input("Enter a number: ")))
    l.sort()
    print("Ascending order:", l)
    l.sort(reverse=True)
    print("Descending order:", l)
sort_numbers()
