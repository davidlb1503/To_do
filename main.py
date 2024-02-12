
def create():
    pass

def view():
    pass

def delete():
    pass


def main():
    option = int(input())

    while(option):
        print("Press 1 to create")
        print("Press 2 to view all the notes")
        print("Press 3 to delete a note")
        print("Press 0 to exit")

        if option == 1:
            create()
        elif option == 2:
            view()
        elif option == 3:
            delete()
        option = int(input())

main()
        
