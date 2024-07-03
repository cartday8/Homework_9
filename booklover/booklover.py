import pandas as pd

class BookLover:
    
    
    
    def __init__(self, name, email, fav_genre, num_books = None, book_list = None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        
    def add_book(self, book_name, rating):
        #Making sure book_name is string, rating is int from 1 to 5, and if the bookname is in the booklist
        if not isinstance(book_name, str):
            raise ValueError("Please put in a string for the book name")
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise ValueError("Please put in an integer from 1 to 5")               
        if self.book_list['book_name'].isin([book_name]).any():
            raise ValueError("This book is already in your list")    
            
        self.book_name = book_name
        self.rating = int(rating)
        
        #Adds bookname and rating to dataframe
        new_book = pd.DataFrame({'book_name': [self.book_name], 'book_rating': [self.rating]})
        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        
    def has_read(self, book_name):
        #making sure bookname is a string
        if type(book_name) != str:
            raise ValueError("Please put in a string for the book name")
            
        #Checking to see if bookname is in the booklist and then returning true or false
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
        
    def num_books_read(self):
        return self.book_list.shape[0]
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating']>3]