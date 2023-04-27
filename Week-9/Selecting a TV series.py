
"""
Programming 1 Fall 2022
Name: Nkamanyi Martin <chatutie.nkamanyimartin@tuni.fi>
Student ID: K440302
"""

def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    TODO: comment the parameter and the return value.
    :param filename: file, the file with the series data
    :return: dic, the dictionary of tv series alongside their names and genres
    """

    # TODO initialize a new data structure
    genre_data = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            # TODO add the name and genres data to the data structure
            genre_data[name] = genres

        file.close()
        return genre_data   # TODO return the data structure

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    file_name = input("Enter the name of the file: ")

    genre_data = read_file(file_name)

    # TODO print the genres
    genres = []
    available_genres = ""
    for genre in genre_data.values():
        for k in genre:
            if k not in genres:
                genres.append(k)
        available_genres = ", ".join(sorted(genres))

    print("Available genres are:", available_genres)

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        # TODO print the series belonging to a genre.
        for s in sorted(genre_data.keys()):
            if genre in genre_data[s]:
                print(s)


if __name__ == "__main__":
    main()