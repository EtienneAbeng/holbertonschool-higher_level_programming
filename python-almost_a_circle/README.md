# Learning Objectives

## General

### Unit Testing
Unit testing is a software testing technique where individual units or components of a software application are tested in isolation to ensure they behave as expected. In a large project, unit testing helps to verify the correctness of individual functions, classes, or modules. 

To implement unit testing in a large project:
- Identify units/components to test
- Write test cases covering various scenarios and edge cases
- Choose a testing framework (e.g., unittest, pytest)
- Organize test files mirroring the project structure
- Write test code using assertions
- Run tests using the testing framework's interface
- Integrate unit testing into the continuous integration (CI) pipeline

### Serialization and Deserialization
Serialization is the process of converting a data structure or object into a format that can be stored or transmitted, while deserialization is the reverse process. In Python, the `pickle` module is commonly used for serialization and deserialization of Python objects.

### JSON Handling
JSON (JavaScript Object Notation) is a lightweight data interchange format. Python provides the `json` module to work with JSON data. You can serialize Python objects to JSON strings and deserialize JSON strings to Python objects using this module.

### *args and **kwargs
`*args` and `**kwargs` are special syntax in Python used to pass a variable number of arguments to a function. 
- `*args` is used to pass a variable number of positional arguments to a function.
- `**kwargs` is used to pass a variable number of keyword arguments to a function.

### Named Arguments in Functions
Named arguments in functions allow you to specify arguments by their parameter names when calling a function. This provides clarity and flexibility in function calls, especially for functions with many parameters.

## Requirements

### Python Scripts
- All scripts should end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- Include a README.md file at the root of the project folder
- Use `pycodestyle` for code formatting
- All files must be executable
- Document modules, classes, and functions using docstrings
- A documentation should be a sentence explaining the purpose of the module, class, or method
- Use Python version 3.8.5

### Python Unit Tests
- All test files should end with a new line
- Test files should be inside a `tests` folder
- Use the `unittest` module for writing tests
- Test files should start with `test_`
- Organize test files similar to the project structure
- Execute tests using `python3 -m unittest discover tests`

We encourage collaboration on test cases to ensure all edge cases are covered.

## Collaboration
Working together on test cases can help identify and cover all edge cases, ensuring comprehensive testing of the project. Collaboration fosters better understanding of the codebase and improves the quality of the tests.

---
