username = input("Enter username: ")
email = input("Enter email: ")
phone = input("Enter phone: ")
password = input("Enter password: ")
password_repeat = input("Repeat password: ")

# Username Validation
if len(username) < 5 or len(username) > 20:
    print("Username should be between 5 and 20 characters long.")
elif not username.isalnum():
    print("Username can only contain alphanumeric characters.")
elif username.lower() in ['admin', 'root']:
    print("Username should not be a reserved name.")
else:
    print("Username is valid.")

# Email Validation
if "@" not in email or "." not in email.split("@")[-1]:
    print("Email format is invalid.")
else:
    print("Email is valid.")

# Phone Number Validation
if phone.startswith("+"):
    phone_without_plus = phone[1:]
else:
    phone_without_plus = phone

if not phone_without_plus.isdigit() or len(phone_without_plus) not in [9, 11, 12]:
    print("Phone number format is invalid. It should be +37499123456 or 099123456.")
else:
    print("Phone number is valid.")

# Password Validation
if len(password) < 8:
    print("Password should be at least 8 characters long.")
elif not any(char.isupper() for char in password):
    print("Password should contain at least one uppercase letter.")
elif not any(char.islower() for char in password):
    print("Password should contain at least one lowercase letter.")
elif not any(char.isdigit() for char in password):
    print("Password should contain at least one digit.")
elif not any(char in "!@#$%^&*" for char in password):
    print("Password should contain at least one special character.")
else:
    print("Password is valid.")

# Password Repeat Validation
if password != password_repeat:
    print("Passwords do not match.")
else:
    print("Passwords match.")