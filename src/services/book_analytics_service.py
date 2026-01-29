import numpy as np
import pandas as pd
from src.domain.book import Book

#Ground rules for numpy:
#1. keep numpy in the service layer ONLY
#   if you see numpy imports anywhere else this is a design smell
#2. notic ehow methods take in books and return normal datatypes NOT ndarrays

class BookAnalyticsService:

    def average_price(self, books:list[Book]) -> float:
        prices = np.array([b.price_usd for b in books], dtype=float)
        return float(prices.mean())
    
    def top_rated(self, books:list[Book], min_ratings: int = 1000, limit: int = 10) -> list[Book]:
        ratings = np.array([b.average_rating for b in books])
        counts = np.array([b.ratings_count for b in books])
        
        #what we have now:
        #books -> books objects
        #ratings -> numbers for all books
        #counts -> numbers for all books
        #filtered books contains all books that have at least 1000 ratings
        mask = counts >= min_ratings
        filteredBooks = np.array(books)[mask]
        #now scores is only the ratings for the filtered books. i.e. over 1000 ratings
        scores = ratings[mask]
        sorted_idx = np.argsort(scores)[::-1]
        return filteredBooks[sorted_idx].tolist()[:limit]

    #value score = rating * log(ratings_count) / price
    def value_scores(self, books:list[Book]) -> dict[str, float]:
        ratings = np.array([b.average_rating for b in books])
        counts = np.array([b.ratings_count for b in books])
        prices = np.array([b.price_usd for b in books])

        scores = (ratings * np.log1p(counts)) / prices

        return {
            #zip() iterates both lists in parallel
            #pairing each book with its corresponding score
            #zip() will stop automatically if one list is shorter
            #if the same key appears more than once later entries overwrite earlier ones
            book.book_id: float(score) #output of dict comprehension
            for book, score in zip(books, scores)
        }
    
    def median_price_by_genre(self, books:list[Book]) ->dict[str, float]:
        #make list of books a dict to turn into a dataframe
        #manipulate with pandas
        df = pd.DataFrame(books)
        median = df.groupby('genre')['price_usd'].median().round(2)
        return(median)

    def most_popular_genre(self, books:list[Book]) ->dict[str, float]:
        #doing this by highest sold
        df = pd.DataFrame(books)
        most_popular = df.groupby('genre')['sales_millions'].sum().round(2).idxmax()
        return most_popular