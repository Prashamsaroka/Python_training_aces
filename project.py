# Python Password Security Tool

# Function to check password strength
def check_strength(password):
    upper = lower = digit = 0

    if len(password) < 8:
        return "Weak Password (Minimum 8 characters required)"

    for ch in password:
        if ch.isupper():
            upper = 1
        elif ch.islower():
            lower = 1
        elif ch.isdigit():
            digit = 1

    if upper and lower and digit:
        return "Strong Password"
    else:
        return "Moderate Password (Add uppercase, lowercase and digits)"


# Function for login system
def login_system():
    stored_username = "admin"
    stored_password = "Admin123"

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == stored_username and password == stored_password:
        print("✅ Login Successful")
    else:
        print("❌ Login Failed")


# Main menu
while True:
    print("\n--- Python Password Security Tool ---")
    print("1. Check Password Strength")
    print("2. Secure Login System")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        pwd = input("Enter password to check: ")
        result = check_strength(pwd)
        print("Result:", result)

    elif choice == "2":
        login_system()

    elif choice == "3":
        print("Thank you for using the tool!")
        break

    else:
        print("Invalid choice! Try again.")
