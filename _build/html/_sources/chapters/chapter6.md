# Chapter 6: Error Handling

## 6.1 Introduction to Errors and Exceptions

### 6.1.1 What are Exceptions?
Exceptions are unexpected events that disrupt the normal flow of a program. They are Python's way of signaling that something has gone wrong during program execution. Understanding and managing exceptions is crucial for writing robust, reliable code.

#### Types of Errors
1. **Syntax Errors**: Detected before the program runs
   - Incorrect indentation
   - Missing colons
   - Misspelled keywords

2. **Runtime Errors**: Occur during program execution
   - Division by zero
   - Accessing undefined variables
   - Attempting to use an index that doesn't exist

### 6.1.2 The Exception Hierarchy
```python
# Python's built-in exception hierarchy
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── ValueError
    ├── TypeError
    ├── IndexError
    └── KeyError
```

## 6.2 Basic Exception Handling

### 6.2.1 Try-Except Blocks
```python
# Basic exception handling
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Handling multiple exceptions
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

### 6.2.2 Handling Multiple Exceptions
```python
def process_data(data):
    try:
        # Multiple potential error points
        length = len(data)
        average = sum(data) / length
        return average
    except TypeError:
        print("Error: Data contains non-numeric values")
    except ZeroDivisionError:
        print("Error: Empty data list")
```

## 6.3 Advanced Exception Handling

### 6.3.1 Else and Finally Clauses
```python
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        # Runs if no exception occurs
        print(f"Division result: {result}")
    finally:
        # Always runs, with or without an exception
        print("Division operation completed")
```

### 6.3.2 Raising Exceptions
```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Invalid age")
    return age

try:
    user_age = validate_age(-5)
except ValueError as e:
    print(f"Validation Error: {e}")
```

## 6.4 Custom Exceptions

### 6.4.1 Creating Custom Exception Classes
```python
class InsufficientFundsError(Exception):
    """Custom exception for banking operations"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Insufficient funds. Balance: {balance}, Requested: {amount}"
        super().__init__(self.message)

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return amount
```

## 6.5 Best Practices in Error Handling

1. **Be Specific**: Catch specific exceptions, not generic ones
2. **Provide Meaningful Messages**: Give clear error descriptions
3. **Log Exceptions**: Use logging for tracking errors
4. **Avoid Silent Failures**: Always handle or report exceptions
5. **Use Context Managers**: Leverage `with` statements for resource management

## 6.6 Debugging Techniques

### 6.6.1 Print Debugging
```python
def complex_calculation(x, y):
    print(f"Input values: x={x}, y={y}")  # Debugging print
    try:
        result = x / y
        print(f"Intermediate result: {result}")
        return result
    except Exception as e:
        print(f"Error occurred: {e}")
```

### 6.6.2 Using the `traceback` Module
```python
import traceback

try:
    # Some complex operation
    risky_function()
except Exception:
    # Print full stack trace
    traceback.print_exc()
```

## 6.7 Practical Exercises

1. Create a calculator program with comprehensive error handling
2. Develop a file reading utility that gracefully handles various file-related exceptions
3. Build a user registration system with input validation

## Conclusion

Error handling is not just about preventing crashes—it's about creating resilient, user-friendly applications that can gracefully manage unexpected situations.

### Learning Objectives
- Understand Python's exception mechanism
- Write robust error-handling code
- Create custom exceptions
- Implement debugging strategies

### Recommended Resources
- Python Official Documentation on Exceptions
- "Effective Python" by Brett Slatkin
- Online Python debugging tutorials