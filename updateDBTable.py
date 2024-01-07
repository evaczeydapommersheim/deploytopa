from movieDAO import movieDAO
# Create DB Table movie
#result = movieDAO.createDbTable()
 
# Create movies in the movie table
dbRows = [
    ("Drama", "The Shawshank Redemption", "Frank Darabont", "Morgan Freeman", 1994),
    ("Drama, Mystery, Thriller", "The Sixth Sense", "M. Night Shyamalan", "Bruce Willis", 1999),
    ("Drama, Romance", "Forrest Gump", "Robert Zemeckis", "Tom Hanks",1994),
    ("Drama, Romance, Comedy", "The Terminal", "Steven Spielberg", "Tom Hanks", 2004),
    ("Drama, Romance, Comedy", "As Good as it gets", "James L. Brooks", "Jack Nicholson", 1997),
    ("Drama, Romance, Comedy", "The Terminal", "Steven Spielberg", "Tom Hanks", 2004),
    ("Action", "De Ja Vu", "Tony Scott", "Denzel Washington", 2006)
]

for dbRow in dbRows:
  movieDAO.create(dbRow)

# create movie
#newMovie = movieDAO.create(("Drama, Romance", "Good Will Hunting", "Gus Van Sant", "Robin Williams", 1997))

# TESTING CODE FROM movieDAO.py file

# Find by id
#result = movieDAO.findByID(newMovie)
#print ("test create and find by id")
#
#print (result)
# Find by year
#print ('Testing Find by year')
#results = movieDAO.findByYear(1994)
#print(results)

# Update
#movieDAO.update(("Crime, Drama, Mystery", "Seven", "David Fincher", "Brad Pitt, Morgan Freeman", 1995, 8))
#result = movieDAO.findByID(8)
#print("test update")
#print (result)

# Get all
#print("test get all")
#allMovies = movieDAO.getAll()
#for movie in allMovies:
#  print(movie)


# Delete movie id = 7 in the movie table
#movieDAO.delete(10)



