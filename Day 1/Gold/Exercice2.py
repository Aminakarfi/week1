for number in range(1, 21):
    print(number)

numbers = list(range(1, 21))  # This creates a list: [1, 2, 3, ..., 20]

for index in range(len(numbers)):
    if index % 2 == 0:  # If index is even (0, 2, 4, ...)
        print(numbers[index])
