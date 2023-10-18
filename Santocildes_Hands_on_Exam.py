print("****************************")
print("| Number System Converter |")
print("****************************")
print("By: Vince Joram P. Santocildes")
print("")
decimal_number = int(input("Enter a decimal number:"))
print("")
print("********************************************")
print("[1] Decimal Number to Binary Number")
print("[2] Decimal Number to Octal Number")
print("[3] Decimal Number to Hexadecimal Number")
print("********************************************")
print("")
convert_number = int(input("How do you want to convert your Decimal number? Enter from [1-3]:"))

if convert_number >= 4:
    print("Invalid Option. Try Again")

elif convert_number == 1:
    print("The Binary Number of", decimal_number, "is", format(decimal_number, "b"))

elif convert_number == 2:
    print("The Octal Number of", decimal_number, "is", format(decimal_number, "o"))

elif convert_number == 3:
    print("The Hexadecimal of", decimal_number, "is", format(decimal_number, "x"))