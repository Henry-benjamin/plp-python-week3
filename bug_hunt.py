#Bug: missing the quote at the End of a string, And I fixed it to add the quote at the end of a string.
print("Welcome to the Bug Hunt!")
name = input("What is your name? ")
#Bug: missing the formatting stirng(f) and enclose the variable name with the curly brace and name variable was misspelle, I add f and close the varibale within curly brace
print(f"Nice to meet you, {name}")
# BUg: input() method returns a stirng always, then I fixed it to converte input() into an int()
age = int(input("How old are you? "))
#Bug: it tried to concantinate age and the string by using +, I ifxed by replacing the + operator with comma (,).
print("Next year you will be ",  age + 1)