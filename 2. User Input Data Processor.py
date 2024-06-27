#Task 1

def name_processor():
    first_name = input("Whats your first name: ")
    last_name = input("Whats your last name: ")

    if len(first_name) < 2:
        print("Error, need more than 2 characters in first name.")
    if len(last_name) < 2:
        print("Error, need more than 2 characters in last name.")
    else:
        print("Name is valid!")
    
name_processor()

