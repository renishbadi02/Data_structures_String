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




list = [1,2,3,4,5,6,7,8,9,10]
#print firs five element
print(list)
#extrect first five element 
first_five = list[:6]

#revers extrext element 
reverse_five = first_five[::-1]

print("Extrect fist five element:",first_five)
print("Revers extrect element:",reverse_five)