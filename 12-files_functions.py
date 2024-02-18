
def add_3names():
    name1 = input("enter first name:")
    name2 = input("enter second name:")
    name3 = input("enter third name:")

    f = open("names.txt","a")
    f.write("\n"+name1)
    f.write("\n"+name2)
    f.write("\n"+name3)
    f.close()


def print_names_from_file():
    f = open("names.txt", "r")
    for x in f:
        print(f"hello {x}",end='')
    f.close()  # close the file

add_3names()
print_names_from_file()
