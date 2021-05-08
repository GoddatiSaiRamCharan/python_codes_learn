import interactor


def prompt():
    menu_prompt = input(
        "Select a option from below options available "
        "\n'a' to add book to the reading list "
        "\n's' to search the books in the reading list "
        "\n'd' to delete from file"
        "\n'c' to change the book status "
        "\n'dis' to display the complete content in the file "
        "\n'e' to exist the reading list").strip().lower()
    return menu_prompt


def addmovies():
    interactor.add_movies()


def searchmovies(moviename):
    interactor.search_movies(moviename)


def deletefilecontent(moviename):
    interactor.delete_filecontent(moviename)


def changereadstatus(moviename):
    interactor.change_readstatus(moviename)


def displaycontent():
    interactor.display_content()


menu_prompt = prompt()
while menu_prompt != 'e':

    if menu_prompt == "a":
        addmovies()

    elif menu_prompt == "e":
        break

    elif menu_prompt == "s":
        movie_name = input("enter the movie to be searched")
        searchmovies(movie_name)

    elif menu_prompt == "d":
        movie_name = input("enter the movie to be deleted")
        deletefilecontent(movie_name)

    elif menu_prompt == "c":
        movie_name = input("enter the movie to be change the read status")
        changereadstatus(movie_name)

    elif menu_prompt == "dis":
        displaycontent()

    else:
        print(f"You have selected invalid option")

    menu_prompt = prompt()
