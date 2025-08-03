def print_mariopyr(n):
    for i in range(n + 1):
        print(" " * (n - i) + "*" * i)



def mario_list():
    l = [" ", " ", " ", " ", " "]
    for i in l:
        l.append("*")
        l.remove(" ")
        print(l)