# ⚛️ Fermion

Fermion is a lightweight Python-based mini-interpreter that simulates a simple scripting environment with its own interactive shell.

**It lets you:**

- Define variables
- Perform mathematical operations
- Loop values
- Manage your custom environment
- Run .ferm script files


All inside an interactive terminal. Think of it as a mini command language, written in Python, with authentication, error handling, and persistence built-in.


---

## ✨ Features

#### 1. 🔑 Authentication System

- **Username management** → reset username {name}

- **Password authentication with file-based persistence**

- **Lockout after 5 wrong attempts (30 minutes cooldown)**


#### 2. 🧮 Mathematical Operations

- `int`, `add`, `sub`, `mul`, `div`, `mod`

- Graceful handling of `ZeroDivisionError` & `TypeError`


#### 3. 📝 Variable Management

- Create and store integers & strings
- Rename variables
- Delete variables
- List all variables
- Purge entire variable environment


#### 4. 🔄 Looping Support

- `loop 5 {var}` → print a variable multiple times efficiently


#### 5. 🖨️ Output & Type Checking

- Print variable values
- Check data type of a variable


#### 6. 📜 Script Execution

Run `.ferm` script files via:

```
ferm run file.ferm
```


---

## 🚀 Getting Started

#### 1. Clone the Repository

```
git clone https://github.com/yourusername/fermion.git
```
```
cd fermion
```
#### 2. Run Fermion

```
python main.py
```
On first run, you’ll be asked to set:
- A username → saved in `authentication.fermlog`
- A password → saved in `password.fermlog`


#### 3. Interactive Shell

After authentication, you’ll enter the Fermion shell:

```
>>> yourname@fermion ~$
```

---

📖 Commands

🔹 Variable Management

int x = 10           # Create integer variable x
str msg = Hello      # Create string variable
rename x y           # Rename variable x to y
list                 # Show all variables
del x                # Delete variable x
purge                # Clear all variables

🔹 Math Operations

add x + y            # Add values of x and y
sub a - b            # Subtract b from a
mul a * b            # Multiply two variables
div a / b            # Divide a by b
mod z                # Print absolute/modulus of z

🔹 Utility

print var1           # Display a variable’s value
type var2            # Show the type of a variable
loop 5 message       # Print variable message 5 times

🔹 System & File Execution

ferm run script.ferm # Execute a .ferm script file line by line
reset username John  # Change active username
exit                 # Exit Fermion


---

📜 Example Session

Welcome to Fermion
Creating Environment...
Logged in as @coder123

>>> coder123@fermion ~$ int a = 10
>>> coder123@fermion ~$ int b = 5
>>> coder123@fermion ~$ add a + b
15
>>> coder123@fermion ~$ mul a * b
50
>>> coder123@fermion ~$ rename a alpha
Renamed a to alpha
>>> coder123@fermion ~$ list
Variables :
alpha = 10
b = 5
>>> coder123@fermion ~$ loop 3 alpha
10
10
10
>>> coder123@fermion ~$ str greeting = Hello
>>> coder123@fermion ~$ print greeting
Hello


---

📂 Script Execution (.ferm Files)

example.ferm

int x = 100
int y = 25
add x + y
div x / y
str msg = FermionWorks!
print msg

Run in shell:

>>> yourname@fermion ~$ ferm run example.ferm


---

⚠️ Error Handling

Fermion provides user-friendly error messages:

Invalid command →
<SyntaxError>: Invalid Command

Variable not found →
<NameError>: Variable 'x' not Defined

Divide by zero →
<ZeroDivisionError>: Can't Divide by zero

Type mismatch →
<TypeError>: Not an integer



---

🔒 Authentication

First run → set username & password

Username saved in authentication.fermlog

Password saved in password.fermlog

5 wrong attempts → 15 min lockout



---

🛠️ Future Improvements

Boolean/logical operators

Arrays/lists support

File-based persistent variables

Built-in scripting stdlib



---

💡 Why "Fermion"?

In physics, fermions are the fundamental building blocks of matter.
Similarly, Fermion is designed as a fundamental building block interpreter for learning and experimenting with language creation.


---

📜 License

This project is open-source under the MIT License.


---

