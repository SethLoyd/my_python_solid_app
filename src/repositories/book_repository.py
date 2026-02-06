import json
from src.domain.book import Book
from datetime import datetime
from src.repositories.book_repository_protocol import BookRepositoryProtocol

class BookRepository(BookRepositoryProtocol):
    def __init__(self, filepath: str = 'books.json'):
        self.filepath = filepath 

    def get_all_books(self) -> list[Book]:
        with open(self.filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Book.from_dict(item) for item in data]

    def add_book(self, book:Book) -> str:
        books = self.get_all_books()
        books.append(book)
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump([b.to_dict() for b in books], f, indent=2)
        return book.book_id
    
    def find_book_by_name(self, query:str) -> list[Book]:
        books = self.get_all_books()
        return [b for b in books if b.title == query]
    
    def find_book_by_id(self, query:str) -> list[Book]:
        books = self.get_all_books()
        #may cause issue with not found
        return [b for b in books if b.book_id == query]
    
    def delete_book(self, query:str) -> str:
        specific_book = self.find_book_by_id(query)
        if len(specific_book) == 0:
            return 'Book not found.'
        else:
            specific_book = specific_book[0]
            # delete book from file
            books = self.get_all_books()
            books.remove(specific_book)
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([b.to_dict() for b in books], f, indent=2)
            return 'Book deleted'

    def edit_book(self, book:Book) -> Book:
        specific_book = self.find_book_by_id(book.book_id)
        if len(specific_book) == 0:
            return 'Book not found'
        else:
            specific_book = specific_book[0]
            #update book
            if book.title != "":
                specific_book.title = book.title
            if book.author !="":
                specific_book.author = book.author
            if book.genre != "":
                specific_book.genre = book.genre
            if str(book.price_usd) != "":
                specific_book.price_usd = book.price_usd
        all_books = self.get_all_books()
        #replace by id then update json file
        all_books = [specific_book if b.book_id == specific_book.book_id else b for b in all_books]
        with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([b.to_dict() for b in all_books], f, indent=2)
        return specific_book
            
    def check_out(self, book_id:str) -> str:
        #find book by id returns list of books need to fix to access pieces
        specific_book = self.find_book_by_id(book_id)
        if len(specific_book) == 0:
            return 'Book not found'
        specific_book = specific_book[0]
        if not specific_book.available:
            return('Book is already checked out.')
        specific_book.available = False
        specific_book.last_checkout = str(datetime.now())
        all_books = self.get_all_books()
        #replace by id then update json file
        all_books = [specific_book if b.book_id == specific_book.book_id else b for b in all_books]
        with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([b.to_dict() for b in all_books], f, indent=2)
        return "Book Checked out"

    def check_in(self, book_id:str) -> str:
        specific_book = self.find_book_by_id(book_id)
        if len(specific_book) == 0:
            return 'Book not found'
        specific_book = specific_book[0]
        if specific_book.available:
            return ('Book is not checked out.')
        specific_book.available = True
        specific_book.last_checkin = str(datetime.now())
        all_books = self.get_all_books()
        #replace by id then update json file
        all_books = [specific_book if b.book_id == specific_book.book_id else b for b in all_books]
        with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([b.to_dict() for b in all_books], f, indent=2)
        return "Book Checked in"