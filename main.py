import time

print("Fermion v1.2.1")

password_file = "data/password.fermlog"
username_file = "data/username.fermlog"


try:
    with open(username_file) as f:
        username = f.read()

except FileNotFoundError:
    with open(username_file,'w') as f:
        while True:
            username_auth_input = input("Set a new username : ").strip()
            if " " in username_auth_input:
                print("Spaces not allowed! ")

            else:
                break

        f.write(username_auth_input)

with open(username_file) as f:
    username = f.read()
try:
    with open(password_file) as f:
        password = f.read()

except FileNotFoundError:
    with open(password_file,'w') as f:
        password_auth_input = input("Set a new password : ").strip()
        f.write(password_auth_input)
        
with open(password_file) as f:
    password = f.read()
    

passwd = input("Password : ")

while passwd != password:
    print("Access Denied")
    passwd = input("Password : ")

line_input = input(f">>> {username}@fermion ~$ ")

# Fix : 
# 1. Useless file opening 
# 2. Empty username and password security 