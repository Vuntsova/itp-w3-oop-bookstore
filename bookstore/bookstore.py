from argparse import Namespace
def fixtures():
    fix = Namespace()
    
    
    
class Bookstore(object):
    def __init__(self,name):
        self.name=name
        self.books=[]
        
    def get_books(self):
        return self.books
    
    def add_book(self, book):
        self.books.append(book)
        
    def search_books(self, title=None, author=None):
        results=[]
        for book in self.books:
            if title and author and title.lower() not in book.title.lower() and author.lower() not in book.author.lower():
                continue
            if title and title.lower() not in book.title.lower():
                continue
            if author and author.lower() not in book.author.lower():
                continue
            results.append(book)
            
        return results
        


class Author(object):    
    def __init__(self, name, nationality):
        
        self.name = name
        self.nationality = nationality
        self.books = []
        
    def get_books(self):
        return self.books

    def add_book(self, book):
        self.books.append(book)
        
        
        


class Book(object):
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
        self.author.add_book(self)
        



borges = Author("Jorge Luis Borges", "AR")
ficciones = Book("Ficciones", author=borges)
aleph = Book("The Aleph", author=borges)
store = Bookstore("Rmotr's bookstore")
store.add_book(ficciones)
store.add_book(aleph)
# print(store.books)
print(store.get_books())
