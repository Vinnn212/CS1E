zodiac_signs = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep"]

try:
    year = int(input("Enter a year to identify the Chinese zodiac sign: "))

    if year < 0:
        print("Year not supported")
    else:
        year_index = year % 12
        zodiac = zodiac_signs[year_index]
        print(f"The Chinese zodiac sign for the year", year, "is", zodiac)
except ValueError:
    print("Please enter a valid year (integer).")
