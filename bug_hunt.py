#Bug: missing the quote at the End of a string, And I fixed it to add the quote at the end of a string.
print("Welcome to the Bug Hunt!")
name = input("What is your name? ")
#Bug: name variable was misspelle 
print("Nice to meet you", name)
age = input("How old are you? ")
#Bug: it tried to concantinate age and the string by using +, I ifxed by replacing the + operator with comma (,). and convert age into a number by using int()
print("Next year you will be ",  int(age) + 1)