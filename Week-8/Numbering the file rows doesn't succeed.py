
"""
Programming 1 Fall 2022
Name: Nkamanyi Martin <chatutie.nkamanyimartin@tuni.fi>
Student ID: K440302
"""

def main():
    file_name = input("Enter the name of the file: ")
    try:
        file = open(file_name, mode="r")
    except OSError:
        print(f"There was an error in reading the file.")
        return

    count = 0
    for file_line in file:
        file_line = file_line.rstrip()
        count += 1
        print(f"{count } {file_line}")

    file.close()

main()