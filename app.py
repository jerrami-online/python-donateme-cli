from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

# Task 2: Show homepage and initialize app data

database = {"admin": "password123"}
donations = []
authorized_user = ""

"""

show_homepage()

if authorized_user == "":
    print("You must be logged in to donate.")
else:
    print(f"Logged in as: {authorized_user}")
    
"""


# Task 3: Handle user input

"""

while True:

    option = input("Choose an option: ")

    if option == "1":

        print("TODO: Write Login Functionality")

    elif option == "2":

        print("TODO: Write Register Functionality")

    elif option == "3":

        print("TODO: Write Donate Functionality")

    elif option == "4":

        print("TODO: Write Show Donations Functionality")

    elif option == "5":

        print("Leaving DonateMe...")
        break

    else:
        print("Invalid Entry")

"""

# Task 4: Login functionality

while True:

    show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as: {authorized_user}")

    option = input("Choose an option: ")

    if option == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
        
# Task 5: Register functionality

    elif option == "2":

        username = input("Enter username: ")
        password = input("Enter password: ")

        authorized_user = register(database, username)

        if authorized_user != "":
            if len(password) >= 5:
                database[authorized_user] = password
            else:
                print("Invalid password. It must be at least 5 characters long.")
                    

 # Task 6: Donate functionality

    elif option == "3":

        if authorized_user == "":
            print("You are not logged in")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)


# Task 7: Show Donations

    elif option == "4":

        show_donations(donations)

    elif option == "5":

        print("Leaving DonateMe...")
        break

    else:
        print("Invalid Entry")

