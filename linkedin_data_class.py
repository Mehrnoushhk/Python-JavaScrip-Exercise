from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(10, 40))

@dataclass
class Book:
    
    title : str = 'No Title'
    author : str = 'No Author'
    pages : int = field(default= 100)
    price: float = field(default_factory=price_func)
    __secret = 'This is a secret'
    def __post_init__(self):
        self.description = f'The book {self.title} is {self.pages} pages'
    def book_info(self):
        return f'{self.title} is written by {self.author}'

# book_1 = Book('War And Peace', 'Leo Tolstoy', 1225, 39.95)
# book_2 = Book('The Catcher In The Ray', 'JD Salinger', 234, 29.95)
# book_3 = Book('War And Peace', 'Leo Tolstoy', 1225, 39.95)
book_4 = Book()


# print(book_1.title)
# print(book_2)
# print(book_1 == book_3)
# print(book_1.book_info())
# print(book_2.description)
print(book_4)
print(book_4._Book__secret)