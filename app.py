from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
authorized_user = ""

# Main app Loop

while True:

    show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as: {authorized_user}")

    option = input("Choose an option: ")

    # Login

    if option == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)

    # Register

    elif option == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")

        if len(password) < 5:
            print("Invalid password. Must be at least 5 characters.")
        else:
            authorized_user = register(database, username)
            if authorized_user != "":
                database[authorized_user] = password

    # Donate

    elif option == "3":
        if authorized_user == "":
            print("You are not logged in")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)

    # Show Donations

    elif option == "4":
        show_donations(donations)

    # Exit

    elif option == "5":
        print("Leaving DonateMe...")
        break

    else:
        print("Invalid Entry")
