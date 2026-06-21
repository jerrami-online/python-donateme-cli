# DonateMe CLI

A simple command-line donation management application built in Python.

This project was developed as part of my Python Backend learning journey and demonstrates core programming concepts.

## Features

- User registration
- User login
- Case-insensitive usernames
- Username validation
- Password validation
- Donation tracking
- Donation history
- Total donation calculation

## Technologies

- Python 3

## Project Structure

```text
donations_pkg/
├── homepage.py
├── user.py
└── __init__.py

app.py
```

## Additional Enhancements

Beyond the original workshop requirements, I implemented:

- Case-insensitive username handling
- Username validation (must start with a letter and contain only alphanumeric characters)
- Password length validation
- Positive donation validation
- Total donation calculation

## Future Improvements

- SQLite database integration
- Password hashing
- User logout functionality
- Donation analytics
- Flask API version

## Sample Output

```text
=== DonateMe Homepage ===

1. Login
2. Register
3. Donate
4. Show Donations
5. Exit

Choose an option: 3

admin donated $100.0

Total: $100.0
```
