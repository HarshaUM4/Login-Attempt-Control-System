import time

# Correct password
correct_password = "admin123"

# Maximum attempts allowed
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Incorrect password! Attempts remaining: {remaining}")

if attempts == max_attempts:
    print("\nToo many failed attempts.")
    print("Access locked for 10 seconds...")
    time.sleep(10)
    print("You can try again now.")