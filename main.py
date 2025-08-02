print('Welcome to Fermion')

variables = {}
list_command = ('set','print','add')
username = input("Enter your username : ").strip()
while True:
    line = input(f'>>> {username}@fermion ~$ ')
    command = line.split()

    if command[0] not in list_command:
        print("Invalid Command")
        continue
    else:
        pass
# Set Command = "set {var_name} = {integer}"
    if command[0] == 'set' and command[2] == '=':
        var_name = command[1]
        value = command[3]
        variables[var_name] = value 

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
            num2 = variables[var2]
            result = num1 + num2 
            print(result)
            

    