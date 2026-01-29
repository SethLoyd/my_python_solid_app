import pytest 
import src.services.book_service as book_service
from tests.mocks.mock_book_repository import MockBookRepo

def test_get_all_books_positive():
    # AAA - arrange, act, assert
    repo = MockBookRepo()
    svc = book_service.BookService(repo)
    books = svc.get_all_books()
    assert len(books) == 1

def test_find_book_by_name_negative():
    name = 3
    repo = MockBookRepo()
    svc = book_service.BookService(repo)

    with pytest.raises(TypeError) as e:
        book = svc.find_book_by_name(name)
    assert str(e.value) == 'Expected a str, got something else.'

def test_edit_book_negative():
    #Fix this maybe make a pos test instead
    id = 3
    repo = MockBookRepo()
    svc = book_service.BookService(repo)
    with pytest.raises(TypeError) as e:
        book = svc.edit_book(id)
    assert str(e.value) == 'Expected a book, got something else.'


def test_delete_book_negative():
    #Finish this
    repo = MockBookRepo()
    svc = book_service.BookService(repo)
    id = 1
    books = svc.get_all_books()
    with pytest.raises(TypeError) as e:
        book = svc.delete_book(id)
    assert str(e.value) == 'Expected a str, got something else.'
