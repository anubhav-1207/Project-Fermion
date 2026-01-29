variables = {}

command_list = ['int','add','diff','prod','recprod','mod','show','list','del','rename','type','ferm'] 

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

