# Introduction to Python, Variables and Data Types

## What is Programming?

The process of preparing an instructional program for a device (such as a computer).

## What are Programming Languages?

It acts as a middle-man or translator for translating a program into machine code.

## How do computers perform tasks?

- To perform any task, we need 2 things
  - **The language that computers understand**
  - **Programming Environment**

## Programming Environment➖

- A programming environment combines hardware and software and allows a developer to build applications.
- Developers typically work in **integrated development environments or IDEs**.
- These connect users with all the features necessary to write and test their code correctly.
- Different IDEs will offer other capabilities and advantages.
- Examples of IDEs ➖ **Visual Studio, NetBeans, Eclipse, IntelliJ**, etc.

## What is Python?

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.

| Term              | Meaning                                                       |
| ----------------- | ------------------------------------------------------------- |
| Interpreted       | Executes code line-by-line, no need to compile                |
| Object-Oriented   | Supports class and object-based program structure             |
| High-Level        | Easy to read/write, abstracted from hardware                  |
| Dynamic Semantics | Variables don’t need types declared, type checking at runtime |

Created by Guido van Rossum in 1991 at CWI (Centrum Wiskunde & Informatica), Netherlands.

## General-Purpose Language

Python can be used for:

AI & Machine Learning

Data Science (Most popular choice!)

Web Development (Django/Flask frameworks)

Automation and Scripting

Famous Companies Using Python + Django:
YouTube, Spotify, Pinterest, Instagram, Dropbox

## Why the name “Python”?

Inspired by the BBC comedy “Monty Python’s Flying Circus”.
Guido wanted a name that was short, unique, and mysterious.

## Why Learn Python?

- Simple & Easy to Learn
- Dynamic and Powerful
- Huge Library Ecosystem (130,000+ packages)
- Free and Open Source
- Platform Independent
- Interpreted (no need to compile)
- Robust Exception Handling

## Indentation in Python

Python uses indentation to define blocks of code instead of curly braces {}.

```
    if True:
    print("This is indented correctly")
    ❌ Indentation error if not properly aligned.

```

---

## Note => The extension used for Python files is .py.

## Printing Output in Python

Use the built-in print() function:

```
    print("Hello, world!")
```

You can print strings, numbers, and variables.

## Python Comments

Used to explain code and prevent execution.

### Single-line comment:

```
# This is a comment
```

### Multi-line comment:

```
'''
This is
a multi-line comment
'''

```

## What is a Variable?

A named container to store data.

```
name = "Alice"
age = 25
```

Think of variables as boxes with labels.
(CASE SENSITIVE)

## Check Variable Type

```
print(type(name))   # <class 'str'>
print(type(age))    # <class 'int'>
```

Python is a fantastic language that automatically identifies the type of data for us.

## Rules for Declaring Variables

### Valid Names:

1. Must start with a letter or \_ (underscore)
2. Can contain letters, numbers, and underscores
3. Case-sensitive (age, Age, and AGE are different)
4. Don't Use Keywords

## Data Types in Python

<img src="./dataType.png" width="60%"/>

Can you store milk in a basket or can you use a bottle to store fruits?

We are using different types of containers to store different things.

While the bottle can hold milk or water or juice, it will hold only liquids.

Similarly,

- A variable of type **_string_** (like the variable - *custName*), can store only strings.
- A variable of type **int** (like the variable - *custAge)* can store only integers.
- A variable of type **boolean** (like the variable - *custMaritalStatus)* can store either true or false.
- A variable of type **float** (like the variable - fruitWeight*)* can store only decimal values.

*The type of data a variable can hold is called its* **Data type**.
It may be **int**, **string, boolean, float,** etc. (A variable of type Boolean can either be *True* or *False).*

| Data Type | Example         | Description     |
| --------- | --------------- | --------------- |
| `str`     | `"Alice"`       | Text values     |
| `int`     | `25`            | Whole numbers   |
| `float`   | `3.14`          | Decimal numbers |
| `bool`    | `True`, `False` | Logical values  |

## Type **Casting in Python**

Type Casting is the method to convert the variable data type into a certain data type in order to the operation required to be performed by users.

There can be two types of Type Casting in Python –

- Implicit Type Casting
- Explicit Type Casting

### Implicit Type Casting

In this, Python **converts the data type** into another data type **automatically**. In this process, users don’t have to involve in this process.

### Explicit Type Casting

In this, Python needs **user involvement to convert the variable data type** into a certain data type in order to the operation required.

Mainly type casting can be done with these data type functions:

- **int():** int() function take float or string as an argument and return int type object.
- **float():** float() function takes int or string as an argument and returns float type object.
- **str():** str() function take float or int as an argument and return string type object.
- **bool():** bool() function take float, string or int as an argument and return a boolean-type object. Number other than 0 change into True. Empty String change into False.

## Many Values to Multiple Variables

Python allows you to assign values to multiple variables in one line.

Ex➖

```
x,y,z= "box", "pencil", "eraser"

print(x)    # box
print(z)    # pencil
print(y)    # eraser
# The number of variables matches the number of values, or else you will get an error
```

## One Value to Multiple Variables

Python allows you to assign the *same* value to multiple variables in one line.

Ex➖

```cpp
a=b=c="Maggi"
print(a)    # Maggi
print(b)    # Maggi
print(c)    # Maggi
```

---

## Mathematical Operators

The mathematical operators in Python are :

- **Addition Operator**
- **Subtraction Operator**
- **Multiplication Operator**
- **Division Operator**
- **Modulo Operator** => gives the remainder
- **Exponentiation Operator** => compute the power of any number

## String Concatenation

- Concatenation means a series of interconnected things.
- Use **+** to join two or more string

```
  a="Hii...."
  b="Sam...."
  print(a+b)          # Hii....Sam....
```

## Comparison Operators

Comparison operators are used for comparing two values.

- There are 6 comparison operators:
  - **> (Greater Than)**
  - **>= (Greater Than Equal To)**
  - **< (Less Than)**
  - **<= (Less Than Equal To)**
  - **== (Equal)**
  - **!= (not Equal)**
- The result of a comparison operator is always a boolean value.

## Logical Operators

A logical operator is a symbol or word used to connect two or more expressions.

## Types of Logical Operators

Python provides three logical operators:

1. and
2. or
3. not

## Assignment Operators

Assignment operators are used to assign values to variables.

- The most common is `=`, which assigns the right-hand side value to the left-hand side variable.
- Python also supports compound assignment operators.

### Types of Assignment Operators:

| Operator | Description             | Example          |
| -------- | ----------------------- | ---------------- |
| =        | Assign value            | a = 5            |
| +=       | Add and assign          | a += 2 (a = a+2) |
| -=       | Subtract and assign     | a -= 2 (a = a-2) |
| \*=      | Multiply and assign     | a *= 3 (a = a*3) |
| /=       | Divide and assign       | a /= 2 (a = a/2) |
| %=       | Modulo and assign       | a %= 2 (a = a%2) |
| //=      | Floor divide and assign | a //= 2          |
| \*\*=    | Exponent and assign     | a \*\*= 2        |

## Membership Operators

Membership operators are used to test whether a value is a member of a sequence (like string, list, tuple, etc.).

### Types of Membership Operators:

| Operator | Description                 |
| -------- | --------------------------- |
| in       | Returns True if present     |
| not in   | Returns True if not present |

### Note: Membership checks are case-sensitive.

## Conditional Statements

Conditional Statements in Python perform different computations or actions depending on whether a specific Boolean constraint evaluates to true or false.

- Conditional statements are used **to decide the flow of execution based on different conditions**. If a condition is true, you can perform one action and if the condition is false, you can perform another action.
- Through Conditional Statements, we can control which code needs to run or which code will not run.

For Example: the traffic light controls the flow of vehicles on the road.

- Depending upon the color of the light, the actions happened.
- If the light is green, then it is a signal to move.
- If the light is red then it is a signal to stop.

## Different Types of Conditional Statements

There are four types of conditional statements in Python.

1. If statement
2. If…Else statement
3. If…Elif…Else statement
4. Nested If

## Ternary Operator

- Ternary operators also known as **conditional expressions** are operators that evaluate something based on a condition being true or false.
- It was added to Python in version **2.5.**
- It simply allows testing a condition in a **single line** replacing the multiline if-else making the code compact.
- Syntax➖
  ```
  [on_true] if [expression] else [on_false]
  ```
- For ex-

  ```
  # to check whether a number is odd or even
  a=10;
  print("Even Number") if(a%2==0) else print("Odd Number");

  x = 5
  result = "Greater" if x > 10 else "Equal" if x == 10 else "Less"
  print(result)
  ```
