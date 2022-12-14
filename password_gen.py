import random

uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercaseLetters = uppercaseLetters.lower()
numbers = "0123456789"
symbols = "!@#$%^&*"

uppercase, lowercase, number, symbol = True, True, True, True

all = ""

if uppercase:
    all += uppercaseLetters
if lowercase:
    all += lowercaseLetters
if number:
    all += numbers
if symbol:
    all += symbols

length = 16

password = "".join(random.sample(all, length))
print("Your password is: " + password)

saved_passwords = open("generated_passwords", "a")
saved_passwords.write(password + "\n")
saved_passwords.close()