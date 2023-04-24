"""
Programming 1 Fall 2022
Name: Nkamanyi Martin <chatutie.nkamanyimartin@tuni.fi>
Student ID: K440302
"""

def main():
    bored = True
    while bored:
        question = input("Bored? (y/n) ")
        if question == "y":
            bored = False
            print("Well, let's stop this, then.")

main()