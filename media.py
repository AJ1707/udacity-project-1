"""
module displaying movie objects,attributes and instances
"""
import webbrowser


class Movie():
    """
    class object store movie related information
    """
    
    """
    Initialize instance of class Movie
    containing all the elements of the movie trailer
    """

    def __init__(self,movie_title,movie_storyline,poster_image_url,trailer_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image_url
        self.trailer_youtube_url=trailer_youtube
    def show_trailer(self):
        """
        initialize the instance to open the youtube url
        """
        webbrowser.open(self.trailer_youtube_url)

