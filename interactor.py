import csv

def check_fileheader():
    with open("movies_data.csv", newline="") as verify:
        content = verify.read()
    d = len(content)
    if d == 0:
        with open("movies_data.csv", "w", newline="") as file_content:
            file_header = ["movie_name", "released_year", "director", "read_status"]
            writer = csv.DictWriter(file_content, file_header)
            writer.writeheader()


def clear_filecontent():
    d = ""
    with open("movies_data.csv", "w", newline="") as clear:
        clear.write(d)


def file_appenddata(data):
    check_fileheader()
    with open("movies_data.csv", "a", newline="") as file_content:
        file_header = ["movie_name", "released_year", "director", "read_status"]
        writer = csv.DictWriter(file_content, file_header)
        writer.writerow(data)


def read_filecontent():
    file_read = open("movies_data.csv", "r")
    file_content = [line.strip() for line in file_read.readlines()]
    file_read.close()
    linenumber = 0
    headers = []
    datacontent = []
    dictionary_form = []
    for data in file_content:
        if linenumber == 0:
            data = data.split(",")
            for pcontent in data:
                headers.append(pcontent)
            linenumber = linenumber + 1
        else:
            data = data.split(",")
            for pcontent in data:
                datacontent.append(pcontent)
            dictionary_form.append(dict(zip(headers, datacontent)))
            datacontent.clear()
    return dictionary_form


def add_movies():
    name = input("Enter the movie name:- ")
    release_date = input("enter the year of released:- ")
    director = input("Enter the the director")
    book_read = input("enter yes if book is read else enter no :").strip().lower()
    data = {"movie_name": name, "released_year": release_date, "director": director, "read_status": book_read}
    file_appenddata(data)


def search_movies(movie_name):
    search_field = movie_name
    with open("movies_data.csv", "r", newline="") as file_content:
        reader = csv.DictReader(file_content)
        for data in reader:
            if data["movie_name"] == search_field:
                print(data)
                break
        else:
            print(f"the movie you are looking is not available")
            d = input("if do you want to enter this data enter 'a' else enter any value").strip().lower()
            if d == "a":
                add_movies()


def display_content():
    dictionary_content = read_filecontent()
    print(f"The content in the file is as follows")
    for data in dictionary_content:
        print(f"The name of the movie or book  is '{data['movie_name']}'"
              f" by '{data['director']}' released in the year '{data['released_year']}'")


def change_readstatus(movie_name):
    dictionary_form = read_filecontent()
    search_field = movie_name
    for data in dictionary_form:
        if data["movie_name"] == search_field:
            read_status_update = input("Can you please update the read status as 'yes' or 'no' :- ")
            if data["read_status"] != read_status_update:
                data["read_status"] = read_status_update
            ndata = {"movie_name": data["movie_name"],
                     "released_year": data["released_year"],
                     "director": data["director"],
                     "read_status": data["read_status"]}
            file_appenddata(ndata)
            delete_filecontent(search_field)
            print("The request is processed successfully")
            break
    else:
        print(f"we cannot see any movie or book in name of {search_field} "
              f"please re-verify and select the option to process relevantly")


def delete_filecontent(movie_name):
    dictionary_form = read_filecontent()
    search_field = movie_name
    for content in dictionary_form:
        if content["movie_name"] == search_field:
            content.clear()
            clear_filecontent()
            check_fileheader()
            for data in dictionary_form:
                n = len(data)
                if n != 0:
                    ndata = {"movie_name": data["movie_name"], "released_year": data["released_year"],
                             "director": data["director"], "read_status": data["read_status"]}
                    file_appenddata(ndata)
            break
    else:
        print(f"we cannot see any movie or book in name of {search_field} "
              f"please re-verify and select the option to reprocess relevantly")
