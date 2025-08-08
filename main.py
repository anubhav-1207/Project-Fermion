print('Welcome to Fermion')

variables = {}
list_command = ('int','print','add','sub','mod','type','rename','list','purge','mul','div','ferm','del','find','loop','str')
username = input("Enter your username : ").strip()

def ferm_runner():
    while True:
        line = input(f'>>> @fermion ~$ ')
        command = line.split()

        if command[0] not in list_command:
            print("<SyntaxError>:Invalid Command")
            continue
        else:
            pass


    # Int Command = "int {var_name} = {integer}"
        if command[0] == 'int' and command[2] == '=':
            var_name = command[1]
            raw_value = command[3]
            try:
                value = int(raw_value)
                variables[var_name] = value
            except ValueError:
                print("<ValueError>:Not An Integer")        
            

    # Type Command = "type {var}"
        elif command[0] == 'type':
            var_name = command[1]
            if var_name in variables:
                print(type(variables[var_name]))
            else:
                print("<NameError:Variable not defined")

    # Print Command = "print {var_name}"
        elif len(command) == 2 and command[0] == 'print':
            var_name = command[1] 
            if var_name in variables:
                print(variables[var_name])

            else : 
                print(f"<NameError>:Variable {var_name} not Defined")



    # Add Command = "add {var1} + var{2}"
        elif len(command) == 4 and command[0] == 'add':
            var1 = command[1]
            var2 = command[3]
            if var1 and var2 in variables:
                num1 = variables[var1]
                # num1 = int(num1)
            
                num2 = variables[var2]
                # num2 = int(num2)
                result = num1 + num2 
                print(result)
                
            else:
                print(f"<NameError>:Variable '{var1}' or/and '{var2}' not Defined")




    # Sub Command = "sub {var1} - {var2}"
        elif len(command) == 4 and command[0] == 'sub':
            var1 = command[1]
            var2 = command[3]   

            if var1 and var2 in variables:
                num1 = variables[var1]
                num2 = variables[var2]
                result = num1 - num2 
                print(result)
            
            else:
                print(f"<NameError>:Variable '{var1}' or/and '{var2}' not Defined")

                
                
    # Mul Command = "mul {var1} * {var2}"
        elif len(command) == 4 and command[0] == 'mul':
            var1 = command[1]
            var2 = command[3]   

            if var1 in variables and var2 in variables:
                num1 = variables[var1]
                num2 = variables[var2]
                result = num1 * num2 
                print(result)

            else:
                print(f"<NameError>:Variable '{var1}' or/and '{var2}' not Defined")



    # Div Command = div {var1} / {var2}
        elif len(command) == 4 and command[0] == 'div':
            var1 = command[1]
            var2 = command[3]   

            if var1 and var2 in variables:
                num1 = variables[var1]
                num2 = variables[var2]
                if num2 == 0:
                    print('''ZeroDivisionError:Can't Divide by zero''')
                result = num1 // num2 
                print(result)

            else:
                print(f"<NameError>:Variable '{var1}' or/and '{var2}' not Defined")

        
    # Mod Command = mod {var}
        elif len(command) == 2 and command[0] == 'mod':
            var_name = command[1]
            if var_name in variables:
        
                try:
                    value = variables[var_name]
                except:
                    print('### ValueError : not an integer')
                
                if value < 0:
                    print(-value)
                else:
                    print(value)

            else:
                print(f"<NameError>:Variable '{var_name} not Defined")




    # Rename Command = "rename {old_var} {new_var}
        elif len(command) == 3 and command[0] == 'rename':
            var_new = command[2]
            var_old = command[1]

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

            
            




    # Purge Command = 'purge'
        elif len(command) == 1 and command[0] == 'purge':
            if variables:
                variables.clear()

            else:
                print(f"<NameError>:List '{variables}' is empty")


    # List Command = "list"
        elif len(command) == 1 and command[0] == 'list':
            if variables:
                print('Variables :')
                for var_name,value in variables.items():
                    print(f'{var_name} = {value}')
            else:
                print(f"<NameError>:Variable '{variables}' is empty")
                    
    # Del Command = "del {var_name}"
        elif len(command) == 2 and command[0] == 'del':
            var_name = command[1]
            del variables[var_name]


    # Find Command = "find {var_name}"
        elif len(command) == 2 and command[0] == 'find':
            value = int(command[1])
            keys = [k for k , v in variables.items() if v == value]
            print(keys)

    # Loop Command = "loop {value} {times}"
        elif len(command) == 3 and command[0] == 'loop':
            value = command[1]
            var_new = int(command[2])
            for x in range(var_new):
                print(value)

    # Str Command = "str {var} {string}" 
        elif len(command) == 3 and command[0] == 'str':
            var_name = command[1]
            try:
                string = str(command[2])
                variables[var_name] = (string)
            except ValueError:
                print("Not A String")
                value = int(command[3])

    # Easter Egg: cat
        elif len(command) == 1 and command[0] == 'aditya':
            print("You Found An Easter Egg : This tells us that Aditya is my bestfriend.")


    



















ferm_runner()