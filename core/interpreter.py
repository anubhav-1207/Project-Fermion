from core import commands

def start_shell(user):
    while True:
        line = input(f"{user}@fermion ~$ ")
        if line == 'exit':
            break
        elif line == '' or line == ' ':
            print("Empty Not Allowed")

        command = line.split()
        cmd = command[0]

        if cmd == 'int' and command[2] == '=': # int var = value
            value = command[3]
            var = command[1]
            commands.integer(value,var)
        
        elif cmd == 'add' and command[2] == '+': # add var1 + var2
            var1 = command[1]
            var2 = command[3]
            commands.add(var1,var2)
            print('Error')

        
