# file_handling_assignment.py

def create_and_write_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is line 1.\n")
            file.write("The number is 42.\n")
            file.write("Python file handling is easy.\n")
        print("File created and written successfully.")
    except PermissionError:
        print("Permission denied: unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except FileNotFoundError:
        print("File not found: unable to read the file.")
    except PermissionError:
        print("Permission denied: unable to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Appending line 4.\n")
            file.write("Appending the number 99.\n")
            file.write("This is the appended line 6.\n")
        print("File appended successfully.")
    except PermissionError:
        print("Permission denied: unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    create_and_write_file()
    read_file()
    append_to_file()
    read_file()

if __name__ == "__main__":
    main()
