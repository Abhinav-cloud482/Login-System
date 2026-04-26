# Login-System

## Login System (Tkinter + Python)

A simple desktop-based login system built using Python and Tkinter. This project demonstrates user authentication with password hashing, account locking after multiple failed attempts, and password reset functionality.

## Features

- User Registration
- Secure Password Hashing using SHA-256
- Login Authentication
- Account Lock after 3 Failed Attempts
- Password Reset Option
- Session Token Generation (UUID-based)
- Persistent User Storage using Pickle

## Tech Stack

- Python 3
- Tkinter (GUI)
- Pickle (Data Storage)
- Hashlib (Password Security)
- UUID (Session Token)

## Project Structure

```
Login-System/
│── Login - System.py   # Main application file
│── users.pkl           # Auto-generated user database (after first run)
│── README.md           # Project documentation

```

## Installation & Setup

1. Clone the repository :

```
git clone https://github.com/your-username/login-system.git
cd login-system
```

2. Run the application :

```
python "Login - System.py"
```

   - Make sure Python 3 is installed on your system.


## Usage

### Register

  - Enter a username and password (minimum 6 characters)
  - Click Register

### Login

  - Enter registered credentials
  - Click Login
  - On success, a session token will be generated

### Reset Password

  - Enter your username
  - Click Reset Password
  - Provide a new password


## Security Features

- Passwords are hashed using SHA-256 before storage
- Accounts are locked after 3 failed login attempts
- Resetting password unlocks the account
- Session tokens generated using UUID


## Limitations

- Uses Pickle for storage (not recommended for production)
- No database integration
- No encryption for stored files
- Basic UI (Tkinter-based)


## Future Improvements

- Replace Pickle with SQLite or a secure database
- Add email-based password recovery
- Improve UI/UX
- Implement password strength validation
- Add multi-user session management


