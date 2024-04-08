"""
PowerOfTen
"""
# Provide your solution here
number = int(input("Enter a max 3 digit number: "))

if number % 10 == 0:
    print(number)
elif number < 0:
    print("number cannot be negative")
else:
    print("number has more than 3 digits")


"""
Cash Box
"""
# Provide your solution here

number = input("to pay: ")
number2 = input("received: ")

change = number - number2
print(f"{change}")

if number2 < number:
    print("you did not pay enough")
elif change < 0:
    print("negative received amount is invalid")