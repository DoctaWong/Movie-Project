import webbrowser

class Movie():
    
    def __init__(self, title, genre, length, imdb_rating, poster_image, trailer_youtube, release_date):
        self.title = title
        self.genre = genre
        self.length = length
        self.imdb_rating = imdb_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date

    def show_trailer(self):
        '''opens a web browser with the link specified in trailer_url'''
    
        webbrowser.open(self.trailer_url)
