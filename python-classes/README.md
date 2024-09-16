# Python - Classes and Objects

## Description

This project focuses on Object-Oriented Programming (OOP) in Python. The goal is to understand and implement concepts such as classes, objects, methods, encapsulation, data abstraction, and more, while working with Python-specific constructs like `__init__`, private attributes, and properties.

## Learning Objectives

At the end of this project, you should be able to explain:

- **OOP (Object-Oriented Programming)**: What it is and why it's important.
- **First-class everything**: How Python treats functions, classes, and other constructs as first-class objects.
- **Classes**: How to define a class and how it serves as a blueprint for creating objects.
- **Objects**: What objects are and how they are instances of classes.
- **Instance vs Class**: Differences between an instance and the class it is created from.
- **Attributes**: The characteristics or properties that objects of a class have.
- **Encapsulation**: How to protect attributes from being accessed directly, through private, public, and protected attributes.
- **`self`**: How it represents the current instance of the class.
- **Methods**: Functions that belong to a class and operate on its instances.
- **`__init__` method**: The constructor method for initializing new objects.
- **Data Abstraction and Information Hiding**: Concepts that allow hiding the internal state of objects.
- **Properties**: How to use properties instead of getter and setter methods in Python.
- **Dynamic Attributes**: How to create new attributes dynamically for instances.
- **Pythonic Getters and Setters**: How Python provides an elegant way to define getters and setters.
- **Attribute binding**: How attributes are bound to instances and classes.
- **`__dict__`**: What it contains and how Python finds the attributes of an object or class.
- **`getattr`**: How to use the `getattr` function to retrieve object attributes dynamically.

## Requirements

- Python 3.8.5
- All files must be executable and end with a new line.
- Code style should follow **Pycodestyle** version 2.7.*
- All modules, classes, and functions must have proper documentation.
  
## Project Tasks

### 0. My first square
Define an empty class `Square`.

### 1. Square with size
Define a class `Square` with a private attribute `size` and allow instantiation with this attribute.

### 2. Size validation
Extend the `Square` class to validate the `size` attribute, ensuring it is an integer and greater than or equal to 0.

### 3. Area of a square
Add a method `area()` to calculate the area of the square.

### 4. Access and update private attribute
Implement getter and setter properties for `size` to control access and validation of the private attribute.

### 5. Printing a square
Add a method `my_print()` to print the square using the `#` character.

### 6. Coordinates of a square
Enhance the `Square` class to include a `position` attribute and adjust the `my_print()` method to account for it.

## Usage

To test your implementation, you can run the provided main files like this:

```bash
./0-main.py
./1-main.py
...
