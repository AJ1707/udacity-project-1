# movie-trailer

Project report : Movie trailer

Programming language :python,html

Description: A project using python that plays a list of youtube trailes for a specified no of movies.To be particular 6 movies

Number of files: 4

	1.media.py
	2.fresh_tomatoes.py
	3.entertainment_center.py
	4.fresh_tomatoes.html

media.py
	This file contains a imported function webbrowser that allows to play the youtube players.

It also contains a class Movie that contains arguments which allows various elements of the movies to be viewed
It also contains the method show_trailer() that uses the imported webbrowser to play the youtube trailer

fresh_tomatoes.py
	This contains an inbuilt html file that gets launched when this file gets executed.It mainly organises the information from 
the two python file (media.py,entertainment_center.py) to be organized and to be displayed as complete website.


entertainment_center.py
	This is where the all the list of all the movies and its details like the movie information ,picture, youtube trailer gets stored .
The list of the entire movies is stored undfer a single list movies for easy usage.It is form here where the method to launch the website 
gets called.

fresh_tomatoes.html
	This html page gets automatically executed when the fresh_tomatoes.py gets executed. This is the final output of the project where the 
poster images of the movies gets displayed and by clicking the poster image the youtube trailer of the movie gets displayed.


#How to launch the project

1)Run the entertainment_center.py python file
2)Select the movie's trailer you have to play
3)This views the youtube trailer of the selected poster image

