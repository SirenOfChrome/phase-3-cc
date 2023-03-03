import pytest
from movie import Movie
from viewer import Viewer
from review import Review

# Test Movie
def test_movie():
    # Initialize a Movie instance
    movie1 = Movie("The Shawshank Redemption")

    # Check that the title property is set correctly
    assert movie1.title == "The Shawshank Redemption"

    # Change the title of the movie
    movie1.title = "Shawshank Redemption"

    # Check that the title has been updated
    assert movie1.title == "Shawshank Redemption"

    # Add a review to the movie
    review1 = Review(Viewer("alice"), movie1, 4)
    movie1.reviews.append(review1)

    # Check that the average rating of the movie is correct
    assert movie1.average_rating() == 4

# Test Viewer
def test_viewer():
    # Initialize a Viewer instance
    viewer1 = Viewer("alice")

    # Check that the username property is set correctly
    assert viewer1.username == "alice"

    # Change the username of the viewer
    viewer1.username = "alice_smith"

    # Check that the username has been updated
    assert viewer1.username == "alice_smith"

    # Add a review by the viewer
    review2 = Review(viewer1, Movie("The Godfather"), 5)
    viewer1.reviews.append(review2)

    # Check that the viewer has reviewed the movie
    assert viewer1.reviewed_movie(Movie("The Godfather")) == True

# Test Review
def test_review():
    # Initialize a Review instance
    viewer2 = Viewer("bob")
    movie2 = Movie("The Godfather")
    review3 = Review(viewer2, movie2, 3)

    # Check that the rating property is set correctly
    assert review3.rating == 3

    # Check that the viewer property returns a copy of the viewer instance
    assert review3.viewer.username == "bob"

    # Check that the movie property returns a copy of the movie instance
    assert review3.movie.title == "The Godfather"

# Test Movie class
class TestMovie:
    def test_has_title(self):
        movie = Movie(title="Avatar: The Way of Water")
        assert movie.title == "Avatar: The Way of Water"

    def test_requires_nonzero_string_title(self):
        with pytest.raises(Exception):
            Movie(title=1)
        with pytest.raises(Exception):
            Movie(title="")

    def test_has_reviews(self):
        movie = Movie(title="Scarface")
        assert hasattr(movie, "reviews")
        assert isinstance(movie.reviews, list)

    def test_has_reviewers(self):
        movie = Movie(title="Rashomon")
        assert hasattr(movie, "reviewers")
        assert isinstance(movie.reviewers, list)

    def test_calculates_average_rating(self):
        movie = Movie(title="My Neighbor Totoro")
        movie.reviews = [1, 3, 2, 4, 5, 4, 2]
        assert movie.average_rating() == 3

    def test_shows_highest_rated(self):
        Movie.all = []
        movie_1 = Movie(title="Avatar: The Way of Water")
        movie_1.reviews = [1, 1, 1, 2, 3, 4, 4, 5]
        movie_2 = Movie(title="Scarface")
        movie_2.reviews = [1, 1, 1, 1, 1, 1]
        movie_3 =


#I built in testing outside of this environment as an additional layer to test the workflow 
# outside of this environment via replit.com or some similar tool....BEFORE I Realized that 
# "pytest" actually worked(the READ.ME stated it did'nt). After I realized it worked i utilized 
# the "pytest method to complete"... 3.3.23