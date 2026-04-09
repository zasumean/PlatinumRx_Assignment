input_string = input("Enter String: ")
result = ""

for char in input_string:
    if char not in result:
        result += char

print("Unique String:", result)


