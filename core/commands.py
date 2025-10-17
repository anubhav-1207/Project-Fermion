from core import interpreter
variables = {}

command_list = ['int','add','diff','prod','recprod','mod','show','list','del','rename','type','purge','find','ferm','sqr','loop','str','expo','help','evaluate','turtle'] 

def integer(value,var):
    try:
        value = int(value)
        variables[var] = value
         
    except ValueError:
        print("<ValueError> : Given value is not an integer")

def add(var1,var2):
    #try:
    val1 = variables[var1]
    val2 = variables[var2]
    val1 = int(val1)
    val2 = int(val2)
    print(val1+val2)

def diff(var1,var2):
    val1 = variables[var1]
    val2 = variables[var2]
    val1 = int(val1)
    val2 = int(val2)
    print(val1 - val2)

def prod(var1,var2):
    val1 = variables[var1]
    val2 = variables[var2]
    val1 = int(val1)
    val2 = int(val2)
    print(val1*val2)

def recprod(var1,var2):
    val1 = variables[var1]
    val2 = variables[var2]
    val1 = int(val1)
    val2 = int(val2)
    print(val1/val2)

def mod(var1):
    val1 = variables[var1]
    if val1 > 0:
        print(f'{val1}')
    else:
        print(f'{-val1}')

def show(var1):
    val1 = variables[var1]
    print(f'{var1} = {val1}')

def list():
    print(variables)

def delete(var1):
    del variables[var1]
    print(f"Variable '{var1}' deleted successfully")

def rename(var_new,var_old):
    val_old = variables[var_old]
    variables[var_new] = val_old
    del variables[var_old]

def type_check(var1):
    print(type(variables[var1]))
    
def purge():
    variables.clear()
    print("Cleared")

# def find_check(val1):
#     for key,value in variables.items():
#         if value == val1:
#             print(f'{key}')
#             break

def ferm(filename):
    with open (filename,'r') as f:
        for interpreter.line in f:
            pass
            
def square(var1):
    val1 = variables[var1]
    val1 = int(val1)
    print(val1*val1)

def loop(var1,index):
    val1 = variables[var1]
    val1 = int(val1)
    for i in range(index):
        print(val1)

def str(var_name,string):
    try:
        variables[var_name] = string

    except TypeError:
        print("<TypeError> : Given value is not a string")

def expo(var1,power):
    print(variables[var1]**power)

def help():
    print("Available commands:".center(50,"-"))
    help_output = '''
    int <var> = <value>         : Define an integer variable
    str <var> = <value>         : Define a string variable
    add <var1> + <var2>           : Add two variables
    diff <var1> - <var2>          : Subtract two variables
    prod <var1> * <var2>          : Multiply two variables
    recprod <var1> / <var2>       : Divide two variables
    mod <var>                   : Get the absolute value of a variable
    show <var>                  : Show the value of a variable
    list                        : List all defined variables
    del <var>                   : Delete a variable
    rename <new_var> <old_var>  : Rename a variable
    type <var>                  : Show the data type of a variable
    purge                       : Clear all defined variables
    ferm <filename>             : Execute commands from a file
    sqr <var>                   : Square the value of a variable
    loop <var> => <index>       : Print the value of a variable multiple times
    expo <var> ^ <power>        : Raise the value of a variable to a specified power
    help                        : Show this help message
    exit                        : Exit the interpreter
    evaluate <expression>       : Evaluate a mathematical expression
    '''
    print(help_output)

def evaluate(expression):
    print(eval(expression))
    
def turtle():
    print('''Turtles are basically the introverts of the animal kingdom who accidentally invented mobile homes. They stroll around like they’ve got all the time in the world—which, honestly, they do. While other creatures are out there sprinting, hunting, or stressing about survival, turtles are just like, “Nah, I’m good,” munching on a leaf for six hours straight. Their whole vibe screams self-care. They don’t rush, they don’t panic, they just… exist, like little zen monks with shells. And have you ever noticed how they look mildly offended all the time? It’s like every turtle was promised a glam life as a dragon but ended up being a slow salad enthusiast instead. Yet somehow, they made it iconic. When they tuck themselves into their shells, it’s not fear—it’s boundaries. Pure, healthy boundaries. Baby turtles? Absolute chaos gremlins in tiny armor, charging bravely toward the ocean like it’s an action movie. Old turtles? Unbothered sages who’ve seen empires rise and fall and still refuse to move faster than 1 km/h. Honestly, turtles are proof that life isn’t a race—it’s a very, very slow parade, and if you look cute enough doing it, everyone will cheer anyway.

''')
    
    print("Congratulations!! You have found the turtle easter egg!")
