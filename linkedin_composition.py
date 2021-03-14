class Book:
    def __init__(self, title, price, author = None):
        self.title = title
        self.price = price
        self.author = author
        self.chapters = []

    def add_chapter(self, chapter):
        self.chapters.append((chapter))
    def get_page_count(self):
        result = 0
        for ch in self.chapters:
            result += ch.pages
        return result

class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def __str__(self):
        return f"{self.fname} {self.lname}"

class Chapter:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

author_1 = Author('LEO', 'TOLSTOY')
chapter_1 = Chapter('Chapter 1', 125)
chapter_2 = Chapter('Chapter 2', 97)
chapter_3 = Chapter('Chapter 3', 143)
book_1 = Book('WAR AND PEACE', 39.5, author_1)
book_1.add_chapter(chapter_1)
book_1.add_chapter(chapter_2)
book_1.add_chapter(chapter_3)

print(book_1.title)
print(book_1.author.fname)
print(book_1.get_page_count())