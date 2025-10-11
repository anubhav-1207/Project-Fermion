from core import commands
from core.commands import variables
from core import errors

def start_shell(user):
    while True:
        line = input(f"{user}@fermion ~$ ")
        if line == 'exit':
            break
        elif line == '' or line == ' ':
            print("Empty Not Allowed")

        command = line.split()
        cmd = command[0]

        if cmd == 'int': # int var = value
            if command[2] == '=':
                value = command[3]
                var = command[1]
                commands.integer(value,var)

            else:
                errors.inv_operator()
        
        elif cmd == 'add' : # add var1 + var2
            if command[2] == '+':
                var1 = command[1]
                var2 = command[3]
                if var1 and var2 in variables:
                    commands.add(var1,var2)
                else:
                    errors.not_exist()

            else:
                errors.inv_operator()

        elif cmd == 'diff': # diff x - y
            if command[2] == '-':
                var1 = command[1]
                var2 = command[3]
                if var1 and var2 in variables:
                    commands.diff(var1,var2)
                else:
                    errors.not_exist()

            else:
                errors.inv_operator()
                
        elif cmd == 'prod': # prod x * y
            if command[2] == '*':
                var1 = command[1]
                var2 = command[3]
                if var1 and var2 in variables:
                    commands.prod(var1,var2)
                else:
                    errors.not_exist()

            else:
                errors.inv_operator()

        elif cmd == 'invprod': # recprod x / y 
            if command[2] == '/':
                var1 = command[1]
                var2 = command[3]
                if var1 and var2 in variables:
                    commands.recprod(var1,var2)
                else:
                    errors.not_exist()

            else:
                errors.inv_operator() 
                

        
