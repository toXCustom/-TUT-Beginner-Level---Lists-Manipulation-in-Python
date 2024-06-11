def main():
    numbers = []

    while True:
        try:
            number = iny(input("Enter an integer (0 to finish): "))
            if number == 0:
                break
            numbers.append(number)
        except ValueError:
            print("Please enter a valid integer (digit to convert)")