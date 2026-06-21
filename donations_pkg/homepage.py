def show_homepage():
    print("")
    print("          === DonateMe Homepage ===       ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register       |")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations |")
    print("------------------------------------------")
    print("|               5. Exit                  |")
    print("------------------------------------------")


def donate(username):

    donation_amt = float(input("Enter amount to donate: "))
    if donation_amt <= 0:
        print("Donation must be greater than 0.")
        return ""

    donation_string = f"{username} donated ${donation_amt}"
    print("Thank you for your donation!")
    return donation_string

def show_donations(donations):

    print("\n---All Donations---")
    if donations == []:
        print("Currently, there are no donations")
    else:
        total = 0

        for donation in donations:
            print(donation)
            amount = float(donation.split("$")[1]) # Get the amount after "$" and add it to the total, since donation_string are appended to the donations list as str
            total += amount 
        
        print(f"Total = ${total}") 


