full_name = input("Enter your full name: ")
parts = full_name.split()

if len(parts) >= 2:
    print(f"Hello, {parts[0]}!")
else:
    print("Please enter your full name.")