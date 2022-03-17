#Array with library "movies"
current_movies = {
                  'The Grinch':'11:00am',
                  'Rudolph':'1:pm',
                  'The batman':'4pm',
                  'Titanic remaster':'1am'
                  }

#Showing a list with movies
print("Were showing the following movies:")
#loop takes all the values inside of the array current_movies
for key in current_movies:
    print(key)
#Asking to user to choose one of the movies
movie = input('What movie would you like the showtime for?\n')
#Take the value inside of the library and check if it exists
showtime = current_movies.get(movie)
#If the value doesn't exists show the fisrt message."Requested showtime is not in the movies list!"
if showtime == None:
    print("Requested showtime is not in the movies list!")
#If the value exists it will show the message "movie, 'is playing at', showtime" concatenating the index movie with his value.
else:
    print(movie, 'is playing at', showtime)
