class Book():

    def __init__(self, title, author, rating, num_ratings):
        self.title = title
        self.author = author
        self.rating = rating # bookFinder.getRating()
        self.num_ratings = num_ratings
        # self.cover = cover # bookFinder.getBookCover(title)

    def __lt__(self, other):
        return self.rating < other.rating

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_rating(self):
        return self.rating

    def get_num_ratings(self):
        return self.num_ratings

    def print_book(self):
        print(self.title + " by " + self.author)