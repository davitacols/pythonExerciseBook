# Chapter 7: File Operations

## 7.1 Introduction to File Handling

### 7.1.1 Why File Operations Matter
Files are essential for:
- Data persistence
- Configuration management
- Logging
- Data analysis
- Sharing information between programs

### 7.1.2 File Types and Modes
- Text files
- Binary files
- Read modes
- Write modes
- Append modes

## 7.2 Basic File Reading

### 7.2.1 Opening and Reading Files
```python
# Reading entire file
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('sample.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Reading specific number of lines
with open('sample.txt', 'r') as file:
    first_line = file.readline()
    lines = file.readlines()
```

### 7.2.2 File Reading Techniques
```python
# Reading CSV files
import csv

with open('data.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    headers = next(csv_reader)  # Read header row
    for row in csv_reader:
        print(row)
```

## 7.3 Writing to Files

### 7.3.1 Basic File Writing
```python
# Writing text files
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.writelines(["Line 1\n", "Line 2\n"])

# Appending to files
with open('log.txt', 'a') as file:
    file.write("New log entry\n")
```

### 7.3.2 Writing Complex Data
```python
# Writing CSV files
import csv

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'San Francisco']
]

with open('users.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data)
```

## 7.4 Working with Binary Files

### 7.4.1 Image and Binary File Handling
```python
# Reading binary files
with open('image.jpg', 'rb') as image_file:
    image_data = image_file.read()

# Writing binary files
with open('output.jpg', 'wb') as output_file:
    output_file.write(image_data)
```

## 7.5 Advanced File Operations

### 7.5.1 File and Directory Management
```python
import os
import shutil

# Check file existence
if os.path.exists('data.txt'):
    print("File exists")

# Create directories
os.makedirs('logs/archive', exist_ok=True)

# Copying and moving files
shutil.copy('source.txt', 'destination.txt')
shutil.move('old_location.txt', 'new_location.txt')
```

### 7.5.2 JSON File Handling
```python
import json

# Writing JSON
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

with open('data.json', 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)

# Reading JSON
with open('data.json', 'r') as jsonfile:
    loaded_data = json.load(jsonfile)
```

## 7.6 Error Handling in File Operations

### 7.6.1 Common File-Related Exceptions
```python
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No permission to read file")
except IOError:
    print("Input/Output error occurred")
```

## 7.7 Best Practices

1. Always use `with` statements
2. Close files explicitly
3. Handle potential exceptions
4. Use appropriate file modes
5. Be mindful of file paths
6. Use context managers

## 7.8 Practical Exercises

1. Create a log file analyzer
2. Build a simple note-taking application
3. Develop a CSV data processor
4. Implement a configuration file reader

## Conclusion

File operations are a fundamental skill in Python, enabling data persistence, configuration management, and complex I/O operations.

### Learning Objectives
- Read and write files
- Handle different file types
- Manage file system operations
- Implement error handling
- Use advanced file manipulation techniques

### Recommended Resources
- Python Official File I/O Documentation
- "Python Cookbook" by David Beazley
- Online Python file handling tutorials