age = int(input("How old are you: "))
is_adult = age >= 18
print(is_adult)

if is_adult:
    print("adults pay the full ticket price is $100")
else:
    print("everyone else pays the child price is $50" )