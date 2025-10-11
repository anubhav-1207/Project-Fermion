variables = {}

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

