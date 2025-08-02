print('Welcome to Fermion')

variables = {}
list_command = ('set','print','add','sub','mod','type','rename','list','purge')
# username = input("Enter your username : ").strip()
while True:
    line = input(f'>>> @fermion ~$ ')
    command = line.split()

    if command[0] not in list_command:
        print("Invalid Command")
        continue
    else:
        pass



# Set Command = "set {var_name} = {integer}"
    if command[0] == 'set' and command[2] == '=':
        var_name = command[1]
        try:
            value = int(command[3])
            variables[var_name] = (value)
        except ValueError:
            print("### Error : Not An Integer")

# Type Command = "type {var}"
    if command[0] == 'type':
        var_name = command[1]
        if var_name in variables:
            print(type(variables[var_name]))
        else:
            print("### Error : Variable not defined")

# Print Command = "print {var_name}"
    elif len(command) == 2 and command[0] == 'print':
        var_name = command[1] 
        if var_name in variables:
            print(variables[var_name])

        else : 
            print("### Error ")



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
            print('### Error : Variable(s) not defines')



# Sub Command = "sub {var1} - {var2}"
    elif len(command) == 4 and command[0] == 'sub':
        var1 = command[1]
        var2 = command[3]   

        if var1 and var2 in variables:
            num1 = variables[var1]
            num2 = variables[var2]
            result = num1 - num2 
            print(result)
            
            
            
# Mul Command = "mul {var1} * {var2}"
    elif len(command) == 4 and command[0] == 'mul':
        var1 = command[1]
        var2 = command[3]   

        if var1 in variables and var2 in variables:
            num1 = variables[var1]
            num2 = variables[var2]
            result = num1 * num2 
            print(result)


# Div Command = div {var1} / {var2}
    elif len(command) == 4 and command[0] == 'div':
        var1 = command[1]
        var2 = command[3]   

        if var1 and var2 in variables:
            num1 = variables[var1]
            num2 = variables[var2]
            if num2 == 0:
                print('''### ZeroDivision Error : Can't Divide by zero''')
            result = num1 // num2 
            print(result)
    
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



# Rename Command = "rename {old_var} {new_var}
    elif len(command) == 3 and command[0] == 'rename':
        var_new = command[2]
        var_old = command[1]

        if var_new not in variables and var_old in variables:
            variables[var_new] = variables[var_old]
            print(f'Renamed {var_old} to {var_new}')
            del variables[var_old]
            

# List Command = "list"  
    elif len(command) == 1 and command[0] == 'list':
        print(variables)

# Purge Command = 'purge'
    elif len(command) == 1 and command[0] == 'purge':
        variables.clear()
