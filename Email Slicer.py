email = input("Enter Your Email: ")

# we split our email by username and domain--------- sara123@gmail.com

index = email.index("@")
# email is string ,there is a built in index method

username = email[:index] #don't need the specify the beginning of the string but need ending variable
domain = email[index + 1:] #omitting the @ symbol at the beginning just add +1

print(f"Your username is {username} and domain is {domain}")

