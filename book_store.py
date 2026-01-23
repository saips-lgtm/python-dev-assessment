class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        return 2025 - self.publication_year

    def get_summary(self):
        return "Title: " + self.title + ", Author: " + self.author + ", Published: " + str(self.publication_year)


# Example usage
book1 = Book("Python Basics", "John Smith", "12345", 2018)
book2 = Book("Learning OOP", "Jane Doe", "67890", 2020)

print(book1.title)
print(book1.author)
print(book1.get_age())
print(book1.get_summary())

print()

print(book2.title)
print(book2.author)
print(book2.get_age())
print(book2.get_summary())
