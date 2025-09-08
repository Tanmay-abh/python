import os
import shutil

# Global constants
FILENAME = "students.txt"
RENAMED_FILENAME = "student_records.txt"
DIRECTORY = "SchoolData"

# Sample data (used only for write operation)
sample_students = [
    {"name": "Alice", "roll": "101", "marks": 88},
    {"name": "Bob", "roll": "102", "marks": 75},
    {"name": "Charlie", "roll": "103", "marks": 92}
]

def write_file():
    with open(FILENAME, "w") as file:
        file.write("Name,Roll Number,Marks\n")
        for student in sample_students:
            file.write(f"{student['name']},{student['roll']},{student['marks']}\n")
    print(f" '{FILENAME}' created and student records written.\n")

def read_file():
    try:
        with open(FILENAME, "r") as file:
            content = file.read()
            print(f"\n Contents of '{FILENAME}':\n")
            print(content)
    except FileNotFoundError:
        print(f" File '{FILENAME}' not found.\n")

def rename_file():
    try:
        os.rename(FILENAME, RENAMED_FILENAME)
        print(f" File renamed to '{RENAMED_FILENAME}'\n")
    except FileNotFoundError:
        print(f" File '{FILENAME}' not found. Rename failed.\n")

def create_and_move_to_directory():
    try:
        os.mkdir(DIRECTORY)
        print(f" Directory '{DIRECTORY}' created.")
    except FileExistsError:
        print(f" Directory '{DIRECTORY}' already exists.")

    try:
        shutil.move(RENAMED_FILENAME, os.path.join(DIRECTORY, RENAMED_FILENAME))
        print(f" File moved to '{DIRECTORY}/'")
    except FileNotFoundError:
        print(f" File '{RENAMED_FILENAME}' not found. Move failed.")

def list_directory_files():
    print(f"\n Files in '{DIRECTORY}':")
    try:
        files = os.listdir(DIRECTORY)
        if files:
            for f in files:
                print("", f)
        else:
            print("No files found in the directory.")
    except FileNotFoundError:
        print(f" Directory '{DIRECTORY}' not found.")

def delete_file():
    file_path = os.path.join(DIRECTORY, RENAMED_FILENAME)
    try:
        os.remove(file_path)
        print(f" File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print(f" File '{file_path}' not found.")
    except Exception as e:
        print(f" Error while deleting file: {e}")

def delete_directory():
    try:
        os.rmdir(DIRECTORY)
        print(f" Directory '{DIRECTORY}' deleted successfully.")
    except FileNotFoundError:
        print(f" Directory '{DIRECTORY}' not found.")
    except OSError:
        print(f" Directory '{DIRECTORY}' is not empty or cannot be deleted.")
    except Exception as e:
        print(f" Error while deleting directory: {e}")

# ==========================
# Main Menu Loop
# ==========================

def menu():
    while True:
        print("\n========= Student Record File System =========")
        print("1. Write to students.txt")
        print("2. Read from students.txt")
        print("3. Rename students.txt to student_records.txt")
        print("4. Create directory and move file into it")
        print("5. List files in SchoolData directory")
        print("6. Delete student_records.txt from directory")
        print("7. Delete SchoolData directory")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            write_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            rename_file()
        elif choice == "4":
            create_and_move_to_directory()
        elif choice == "5":
            list_directory_files()
        elif choice == "6":
            delete_file()
        elif choice == "7":
            delete_directory()
        elif choice == "0":
            print(" Exiting program. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")

# Run the program
menu()
