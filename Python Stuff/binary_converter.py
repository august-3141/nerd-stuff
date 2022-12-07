# Binary conversion since I am very bored

print("*** Binary Converter ***")
print("------------------------")

toFrom = str(input("Convert to?: "))

if toFrom == "binary" or toFrom == "Binary" or toFrom == "b":

    intIn = int(input("Enter an integer: "))
    print(f"{intIn} in binary format: {bin(intIn)}")

elif toFrom == "integer" or toFrom == "Integer" or toFrom == "i":

    binIn = input("Enter the binary string: ")
    print(f"{binIn} in integer format: {int(binIn, 2)}")

else:

    print("Make sure you use a valid format (ex. \"binary\", \"integer\")")
