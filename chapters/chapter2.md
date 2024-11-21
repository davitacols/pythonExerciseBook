# Chapter 2: Variables and Data Types
## Making Your Programs Remember Things

### Introduction: What Are Variables?

#### The Box Analogy
Imagine you have a bunch of labeled boxes. In one box labeled "age," you put the number 25. In another box labeled "name," you put the text "Alice." Variables in Python work exactly like this! They're containers that:
- Have names (like "age" or "name")
- Store values (like numbers or text)
- Can be changed whenever you want

```python
age = 25        # Creating a box labeled "age" and putting 25 in it
name = "Alice"  # Creating a box labeled "name" and putting "Alice" in it
```

### Creating Variables

#### Basic Rules for Variable Names
1. **Must start with a letter or underscore:**
```python
# Good variable names
name = "John"
_secret = "hidden"
age = 30

# Bad variable names (these will cause errors)
2name = "John"    # Can't start with a number
my-name = "John"  # Can't use hyphens
```

2. **Can contain letters, numbers, and underscores:**
```python
user_age = 25        # Using underscore (snake_case)
myAge = 25          # Using camel case
PlayerScore = 100   # Using pascal case
```

3. **Case sensitive (age and Age are different):**
```python
age = 25
Age = 30
AGE = 35
# These are three different variables!
```

4. **Can't use Python's special keywords:**
```python
# These won't work
class = "Biology"    # 'class' is a Python keyword
if = 5              # 'if' is a Python keyword

# Use these instead
class_name = "Biology"
if_value = 5
```

### Data Types in Python

#### 1. Numbers

##### Integers (Whole Numbers)
```python
age = 25
temperature = -10
students = 1000

# Operations with integers
sum = 5 + 3         # Addition
difference = 10 - 7  # Subtraction
product = 4 * 3     # Multiplication
quotient = 15 // 2  # Integer division (removes decimal)
```

##### Floating-Point Numbers (Decimals)
```python
price = 19.99
height = 1.75
pi = 3.14159

# Operations with floats
total = 19.99 + 0.99    # Addition
weight = 75.5 - 2.5     # Subtraction
area = 3.14 * (2 ** 2)  # Multiplication and powers
```

##### Number Systems
```python
# Binary (base 2)
binary = 0b1010    # Equal to 10 in decimal

# Octal (base 8)
octal = 0o17       # Equal to 15 in decimal

# Hexadecimal (base 16)
hexa = 0xFF        # Equal to 255 in decimal
```

#### 2. Strings (Text)

##### Creating Strings
```python
# Different ways to create strings
name = "Alice"
message = 'Hello, World!'
long_text = """This is a
multi-line
string"""

# String operations
greeting = "Hello" + " " + "World"    # Concatenation
repeated = "Ha" * 3                   # Repetition (HaHaHa)
```

##### String Methods
```python
text = "Hello, World!"

# Common string operations
print(text.upper())         # HELLO, WORLD!
print(text.lower())         # hello, world!
print(text.replace("H", "J"))  # Jello, World!
print(len(text))           # 13 (length of string)
```

##### String Formatting
```python
name = "Alice"
age = 25

# Different ways to format strings
# Method 1: f-strings (recommended)
message1 = f"My name is {name} and I am {age} years old"

# Method 2: .format()
message2 = "My name is {} and I am {} years old".format(name, age)

# Method 3: % operator (older style)
message3 = "My name is %s and I am %d years old" % (name, age)
```

#### 3. Booleans (True/False)
```python
is_student = True
is_working = False

# Boolean operations
has_access = is_student or is_working   # True
can_vote = age >= 18                    # True if age is 18 or more
```

#### 4. None (Nothing)
```python
# None represents the absence of a value
empty_variable = None
```

### Type Conversion

#### Converting Between Types
```python
# String to Number
age_str = "25"
age_num = int(age_str)      # Convert to integer
price_str = "19.99"
price_num = float(price_str)  # Convert to float

# Number to String
count = 100
count_str = str(count)      # Convert to string

# Example: User Input Processing
user_input = input("Enter your age: ")  # Always returns a string
user_age = int(user_input)              # Convert to number for calculations
```

### Practical Examples

#### 1. Simple Calculator
```python
# Getting user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing calculations
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
div_result = num1 / num2

# Displaying results
print(f"Sum: {sum_result}")
print(f"Difference: {diff_result}")
print(f"Product: {prod_result}")
print(f"Division: {div_result}")
```

#### 2. Personal Information Manager
```python
# Collecting information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

# Creating a summary
print("\n=== Personal Information ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}m")
print(f"Student Status: {'Student' if is_student else 'Not a Student'}")
```

#### 3. Shopping Cart Calculator
```python
# Item prices
banana_price = 0.49
apple_price = 0.89
orange_price = 0.59

# Quantities
banana_qty = int(input("How many bananas? "))
apple_qty = int(input("How many apples? "))
orange_qty = int(input("How many oranges? "))

# Calculations
subtotal = (banana_price * banana_qty + 
           apple_price * apple_qty + 
           orange_price * orange_qty)
tax_rate = 0.08
tax = subtotal * tax_rate
total = subtotal + tax

# Receipt
print("\n=== Shopping Receipt ===")
print(f"Bananas: ${banana_price * banana_qty:.2f}")
print(f"Apples: ${apple_price * apple_qty:.2f}")
print(f"Oranges: ${orange_price * orange_qty:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
```

### Common Mistakes and How to Fix Them

#### 1. Type Mismatch
```python
# Wrong
age = "25"
result = age + 5  # Error! Can't add string and number

# Correct
age = int("25")
result = age + 5  # Works! Now age is a number
```

#### 2. Variable Name Errors
```python
# Wrong
first name = "John"    # Space not allowed
print = "Hello"        # Don't use Python keywords

# Correct
first_name = "John"
message = "Hello"
```

#### 3. Case Sensitivity
```python
# Wrong
Name = "Alice"
print(name)  # Error! 'name' is not defined

# Correct
name = "Alice"
print(name)  # Works!
```

### Practice Exercises

#### Basic Exercises
1. Create variables for your name, age, and favorite color
2. Calculate your age in months
3. Create a program that converts kilometers to miles
4. Make a temperature converter (Celsius to Fahrenheit)

#### Intermediate Exercises
1. Create a BMI calculator
2. Build a simple interest calculator
3. Make a grade calculator
4. Create a time converter (seconds to hours/minutes/seconds)

#### Advanced Exercises
1. Create a currency converter with multiple currencies
2. Build a pizza order calculator with toppings
3. Make a workout tracker that calculates calories burned
4. Create a monthly budget calculator

### Looking Ahead
Next chapter, we'll learn about:
- Making decisions with if statements
- Comparing values
- Creating conditions
- Building more complex programs

### Quick Reference
```python
# Variable Creation
variable_name = value

# Data Types
number = 42          # Integer
decimal = 3.14       # Float
text = "Hello"       # String
is_true = True       # Boolean
empty = None         # None

# Type Conversion
str()    # Convert to string
int()    # Convert to integer
float()  # Convert to decimal
bool()   # Convert to boolean

# String Operations
len()    # Get length
.upper() # Convert to uppercase
.lower() # Convert to lowercase
.strip() # Remove whitespace
```