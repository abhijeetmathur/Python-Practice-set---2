import re
def check_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

email = input("Enter email : ")
if check_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.")