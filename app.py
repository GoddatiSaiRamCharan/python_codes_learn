movies=[]
def usermanual():
  userin=input("Enter the operation to perform 'a' to add to movies or s to search and d to display the movies list:- ")
  return userin

def addmovies():
  name=input("enter movie name :- ")
  director=input("enter movie director :- ")
  year=input("enter year of release :- ")
  movies.append({'name':name , 'director' : director , 'year':year})

def searchmovies():
  searchv=input("enter the value to search in movies data:-")
  for movie in movies:
    if(searchv==movie['name'] ):
      print(movie)
      c=1
    elif(searchv==movie['director'] ):
      print(movie)
      c=1
    elif(searchv==movie['year']):
      print(movie)
      c=1
  if(c!=1):
    print("No movies found with the search you entered")


def displaymovies():
  for details in movies:
    print(details)

display="True"
while display!='f':
  requested=usermanual()
  if (requested == 'a'):
    addmovies()
  elif(requested =='s'):
    searchmovies()
  elif(requested == 'd'):
    displaymovies()
  else:
    print("invalid user input")
  display=input("if you want to continue enter 'true' else enter as 'False':-")


