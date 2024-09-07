# TODO: Create a Python dictionary to serve as a hash table (employee database)
employee_db = {}

# TODO: Add employee names with their roles to the dictionary
employee_db["Alice"] = "Software Engineer"
employee_db["Bob"] = "Data Scientist"
employee_db["Charlie"] = "Product Manager"

# TODO: Print the initial employee database
print("Initial Employee Database:")
for name, role in employee_db.items():
    print(f"{name}: {role}")

# TODO: Update the role of an employee in the database
employee_db["Alice"] = "Senior Software Engineer"

# TODO: Print the database after the employee role update
print("\nEmployee Database after Role Update:")
for name, role in employee_db.items():
    print(f"{name}: {role}")

# TODO: Remove an employee from the database
del employee_db["Bob"]

# TODO: Print the final employee database after the removal
print("\nFinal Employee Database after Removal:")
for name, role in employee_db.items():
    print(f"{name}: {role}")
