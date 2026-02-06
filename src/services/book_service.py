from src.services import book_generator_bad_data_service
from src.repositories.book_repository_protocol import BookRepositoryProtocol
from src.domain.book import Book

class BookService:
    def __init__(self, repo: BookRepositoryProtocol):
        self.repo = repo
    
    def get_all_books(self) -> list[Book]:
        return self.repo.get_all_books()
    
    def add_book(self, book:Book) -> str:
        return self.repo.add_book(book)
    
    def find_book_by_name(self, query:str) -> list[Book]:
        if not isinstance(query, str):
            raise TypeError('Expected a str, got something else.')
        return self.repo.find_book_by_name(query)
    
    def find_book_by_id(self, query:str) -> Book:
        if not isinstance(query, str):
            raise TypeError('Expected a str, got something else')
        return self.repo.find_book_by_id(query)
    
    def delete_book(self, query:str) -> str:
        if not isinstance(query, str):
            raise TypeError('Expected a str, got something else.')
        return self.repo.delete_book(query)
    
    def edit_book(self, book:Book) -> str:
        if not isinstance(book, Book):
            raise TypeError('Expected a book, got something else.')
        return self.repo.edit_book(book)
    
    def check_in_book(self, book_id:str) -> str:
        return self.repo.check_in(book_id)
    
    def check_out_book(self, book_id:str) -> str:
        return self.repo.check_out(book_id)