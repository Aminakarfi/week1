# Ask the user to enter a month number (1 to 12)
month = int(input("Enter the month number (1 to 12): "))

# Check the season based on the month
if month in [3, 4, 5]:
    print("It's Spring!")
elif month in [6, 7, 8]:
    print("It's Summer!")
elif month in [9, 10, 11]:
    print("It's Autumn!")
elif month in [12, 1, 2]:
    print("It's Winter!")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
