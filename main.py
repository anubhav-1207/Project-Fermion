from core.interpreter import start_shell

def login():
    password_file = "data/password.fermlog"
    username_file = "data/username.fermlog"


    try:
        with open(username_file) as f:
            username = f.read()

    except FileNotFoundError:
        with open(username_file,'w') as f:
            while True:
                username_auth_input = input("Set a new username : ").strip()
                if " " in username_auth_input :
                    print("Spaces not allowed! ")

                elif username_auth_input == '':
                    print("Arguement is necessary")

                else:
                    break

            f.write(username_auth_input)
            username = username_auth_input

    try:
        with open(password_file) as f:
            password = f.read()


    except FileNotFoundError:
        with open(password_file,'w') as f:
            while True:
                password_auth_input = input("Set a new password : ").strip()
                if " " in password_auth_input:
                    print("Spaces now allowed")

                elif password_auth_input == '':
                    print("Arguement is necessary")

                elif len(password_auth_input) < 8:
                    print("Arguement must contain atleast 8 characters")

                else:
                    break

            f.write(password_auth_input)
            password = password_auth_input

    passwd = input("Password : ")

    while passwd != password:
        print("Access Denied")
        passwd = input("Password : ")
    
    return username
        
if __name__ == "__main__":
    print("Fermion v1.2.1")
    user = login()
    start_shell(user)

# Fix : 
# 1. Useless file opening 
# 2. Empty username and password security 

# To-Do:
# 1. Error Handling 
# 2. New Commands 