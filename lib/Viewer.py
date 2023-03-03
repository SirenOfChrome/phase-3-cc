class Viewer:
    all = []

    def __init__(self, username):
        if not isinstance(username, str) or len(username) < 6 or len(username) > 16:
            raise ValueError("Username must be a string between 6 and 16 characters")
        for viewer in self.__class__.all:
            if viewer.username == username:
                raise ValueError("Username must be unique")
        self.username = username
        self.reviews = []
        self.reviewed_movies = []
        self.__class__.all.append(self)

    def reviewed_movie(self, movie):
        return movie in self.reviewed_movies

    def rate_movie(self, movie, rating):
        from review import Review
        review = next((review for review in self.reviews if review.movie == movie), None)
        if review:
            review.rating = rating
        else:
            review = Review(self, movie, rating)
            self.reviews.append(review)
        if movie not in self.reviewed_movies:
            self.reviewed_movies.append(movie)
