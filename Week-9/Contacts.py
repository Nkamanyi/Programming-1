
"""
Programming 1 Fall 2022
Name: Nkamanyi Martin <chatutie.nkamanyimartin@tuni.fi>
Student ID: K440302
"""

def read_file(filename):
    """
    From the CSV file, create a dict from each line of the file and store them in a dict

    :param filename: the given CSV file
    :return: dict, the created dict containing other dictionaries
    """

    contacts = {}

    file = open(filename, mode="r")

    file.readline()
    for line in file:
        key, name, phone, email, skype = line.rstrip().split(";")
        contacts[key] = {}
        contacts[key]['name'] = name
        contacts[key]['phone'] = phone
        contacts[key]['email'] = email
        contacts[key]['skype'] = skype

    file.close()
    return contacts




def main():
    info = read_file("contacts.csv")
    print(info["Mike"]["phone"])
    print(info["Tom"]["email"])
    print(info["Archie"]["name"])


main()