# Task Management System

#### Video Demo: <https://youtu.be/fRrvmS8kfeM>

#### Description:
This Task Management System is a simple command-line application written in Python that allows users to manage their tasks efficiently. The project demonstrates the use of functions, data structures, and basic input/output operations in Python.

## Features

1. Add tasks with descriptions and due dates
2. View all tasks with their status (pending or completed)
3. Mark tasks as complete
4. Simple and intuitive command-line interface

## Files

### project.py

This is the main file containing the core functionality of the Task Management System. It includes the following functions:

- `main()`: The main function that runs the program and handles user input.
- `add_task()`: Allows users to add a new task with a description and due date.
- `view_tasks()`: Displays all tasks with their details and status.
- `mark_task_complete()`: Enables users to mark a task as complete.

The file uses the `datetime` module to handle dates and the `sys` module for program exit.

### test_project.py

This file contains pytest test functions for the main functionality of the Task Management System. It includes tests for:

- `test_add_task()`: Verifies that tasks are added correctly.
- `test_view_tasks()`: Ensures that tasks are displayed properly.
- `test_mark_task_complete()`: Checks if tasks can be marked as complete.

The test file uses pytest fixtures and monkeypatching to simulate user input and capture output.

### requirements.txt

This file lists the external dependencies required for the project, which is only pytest for running the tests.

## Design Choices

1. **Data Structure**: I chose to use a list of dictionaries to store tasks. Each dictionary represents a task with keys for description, due date, and completion status. This structure allows for easy addition, retrieval, and modification of tasks.

2. **Command-line Interface**: The project uses a simple menu-based interface for ease of use. While a graphical interface could have been implemented, a CLI keeps the project focused on Python programming concepts.

3. **Date Handling**: The `datetime` module is used to handle dates, ensuring proper date formatting and allowing for future extensions like task sorting or filtering by date.

4. **Testing**: Pytest was chosen for its simplicity and powerful features. The tests cover the core functionality of the program, ensuring reliability.

## Possible Improvements

1. Implement data persistence (e.g., saving tasks to a file or database)
2. Add more features like task editing, deletion, or sorting
3. Implement error handling for edge cases
4. Add color coding for better visual representation in the CLI

This project serves as a foundation for a task management system and demonstrates key programming concepts taught in CS50P.
