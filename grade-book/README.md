# Gradebook

## Overview

Welcome to the Gradebook project! This project is designed to help you organize your subjects and grades using Python lists. It will guide you through various tasks and exercises to practice list manipulation and organization.

## Project Goals

- Organize subjects and grades in Python lists.
- Learn how to perform operations on lists such as adding, updating, and removing elements.
- Understand how to access and modify elements in a two-dimensional list.

## Getting Started

### Prerequisites

- Basic knowledge of Python programming.
- Familiarity with Python lists and basic list operations.

### Project Structure

The project consists of Python scripts and exercises focusing on list operations. You will be working with lists to:

1. **Create a Gradebook:** Define a list to store subjects and their respective grades.
2. **Update Entries:** Modify entries in the list to update grades or subjects.
3. **Remove Entries:** Remove specific entries from the list.
4. **Access Data:** Retrieve and display specific grades or subjects.

### Example Code

Below are some examples of the tasks you might perform:

1. **Create a Gradebook:**

    ```python
    gradebook = [["Math", 85], ["English", 90], ["History", 78]]
    ```

2. **Update an Entry:**

    ```python
    # Update grade for English
    index = [subject[0] for subject in gradebook].index("English")
    gradebook[index][1] = 95
    ```

3. **Remove an Entry:**

    ```python
    # Remove History from the gradebook
    gradebook = [entry for entry in gradebook if entry[0] != "History"]
    ```

4. **Access Data:**

    ```python
    # Access the grade for Math
    math_grade = next(grade for subject, grade in gradebook if subject == "Math")
    ```

## How to Contribute

Feel free to fork the repository, make changes, and submit a pull request. If you encounter any issues or have suggestions for improvements, please open an issue on the project's GitHub page.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [Python's Official Documentation](https://docs.python.org/3/) for providing comprehensive Python programming resources.

