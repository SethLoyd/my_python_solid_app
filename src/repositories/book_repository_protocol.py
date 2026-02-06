from typing import Protocol
from src.domain.book import Book

class BookRepositoryProtocol(Protocol):
    def get_all_books(self) -> list[Book]:
        ...
    
    def add_book(self, book:Book) -> str:
        ...
    
    def find_book_by_name(self, query:str) -> list[Book]:
        ...
    
    def find_book_by_id(self, query:str) -> Book:
        ...

    def delete_book(self, query:str) -> str:
        ...

    def edit_book(self, book:Book) -> str:
        ...

    def check_in(self, book_id:str) -> str:
        ...
    
    def check_out(self, book_id:str) -> str:
        ...
    