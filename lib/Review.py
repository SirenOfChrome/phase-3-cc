class Review:
    def __init__(self, viewer, movie, rating):
        if type(rating) != int or rating < 1 or rating > 5:
            raise ValueError("Rating must be an integer between 1 and 5")
        from viewer import Viewer
        if not isinstance(viewer, Viewer):
            raise TypeError("Viewer must be a Viewer instance")
        from movie import Movie
        if not isinstance(movie, Movie):
            raise TypeError("Movie must be a Movie instance")
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
