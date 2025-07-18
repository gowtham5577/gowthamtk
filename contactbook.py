print("**//contact book //**".upper())
contact = {}
while True:
    print("1.create contact\n2.view contact\n3.update contact\n4.delete  contact\n5.search contcat\n6 count contact\n7.exit")

    choice = input("enter your choice:")
    if choice == '1':
        name = input("enter your contact name:")
        if name in contact:
            print(f"contact {name} already exited.")
        else:
            phno = input("enter phone number:")
            age = input("enter  age:")
            email = input("enter  email:")
            contact[name] = {'phno': phno, 'age': int(age), 'email': (email)}
            print(f"contact name {name} created successfully!")
    elif choice == '2':
        search_name = input("enter a contact name to view:")
        if search_name in contact:
            contacts = contact[name]
            print(f"name:{name}, phno:{phno},age:{age},email:{email}")
        else:
            print("contact not found!")
    elif choice == '3':
        name = input("enter a contact name you want to update:")
        if name in contact:
            phno = int(input("enter a updated phno:"))
            age = input("enter a updated age:")
            email = input("enter a updated email:")
            contact[name] = {'phno': phno, 'age': int(age), 'email': (email)}
            print(f"contact {name} updated successfully!")
        else:
            print("contact not found!")
    elif choice == '4':
        name = input("enter contact name to delete:")
        if name in contact:
            del contact[name]
            print(f"contact {name} deleted successfully!!")
        else:
            print("contact not found!")
    elif choice == '5':
        search_name = input("enter  contact name to search:")
        found = False
        for name, contacts in contact.items():
            if search_name.lower() in name.lower():
                print(f"name:{name}, phno:{phno},age:{age},email:{email}")
                found = True
            if not found:
                print("contact not found:")
    elif choice == '6':
        print(f"Total number of contact is {len(contact)}")
    elif choice == '7':
        print("contact app exited successfully!")
        break
    else:
        print("invalid input..")




