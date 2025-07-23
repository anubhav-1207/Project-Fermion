# Project Fermion 

Fermion Programming Language Specification
Fermion is a low-level, compiler-based programming language designed to be expressive, minimal, and structured. This document provides a detailed and beginner-friendly explanation of every syntax element introduced so far.

---

### **🚀 1. Memory Allocation (Startup Requirement)**

Every Fermion program must begin by specifying how much memory it will use.

🔑 Keywords:

`alloc limit NULL` -  allocates unlimited memory.

`alloc bytelimit 5M` — allocates a memory limit of 5 megabytes.

• Note: Memory is specified only in megabytes. For gigabytes, multiply by 1024.


✅ Example:

```Fermion
alloc limit NULL

alloc bytelimit 20M
```


---

### **🏁 2. Entry Point: Main Function**

Fermion programs begin execution from:

```Fermion
func main index[0]:
```

This marks the starting point of execution. index[0] indicates the entry position (can be extended later).

✅ Example:
``` Fermion
func main index[0]:
    arch.return{str("Hello World")}
func end index[0]
```

###### **⚠️ Notes:

Every program must have `func main index[0]:` and a matching `func end index[0].`

These define the start and end of the executable code block.

---

### 📤 3. Output: Returning Data

Fermion uses `arch.return{...}` to return or print output to the terminal.

###### Syntax:

```Fermion
arch.return{TYPE("value")}

Where TYPE can be:

str() for strings

int() for integers

var() to output a variable’s value

join[...] to concatenate multiple types (see below)
```
###### ✅ Example:

``` Fermion
arch.return{str("Hello World")}

var x = int(5)
arch.return{var(x)}
```



---

### 📦 4. Variable Declaration

Variables are defined with the var keyword, followed by an assignment using a data type.

###### 🔧 Syntax:

`var variable_name = TYPE(value)`

Where TYPE can be any supported data type: `int`, `str`, `bool`, `float`, `list`, etc.

✅ Examples:

```Fermion
var name = str("John")
var age = int(30)
var active = bool(true)
```
##### 🔁 Reassignment:

Use `revar` instead of `var` to reassign a value.

```Fermion
revar age = int(35)
```


---

### ➕ 5. Operations with opr[...]

Fermion supports mathematical and string operations using the `opr[...]` syntax.

###### 🧮 Numeric Operations:

``` Fermion
var a = int(5)
var b = int(3)
var c = opr[var a + var b]
arch.return{var(c)}
```
###### 🔠 String Multiplication:

```Fermion
var laugh = str("ha")
var result = opr[var laugh * int(3)]
arch.return{var(result)}
```
###### ⚡ Direct Literal Operations:

`arch.return{opr[str("ha") * int(3)]}  # Output: hahaha`

###### ⚠️ Rules:

> Only str * int is allowed.
> str * str is invalid.
> Negative multipliers return an empty string.



---

### 🔗 6. Concatenating Mixed Data: join[...]

Use `join[...]` inside `arch.return{}` to output multiple values of different types in a single statement.

###### ✅ Example:

``` Fermion 
var score = int(10)
arch.return{join["Score: ", var(score)]}
```
###### ⚠️ Notes:

`join[...]` automatically converts all elements to strings.

Use for readable output involving numbers and text.

---

📌 Design Notes:

1. Memory allocation is mandatory at the start.


2. main index[0] defines the program’s execution start.


3. arch.return{} is the only way to produce terminal output.


4. Data types must be explicitly declared when defining literals.

But when printing existing variables, use var(...) without type.



5. For string + number output, use join[...].


6. Operations (math or string) must always be done via opr[...].


7. Reassignment uses revar, not var.


8. All values passed directly (not through vars) must be wrapped with their type: str(), int(), etc.

---

## Example Project: User Info Processor 

``` Fermion
alloc bytelimit 5M

func main index[0]:

    # Ask for user input
    var name = input(str)
    var age = input(int)
    var score = input(int)

    # Give a 5 mark bonus
    var bonus = int(5)
    var final = opr[var score + var bonus]

    # Check pass/fail manually (simulate conditionals later)
    # If final >= 40 -> Pass, else Fail
    var result = str("Fail")  # Default
    var passing = int(40)

    # Simulated logic:
    # If final >= passing then revar result = str("Pass")
    # Since we can't do if-else yet, we'll override manually for demo
    revar result = str("Pass")  # Pretend score is above 40 always

    # Line separator
    var sep = str("=")

    # Output starts
    arch.return{var(sep) * int(30)}
    arch.return{join["Student Report for ", var(name)]}
    arch.return{join["Age: ", var(age)]}
    arch.return{join["Score (with bonus): ", var(final)]}
    arch.return{join["Result: ", var(result)]}
    arch.return{var(sep) * int(30)}

func end index[0]
```
