full_name = input("type your Full name: ")
split = full_name.split()

if len(split) == 2:
    print(f"Hello {split[0]}")
elif len(split) == 1:
    print("Hee, type your full name Please ")