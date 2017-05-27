email = input("Enter your email id :").strip()

username = email[:email.index("@")]

domain = email[email.index("@")+1:]

message = "Your username is {} and your domain name is {}"

print(message.format(username,domain))