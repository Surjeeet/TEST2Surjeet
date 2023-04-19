phoneDirectory = {}

phoneDirectory = {}

print("WELCOME TO THE GRANN'S PHONE DIRECTORY MENU\n")

while True:
    print("1. Add a record")
    print("2. Search a record")
    print("3. Change a record")
    print("4. Delete a record")
    print("5. Quit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        name = input("\nEnter name: ")
        phone_number = input("Enter your 10-digit phone number: ")
        if len(phone_number) != 10:
            print("Invalid phone number. Phone number must be 10-digit.")
        else:
           phoneDirectory[name] = phone_number
           print("Record added")

    elif choice == 2:
        name = input("\nEnter name to search: ")
        if name in phoneDirectory:
            print(name + ": " + phoneDirectory[name])
        else:
            print("No record found")

    elif choice == 3:
        name = input("\nEnter name: ")
        if name in phoneDirectory:
            phone_number = input("Enter new 10-digit phone number: ")
            if len(phone_number) != 10:
                print("Invalid phone number. Phone number must be 10-digit.")
            else:
               phoneDirectory[name] = phone_number
               print("Record updated")


    elif choice == 4:
        name = input("\nEnter name: ")
        if name in phoneDirectory:
            del phoneDirectory[name]
            print("\nRecord deleted")
        else:
            print("No record found")

    elif choice == 5:
        break

    else:
        print("Invalid choice")