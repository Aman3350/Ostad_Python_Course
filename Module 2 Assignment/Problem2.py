exit=False

while exit==False:
    name=input("\nEnter your name: ")

    file=open("name.txt", "a")
    file.write(name+"\n")
    file.close()
    print("Name saved successfully")

    while True:
        a=input("\nExit(Y/N): ")
        if a=="Y":
            print()
            exit=True
            break
        elif a=="N":
            break
        else:
            print("Invalid Input. \"Y\" for \"YES\" and \"N\" for \"NO\".")
