txt_filePath = "PythonDemos/5.FileHandling/resources/sample.txt"
json_filePath = "PythonDemos/5.FileHandling/resources/sample.json"
csv_filePath = "PythonDemos/5.FileHandling/resources/sample.csv"

#region CRUD operations for Text file
# Create/Write to Text file
with open(txt_filePath, "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample text file.\n")
    print("Text File Written Successfully")

# Read Text file
with open(txt_filePath, "r") as file:
    content = file.read()
    print("\nText File Content After Write:")
    print(content)

# Update Text file (append new content)
with open(txt_filePath, "a") as file:
    file.write("Appending a new line to the text file.\n")
    print("\nNew Line Appended to Text File")

# Read Text file again to verify update
with open(txt_filePath, "r") as file:
    content = file.read()
    print("\nText File Content After Append:")
    print(content)

# Delete operation (clear the file content)
with open(txt_filePath, "w") as file:
    file.write("")
    print("\nText File Content Cleared")
#endregion


#region CRUD operations for CSV file
import csv
# Create/Write to CSV file
with open(csv_filePath, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])
    print("CSV File Written Successfully")

# Read CSV file
with open(csv_filePath, mode="r") as file:
    reader = csv.reader(file)
    print("\nCSV File Content:")
    for row in reader:
        print(row)

# Update CSV file (append a new row)
with open(csv_filePath, mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Charlie", 35, "Chicago"])
    print("\nNew Row Appended to CSV File")

# Delete operation (recreate file without specific rows)
with open(csv_filePath, mode="r") as file:
    rows = list(csv.reader(file))

with open(csv_filePath, mode="w", newline="") as file:
    writer = csv.writer(file)
    for row in rows:
        if row[0] != "Bob":  # Exclude rows where Name is "Bob"
            writer.writerow(row)
    print("\nRow Deleted from CSV File")
#endregion


#region CRUD operations for JSON file
import json
# Read JSON file
with open(json_filePath, "r") as file:
    data = json.load(file)
    print("\nJSON File Content:")
    print(data)

# Update JSON data
data["new_key"] = "new_value"

# Write updated data back to JSON file
with open(json_filePath, "w") as file:
    json.dump(data, file, indent=4)
    print("\nUpdated JSON File Written Successfully")
#endregion