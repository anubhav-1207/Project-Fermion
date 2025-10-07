variables = {}

def integer(var_name,raw_value):
    try:
        value = int(raw_value)
        var_name = commands[1]
        variables[var_name] = value
    except:
        print("Invalid Operation! Please Try Again")