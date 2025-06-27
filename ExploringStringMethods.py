# Task 1
message = "Python is amazing!"
print("First word: " + message[0:6])
print("Amazing part: " + message[10:17])
print("Reversed string: " + message[::-1])


# Task 2
message = " hello, python world! "
print(message.strip())
print(message.strip().capitalize())
print(message.strip().capitalize().replace("world", "universe"))
print(message.strip().capitalize().replace("world", "universe").upper())


# Task 3
word = input("Enter a word: ")
if word == word[::-1]:
    print("Yes, " + word + " is a palindrome!")
else:
    print("No, " + word + " is not a palindrome")
