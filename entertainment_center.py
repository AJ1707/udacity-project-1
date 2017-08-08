import media
import fresh_tomatoes

dunkrik = media.Movie("Dunkrik","An movie that tells about the events that happens on the hatrbour of dunkrik during the world war","https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg","https://www.youtube.com/watch?v=F-eMt3SrfFU")
focus = media.Movie("Focus","Movie based on bonkers and scammers","https://upload.wikimedia.org/wikipedia/en/thumb/b/bf/2015_Focus_film_poster.png/220px-2015_Focus_film_poster.png","https://www.youtube.com/watch?v=MxCRgtdAuBo")
turtle_video = media.Movie("Turtle demonstration","Drawing a circle with squares using python programming","https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Turtle_Graphics_Spiral.svg/220px-Turtle_Graphics_Spiral.svg.png","https://www.youtube.com/watch?v=cTpoj0I7pZs&feature=youtu.be")
despicable_me_3 = media.Movie("Despicable me 3","Movie about a retired villan who comes back to action","https://upload.wikimedia.org/wikipedia/en/9/91/Despicable_Me_3_%282017%29_Teaser_Poster.jpg","https://www.youtube.com/watch?v=6DBi41reeF0")
fury=media.Movie("Fury","Movie about a tank that stood alone in the enemy's line of defence","https://upload.wikimedia.org/wikipedia/en/thumb/1/17/Fury_2014_poster.jpg/220px-Fury_2014_poster.jpg","https://www.youtube.com/watch?v=-OGvZoIrXpg")
inception=media.Movie("Inception","Movie about a preson who does wonders using his dreams","https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg","https://www.youtube.com/watch?v=YoHD9XEInc0")


movies=[dunkrik,focus,turtle_video,despicable_me_3,fury,inception]

fresh_tomatoes.open_movies_page(movies)



