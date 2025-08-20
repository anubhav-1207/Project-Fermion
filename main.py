import time
import os
import sys

def clear():
    os.system('cls')

print('Welcome to Fermion')

def main():
    variables = {}
    list_command = ('int','print','add','sub','mod','type','rename','list','purge','mul','div','ferm','del','find','loop','str','exit','reset')

    def linux():
        pass

    def multiplication(var1,var2):
        if var1 in variables and var2 in variables:
                    num1 = variables[var1]
                    num2 = variables[var2]
                    result = num1 * num2 
                    print(result)

        else:
            print(f"<NameError>:Variable '{var1}' or/and '{var2}' not Defined")

    def subtraction(var1,var2):
        if var1 in variables and var2 in variables:
            try:
                num1 = variables[var1]
                num2 = variables[var2]
                result = num1 - num2 
                print(result)

            except TypeError:
                print(f'<TypeError>: Not an integer')
                
        
        else:
            print(f"<NameError>:Variable '{var1}' or/and '{var2}' not Defined")

    def integer(var_name,raw_value):
        try:
            value = int(raw_value)
            variables[var_name] = value
        except ValueError:
            print("<ValueError>:Not An Integer")   

    def username_reset(new_name):
        global username
        username = new_name.strip()
        with open('authentication.fermlog','w') as f:
            f.write(f'Username : {username}\n')
        print(f"Changed Username To {username}")
        
    def type_check(var_name):
        if var_name in variables:
            print(type(variables[var_name]))
        else:
            print("<NameError:Variable not defined")

    def print_cmd(var_name):
        if var_name in variables:
            print(variables[var_name])
        else : 
            print(f"<NameError>:Variable {var_name} not Defined")

    def addition(var1,var2):
        if var1 in variables and var2 in variables:
            try:
                num1 = variables[var1]
            # num1 = int(num1)
        
                num2 = variables[var2]
            # num2 = int(num2)
                result = num1 + num2 
                print(result)
            
            except TypeError:
                print(f'<TypeError>: Not an integer')
        else:
            print(f"<NameError>:Variable '{var1}' or/and '{var2}' not Defined")

    def division(var1,var2):
        if var1 in variables and var2 in variables:
            num1 = variables[var1]
            num2 = variables[var2]
            if num2 == 0:
                print('''<ZeroDivisionError>: Can't Divide by zero''')
            else:
                result = num1 / num2 
                print(result)

        else:
            print(f"<NameError>:Variable '{var1}' or/and '{var2}' not Defined")

    def modulus(var_name):

        if var_name in variables:
            try:
                value = variables[var_name]
                if value < 0:
                    print(-value)
                else:
                    print(value)

            except TypeError:
                print('<ValueError> : not an integer')
            
            
        else:
            print(f"<NameError>:Variable '{var_name} not Defined")

    def rename(var_old,var_new):
        if var_new not in variables and var_old in variables:
            variables[var_new] = variables[var_old]
            print(f'Renamed {var_old} to {var_new}')
            del variables[var_old]
            
        elif var_new in variables and var_old in variables:
            print(f"<NameError>:Variable '{var_new}' already exists")

        elif var_new not in variables and var_old not in variables:
            print(f"<NameError>:Variable '{var_old}' and/or '{var_new}' not Defined")

        elif var_new in variables and var_old not in variables:
            print(f"<NameError>:Variable '{var_old}' not Defined")

    def purge():
        if variables:
            variables.clear()

        else:
            print(f"<NameError>:List '{variables}' is empty")

    def list():
        if variables:
            print('Variables :')
            for var_name,value in variables.items():
                print(f'{var_name} = {value}')
        else:
            print(f"<NameError>:Variable '{variables}' is empty")

    def delete(var_name):
        try:
            del variables[var_name]
        except KeyError:
            print(f"<NameError> : Variable {var_name} not Defined")

    def loop(value,var_new):
        if var_new in variables:
            for i in range(value):
                print(variables[var_new])


    def string(var_name,command):
        try:
            string = str(command[3])
            variables[var_name] = (string)
        except ValueError:
            print("Not A String")
            value = int(command[3])

    def process(command):
        if not command:
            return
        
        if command[0] not in list_command:
            print("<SyntaxError>:Invalid Command")
            return
        
        else:
            if command[0] == 'int' and command[2] == '=': #INT COMMAND 
                var_name = command[1]
                raw_value = command[3]
                integer(var_name,raw_value)

    # Reset username command = "reset username {new_name}"
            elif len(command) == 3 and command[0] == 'reset' and command[1] == 'username':
                new_name = command[2]
                username_reset(new_name)

    # Type Command = "type {var}"
            elif command[0] == 'type':
                var_name = command[1]
                type_check(var_name)

    # Print Command = "print {var_name}"
            elif len(command) == 2 and command[0] == 'print':
                var_name = command[1] 
                print_cmd(var_name)

    # Add Command = "add {var1} + var{2}"
            elif len(command) == 4 and command[0] == 'add':
                var1 = command[1]
                var2 = command[3]
                addition(var1,var2)

    # Sub Command = "sub {var1} - {var2}"
            elif len(command) == 4 and command[0] == 'sub':
                var1 = command[1]
                var2 = command[3]   

                subtraction(var1,var2)
                    
    # Mul Command = "mul {var1} * {var2}"
            elif len(command) == 4 and command[0] == 'mul':
                var1 = command[1]
                var2 = command[3]   

                multiplication(var1,var2)

    # Div Command = div {var1} / {var2}
            elif len(command) == 4 and command[0] == 'div':
                var1 = command[1]
                var2 = command[3]   
                division(var1,var2)
            
    # Mod Command = mod {var}
            elif len(command) == 2 and command[0] == 'mod':
                var_name = command[1]
                modulus(var_name)

    # Rename Command = "rename {old_var} {new_var}
            elif len(command) == 3 and command[0] == 'rename':
                var_new = command[2]
                var_old = command[1]
                rename(var_old,var_new)
                
    # Purge Command = 'purge'
            elif len(command) == 1 and command[0] == 'purge':
                purge()

    # List Command = "list"
            elif len(command) == 1 and command[0] == 'list':
                list()
                                    
    # Del Command = "del {var_name}"
            elif len(command) == 2 and command[0] == 'del':
                var_name = command[1]
                delete(var_name)

    # Loop Command = "loop {value} {times}"
            elif len(command) == 3 and command[0] == 'loop':
                value = int(command[1])
                var_new = command[2]
                loop(value,var_new)
                

    # Str Command = "str {var} = {string}" 
            elif len(command) == 4 and command[0] == 'str':
                var_name = command[1]
                string(var_name,command)

    # Ferm Run Command = ferm run {filename}
            elif len(command) == 3 and command[0] == 'ferm' and command[1] == 'run':
                filename = command[2]
                reader(filename)

    # Exit = exit
            elif command[0] == 'exit' and len(command) == 1:
                sys.exit()
                
    global username
    try:
        with open('authentication.fermlog', 'r') as f:
            line = f.readline().strip()
            username = line.split(':', 1)[1].strip()
            if not username:
                raise ValueError("Empty username in file")
            print(f'Logged in as @{username}')

    except (FileNotFoundError, IndexError, ValueError):
        username = input("Enter your username: ").strip()
        with open('authentication.fermlog', 'w') as f:
            f.write(f"username : {username}\n")


    print("Creating Environment...")
    time.sleep(1)
    
    def reader(filename):
        
        print("======================================================")
        print("Opening File...")
        print("======================================================")
        
        time.sleep(0.3)
        
        try:
            with open (filename) as f:
                for line in f:
                    process(line.strip().split())

        except FileNotFoundError:
            print(f"<FileNotFound> : The file {filename} couldn't be imported")
        
    while True:
        line = str(input(f">>> {username}@fermion ~$ ")) 
        process(line.split())
    
def password():
    global pswd
    global passw
    
    try:
        with open('password.fermlog', 'r') as f:
            line = f.readline().strip()
            pswd = line.split(':', 1)[1].strip()
    
    except (FileNotFoundError,IndexError):
        passw = input("Set a new password : ")
        with open('password.fermlog','w') as f:
            f.write(f'Password : {passw}')
            main()
    i = 0
    while i<=5:
        i += 1
        passw = input("Password2 : ")
        if passw == pswd:
            break
        elif passw != pswd and i >= 5:
            print("Maximum number of tries reached and the running module has been locked for 30 minutes. Please try again after 30 mins.")
            time.sleep(900)
            sys.exit()
        else:
            print(f"Wrong Passsword! Tries Left : {5-i}")

password()
main()
# Main Logic Runner 

        