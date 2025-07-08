import random
print("Welcome to Password generator")
print("----------------------------")
chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
numbers =int(input("Amount of passwords to generate: "))
length =int(input("Enter length of password: "))
print("Here are your Passwords")
for password in range(numbers):
    passwords=" "
    for c in range(length):
        passwords+=random.choice(chars)
    print(passwords)
print("This is my second password generator program")
print("Thank you dear user for using the password generator!")