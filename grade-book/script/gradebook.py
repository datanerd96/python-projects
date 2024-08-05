# Defining the grades from the last semester
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Creating a list of subjects
subjects = ["physics", "calculus", "poetry", "history"]

# Creating a list of grades corresponding to the subjects
grades = [98, 97, 85, 88]

# Creating a 2D list (a list of lists) to represent a gradebook manually
gradebook = [grades, subjects]
print(gradebook)  # Output the current gradebook

# Adding a new subject and grade separately to the gradebook
gradebook.append("computers science")  # Incorrectly adding a subject as a single string
gradebook.append(100)  # Incorrectly adding a grade as a single integer
print(gradebook)  # Output the gradebook after adding

# Adding a new subject and grade as a list
gradebook.append(["visual arts", 93])  # Correctly adding a subject with grade as a list
print(gradebook)  # Output the gradebook after adding

# Updating the grade for 'visual arts' by incrementing it by 5
visual_arts_index = gradebook[4][1]  # Retrieve the grade for 'visual arts'
gradebook[4][1] = visual_arts_index + 5  # Update the grade for 'visual arts'
print(gradebook)  # Output the gradebook after updating

# Removing the grade 85 from the gradebook
sublist_with_85 = gradebook[0]  # Retrieve the grades list
sublist_with_85.remove(85)  # Remove the grade 85 from the list
print(gradebook)  # Output the gradebook after removing

# Adding 'Pass' to the list of grades
sublist_with_pass = gradebook[0]  # Retrieve the grades list
sublist_with_pass.append("Pass")  # Add 'Pass' to the list
print(gradebook)  # Output the gradebook after adding 'Pass'

# Combining the last semester's gradebook with the current gradebook
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)  # Output the full gradebook

