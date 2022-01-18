# Program to slice emails

email = input('Enter your email address: ').strip()

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

format_ = (f"Your username is '{username}' and your domain is '{domain}")

print(format_)