
markdown
Copy
Edit
# Python Script: Student Marks & List Operations

## 📌 Description
This Python script performs two tasks:
1. **Student Marks Lookup** – Retrieves a student's marks from a predefined dictionary.
2. **List Operations** – Extracts and reverses the first five elements from a list.

---

## 🖥️ Code Overview

### **Part 1: Student Marks Lookup**
- Creates a dictionary containing student names and their marks.
- Asks the user to input a student's name.
- Displays the marks if the name exists in the dictionary, otherwise shows a "not found" message.

```python
# Step 1: Create a dictionary with student names and their marks
students = {
    "Alice": 85
}

# Step 2: Ask the user to input a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show not found message
if name in students:
    print(f"{name}'s marks are: {students[name]}")
else:
    print(f"Sorry, no record found for '{name}'.")
Part 2: List Operations
Creates a list of numbers from 1 to 10.

Prints the original list.

Extracts the first five elements.

Reverses the extracted elements.

python
Copy
Edit
# Step 1: Create a list
numbers = [1,2,3,4,5,6,7,8,9,10]

# Step 2: Print the original list
print("Original list:", numbers)

# Step 3: Extract the first five elements
first_five = numbers[:5]

# Step 4: Reverse the extracted elements
reverse_five = first_five[::-1]

# Output
print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reverse_five)
📌 Example Output
yaml
Copy
Edit
Enter the student's name: Alice
Alice's marks are: 85
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]
⚠ Notes
Change the students dictionary to add more students and marks.

The list slicing [:5] extracts the first 5 elements (index 0 to 4).

Reversing is done using [::-1]# Data_structures_String
