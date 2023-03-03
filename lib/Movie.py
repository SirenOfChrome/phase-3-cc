class Movie:
    all = []

    def __init__(self, title):
        if type(title) != str or len(title) < 1:
            raise ValueError("Title must be a string of >0 characters")
        self.title = title
        self.reviews = []
        self.reviewers = []
        self.__class__.all.append(self)

    def average_rating(self):
        return sum(review for review in self.reviews) / len(self.reviews) if self.reviews else 0

    @classmethod
    def highest_rated(cls):
        return max(cls.all, key=lambda movie: movie.average_rating() if movie.reviews else 0)
