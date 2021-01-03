class Book:
    book_type = ['paper back', 'hardcover', 'e book']
    def __init__(self, title, author, pages, price, booktype):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = 'This is a secret message'
        if not booktype in Book.book_type:
            raise ValueError(f"{booktype} is not a valid type")
        else:
            self.book_type = booktype
    def set_new_title(self, new_title):
        self.title = new_title
    def get_price(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    def set_discount(self, amount):
        self._discount = amount
    @classmethod
    def get_book_types(cls):
        return cls.book_type

class Newspaper:
    def __init__(self, name):
        self.name = name
print(f"Book Types are {Book.get_book_types()}")
book_1 = Book('War And Peace', 'Leo Tolstoy', 1225, 39.95, 'paper back')
book_2 = Book('The Catcher In The Ray', 'JD Salinger', 234, 29.95, 'e book')

news_1 = Newspaper('The Washington Post')
news_2 = Newspaper('WSJ')


