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
        try:
            cmd = command[0]
        except IndexError:
            print("<NullError> : Empty input failed to parse")
            continue
        
        if cmd not in commands.command_list:
            print(f"<CommandError> : '{cmd}' is not a recognized command")
            continue

        elif cmd == 'int': # int var = value
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

        elif cmd == 'mod': # mod x 
            var1 = command[1]
            if var1 in variables:
                commands.mod(var1)

            else:
                errors.not_exist()        

        elif cmd == 'show': # show x 
            var1 = command[1]
            if var1 in variables:
                commands.show(var1)

            else:
                errors.not_exist()
        
        elif cmd == 'list':
            if variables:
                commands.list()
            else:
                errors.empty()

        elif cmd == 'del':
            var1 = command[1]
            if var1 in variables:
                commands.delete(var1)

            else:
                errors.not_exist()

        elif cmd == 'rename': # rename x to y
            var_old = command[1]
            var_new = command[3]
            if var_old in variables and var_new not in variables:
                commands.rename(var_new,var_old)

            else:
                print('<ValueError> : Either {var_old} is not yet defined or {var_new} is already defined or both')

        elif cmd == 'type':
            var1 = command[1]
            if var1 in variables:
                commands.type_check(var1)

            else:
                errors.not_exist()

        elif cmd == 'purge':
            if variables:
                commands.purge()

            else:
                errors.empty()

        # elif cmd == 'find':
        #     val1 = command[1]
        #     if val1 in variables:
        #         commands.find_check(val1)
        #     else:
        #         errors.not_exist()

        elif cmd == 'ferm': # ferm run data.ferm
            filename = command[2]
            commands.ferm(filename)

        elif cmd == 'sqr': # sqr  var x
            var1 = command[2]
            if var1 in variables:
                commands.square(var1)
            else:
                errors.not_exist()

        elif cmd == 'loop': # loop var x => 5
            var1 = command[2]
            index = int(command[4])
            if var1 in variables:
                commands.loop(var1,index)
            else:
                errors.not_exist()
            
        elif cmd == 'str': # str x = '476geg'
            var1 = command[1]
            string = str(command[3:])
            commands.str(var1,string)

        elif cmd == 'expo': # expo x ^ 22
            var1 = command[1]
            if var1 in variables:
                power = int(command[3])
                commands.expo(var1,power)
            else:
                errors.not_exist()

        elif cmd == 'help':
            commands.help()

        elif cmd == 'evaluate': # evaluate 
            expression = command[1]
            commands.evaluate(expression)
            
            
            