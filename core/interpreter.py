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
        
        # Checking the user's commands validity
        if cmd not in commands.command_list:
            print(f"<CommandError> : '{cmd}' is not a recognized command")
            continue

        # Integer Command    
        elif cmd == 'int': # int var = value
            try:
                if command[2] == '=':
                    value = command[3]
                    var = command[1]
                    commands.integer(value,var)

                else:
                    errors.inv_operator()
            except TypeError:
                errors.type_mismatch()


        # Addition Command
        elif cmd == 'add' : # add var1 + var2
            try:
                if command[2] == '+':
                    var1 = command[1]
                    var2 = command[3]
                    if var1 and var2 in variables:
                        commands.add(var1,var2)
                    else:
                        errors.not_exist()

                else:
                    errors.inv_operator()
            except (IndexError,KeyError,TypeError,ValueError):
                errors.not_exist()

        # Difference Command
        elif cmd == 'diff': # diff x - y
            try:
                if command[2] == '-':
                    var1 = command[1]
                    var2 = command[3]
                    if var1 and var2 in variables:
                        commands.diff(var1,var2)
                    else:
                        errors.not_exist()

                else:
                    errors.inv_operator()

            except (IndexError,KeyError,TypeError,ValueError):
                print("Error")

        # Product Command
        elif cmd == 'prod': # prod x * y
            try:
                if command[2] == '*':
                    var1 = command[1]
                    var2 = command[3]
                    if var1 and var2 in variables:
                        commands.prod(var1,var2)
                    else:
                        errors.not_exist()

                else:
                    errors.inv_operator()
            except (IndexError,KeyError,TypeError,ValueError):
                print("Error")

            
        # Inverse Product Command
        elif cmd == 'invprod': # recprod x / y 
            try:
                if command[2] == '/':
                    var1 = command[1]
                    var2 = command[3]
                    if var1 and var2 in variables:
                        commands.recprod(var1,var2)
                    else:
                        errors.not_exist()

                else:
                    errors.inv_operator() 
            except (IndexError,KeyError,TypeError,ValueError):
                print("Error")

        # Modulus Command
        elif cmd == 'mod': # mod x 
            try:
                var1 = command[1]
                if var1 in variables:
                    commands.mod(var1)

                else:
                    errors.not_exist()        
            except (IndexError,KeyError,TypeError,ValueError):
                print("Error")

        # Show Command
        elif cmd == 'show': # show x 
            try:
                var1 = command[1]
                if var1 in variables:
                    commands.show(var1)

                else:
                    errors.not_exist()
            except (IndexError,KeyError,TypeError,ValueError):
                print("Error")

        # List Command            
        elif cmd == 'list':
            try:
                if variables:
                    commands.list()
                else:
                    errors.empty()
            except (IndexError,KeyError,TypeError,ValueError):
                print("Error")
        # Delete Command
        elif cmd == 'del':
            try:
                var1 = command[1]
                if var1 in variables:
                    commands.delete(var1)

                else:
                    errors.not_exist()
            except (IndexError,KeyError,TypeError,ValueError):
                print("Error")

        # Rename Command
        elif cmd == 'rename': # rename x to y
            try:
                var_old = command[1]
                var_new = command[3]
                if var_old in variables and var_new not in variables:
                    commands.rename(var_new,var_old)

                else:
                    print('<ValueError> : Either {var_old} is not yet defined or {var_new} is already defined or both')
            except (IndexError,KeyError,TypeError,ValueError):
                print("Error")

        # Type Command
        elif cmd == 'type':
            try:
                var1 = command[1]
                if var1 in variables:
                    commands.type_check(var1)

                else:
                    errors.not_exist()
            except (IndexError,KeyError,TypeError,ValueError):
                print("Error")

        # Purge Command 
        elif cmd == 'purge':
            try:
                if variables:
                    commands.purge()

                else:
                    errors.empty()
            except (IndexError,KeyError,TypeError,ValueError):
                print("Error")

        # elif cmd == 'find':
        #     val1 = command[1]
        #     if val1 in variables:
        #         commands.find_check(val1)
        #     else:
        #         errors.not_exist()

        # elif cmd == 'ferm': # ferm run data.ferm
        #     filename = command[2]
        #     commands.ferm(filename)

        # Square Command
        elif cmd == 'sqr': # sqr  var x
            try:
                var1 = command[2]
                if var1 in variables:
                    commands.square(var1)
                else:
                    errors.not_exist()
            except (IndexError,KeyError,TypeError,ValueError):
                print("Error")

        # Loop Command
        elif cmd == 'loop': # loop var x => 5
            try:    
                var1 = command[2]
                index = int(command[4])
                if var1 in variables:
                    commands.loop(var1,index)
                else:
                    errors.not_exist()
            except (IndexError,KeyError,TypeError,ValueError):
                print("Error")

        # String Command
        elif cmd == 'str': # str x = '476geg'
            try:
                var1 = command[1]
                string = str(command[3:])
                commands.str(var1,string)
            except (IndexError,KeyError,TypeError,ValueError):
                print("Error")

        # Exponent Command
        elif cmd == 'expo': # expo x ^ 22
            try:
                var1 = command[1]
                if var1 in variables:
                    power = int(command[3])
                    commands.expo(var1,power)
                else:
                    errors.not_exist()
            except (IndexError,KeyError,TypeError,ValueError):
                print("Error")

        # Help Command
        elif cmd == 'help':
            commands.help()

        # Evaluate Command
        elif cmd == 'evaluate': # evaluate 
            try:
                expression = command[1]
                commands.evaluate(expression)
            except (IndexError,KeyError,TypeError,ValueError):
                print("Error")

        # Turtle Command
        elif cmd == 'turtle':
            commands.turtle()

        # Easter Egg #2 Command
        elif cmd == 'fermion':
            fermion_para = '''In physics, fermions are the fundamental building blocks of matter.
Similarly, Fermion is designed as a fundamental building block interpreter for learning and experimenting with language creation.
Fermion was created with the intention of providing a simple yet powerful platform for users to explore programming concepts and language design.
Just as fermions follow the Pauli exclusion principle, Fermion aims to provide a unique and exclusive experience for each user, allowing them to create and manipulate their own programming languages without interference.
Fermion is not just an interpreter; it's a playground for creativity and innovation in the world of programming languages.
So dive in, experiment, and let your imagination run wild with Fermion.'''
            print(fermion_para.center(80))


        
            
            