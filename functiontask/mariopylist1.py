def mario_list():
    l = [" ", " ", " ", " ", " "]
    for i in l:
        l.append("*")
        l.remove(" ")
        print(l)
mario_list()
