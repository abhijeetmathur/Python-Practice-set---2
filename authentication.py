def authenticate(username, passward):
    
    predefined_username = "user123"
    predefined_passward = "pass123"
    
    if predefined_username == username and predefined_passward == passward:
        return True
    else:
        return False
    
username = input("Enter username: ")
passward = input("Enter passward")

if authenticate(username, passward):
    print("Authentication Successful")
else:
    print("Invalid username or passward")