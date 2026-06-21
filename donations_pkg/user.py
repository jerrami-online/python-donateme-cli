def login(database, username, password):

    username = username.lower() # Make the username case-insensitive for login

    if username in database and database[username] == password:
        print(f"Welcome {username}!")
        return username
    
    elif username in database and database[username] != password:
        print(f"Incorrect password for {username}")
        return ""
    
    else:
        print("User not found. Please register.")
        return ""


def register(database, username):

    username = username.lower() # Make the username case-insensitive for registration.

    if not username[0].isalpha(): # Implement username validation to ensure it starts with a letter.
        print("Username must start with a letter.")
        return ""
    
    if not username.isalnum(): # Implement username validation to ensure it contains only alphanumeric characters.
        print("Username must contain only numbers and letters.")
        return ""

    if len(username) > 10: # Adding validation for username length.
        print("Invalid. Username must not exceed 10 characters")
        return ""

    if username in database: # Adding validation for password length.
        print("Username already registered")
        return ""
    else:
        print(f"{username} has been registered")
        return username

