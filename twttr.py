text=input("Input: ")
print("Output: ", end="")
for letter in text:
    if letter.lower() not in ['a','i','e','o','u']:
        print(letter, end="")
print()

        