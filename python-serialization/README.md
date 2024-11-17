# Python Serialization Project

## Overview

This project focuses on marshaling and serialization in Python. You will explore how data can be transformed and transmitted between systems and applications through different formats such as JSON, XML, and binary data (pickle). By completing the tasks in this project, you will strengthen your understanding of data manipulation and persistence across various serialization formats.

## Learning Objectives

- Understand the differences and similarities between marshaling and serialization.
- Implement serialization in practical tasks.
- Learn to serialize and deserialize data in various formats: JSON, CSV, XML, and binary (pickle).
- Handle data in applications requiring data persistence, distributed computing, or data sharing between software components.
- Work with different Python modules like `json`, `pickle`, `csv`, and `xml.etree.ElementTree`.

## Project Structure

- **task_00_basic_serialization.py**: Basic JSON serialization and deserialization.
- **task_01_pickle.py**: Serialize and deserialize a custom class using the `pickle` module.
- **task_02_csv.py**: Convert CSV data into JSON format.
- **task_03_xml.py**: Serialize and deserialize data to and from XML format.

---

## Tasks

### 0. Basic Serialization
**File**: `task_00_basic_serialization.py`

This task requires you to implement basic serialization and deserialization in Python using JSON. 

**Requirements**:
- Implement a function `serialize_and_save_to_file(data, filename)` to serialize a Python dictionary into a JSON file.
- Implement a function `load_and_deserialize(filename)` to load and deserialize the JSON file back into a Python dictionary.

**Example**:
```python
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
serialize_and_save_to_file(data_to_serialize, 'data.json')
deserialized_data = load_and_deserialize('data.json')
```

### 1. Pickling Custom Classes
**File**: `task_01_pickle.py`

In this task, you will learn how to serialize and deserialize a custom Python class using the `pickle` module.

**Requirements**:
- Create a class `CustomObject` with attributes: `name`, `age`, and `is_student`.
- Implement a `serialize(self, filename)` method to serialize the object to a file.
- Implement a class method `deserialize(cls, filename)` to load the object from the file and return an instance of the class.

**Example**:
```python
obj = CustomObject(name="John", age=25, is_student=True)
obj.serialize("object.pkl")
new_obj = CustomObject.deserialize("object.pkl")
```

### 2. Converting CSV Data to JSON Format
**File**: `task_02_csv.py`

This task focuses on converting CSV data into JSON format using serialization techniques.

**Requirements**:
- Implement a function `convert_csv_to_json(csv_filename)` that reads data from a CSV file, converts it to JSON format, and writes it to a `data.json` file.

**Example CSV** (`data.csv`):
```
name,age,city
John,28,New York
Alice,24,Los Angeles
Bob,22,Chicago
Eve,30,San Francisco
```

**Example**:
```python
convert_csv_to_json("data.csv")
```

### 3. Serializing and Deserializing with XML
**File**: `task_03_xml.py`

In this task, you will explore serialization and deserialization using XML.

**Requirements**:
- Implement a function `serialize_to_xml(dictionary, filename)` to serialize a Python dictionary into XML format.
- Implement a function `deserialize_from_xml(filename)` to deserialize XML data back into a Python dictionary.

**Example**:
```python
sample_dict = {'name': 'John', 'age': '28', 'city': 'New York'}
serialize_to_xml(sample_dict, "data.xml")
deserialized_data = deserialize_from_xml("data.xml")
```

---

## How to Run the Tests

To test each task, use the respective `main` files provided:

1. **Task 0 - Basic Serialization**:
   ```bash
   python3 python-serialization/main_00_basic_serialization.py
   ```

2. **Task 1 - Pickling Custom Classes**:
   ```bash
   python3 python-serialization/main_01_pickle.py
   ```

3. **Task 2 - Converting CSV to JSON**:
   ```bash
   python3 python-serialization/main_02_csv.py
   ```

4. **Task 3 - Serializing and Deserializing with XML**:
   ```bash
   python3 python-serialization/main_03_xml.py
   ```

---

## Resources

To complete this project, refer to the following resources:
- [Python’s `json` module](https://docs.python.org/3/library/json.html)
- [Python’s `pickle` module](https://docs.python.org/3/library/pickle.html)
- [Python’s `csv` module](https://docs.python.org/3/library/csv.html)
- [Python’s `xml.etree.ElementTree` module](https://docs.python.org/3/library/xml.etree.elementtree.html)

---

## Author

This project was created by El Famoso Enes as part of the Holberton School curriculum.
```