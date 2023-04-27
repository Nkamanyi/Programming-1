

"""
Programming 1 Fall 2022
Name: Nkamanyi Martin <chatutie.nkamanyimartin@tuni.fi>
Student ID: K440302
"""

def main():
    file_name = input("Enter the name of the file: ")

    try:
        filee = open(file_name, mode="w")
    except OSError:
        print(f"Writing the file {file_name} was not successful.")
        return

    count = 0
    print("Enter rows of text. Quit by entering an empty row.")
    while True:
        text = input()
        if text == "":
            break
        count += 1
        print(count ,text, file=filee)

    filee.close()
    print(f"File {file_name} has been written.")

main()