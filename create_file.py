# file_handling_assignment.py

def create_file():
    """Create a new text file and write some initial content."""
    try:
        with open('my_file.txt', 'w') as file:
            file.write("Hello, World!\n")
            file.write("This is line number 2.\n")
            file.write("The answer to life is 42.\n")
        print("File created and initial content written.")
    except (PermissionError, IOError) as e:
        print(f"An error occurred while creating the file: {e}")
    finally:
        print("create_file function completed.")

def read_file():
    """Read the contents of the text file and display them."""
    try:
        with open('my_file.txt', 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' was not found.")
    except PermissionError:
        print("Error: Permission denied while trying to read the file.")
    finally:
        print("read_file function completed.")

def append_to_file():
    """Append additional content to the text file."""
    try:
        with open('my_file.txt', 'a') as file:
            file.write("This is an appended line 1.\n")
            file.write("Another line added to the file.\n")
            file.write("Final line added, number 3.\n")
        print("Additional lines appended to the file.")
    except (PermissionError, IOError) as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        print("append_to_file function completed.")

def main():
    create_file()       # Create the file and write initial content
    read_file()         # Read the contents of the file
    append_to_file()    # Append additional content

if __name__ == "__main__":
    main()
