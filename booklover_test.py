import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        self.person = BookLover("Carter", "cart@gmail.com", "scifi")
        self.person.add_book("Dune", 5)
        self.actual = "Dune"
        self.test = self.person.book_list.iloc[0,0]
        self.assertEqual(self.actual,self.test,"It did not add the book")
        

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        self.person = BookLover("Carter", "cart@gmail.com", "scifi")
        self.person.add_book("Dune", 5)   
        
        try:
            self.person.add_book("Dune", 4)
            exception_occurred = False
        except ValueError:
            exception_occurred = True
            
        self.actual = 1
        self.test = self.person.book_list.shape[0]
        self.assertEqual(self.actual,self.test,"It added the book twice")
                
            
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        self.person = BookLover("Carter", "cart@gmail.com", "scifi")
        self.person.add_book("Dune", 5)
        self.test = self.person.has_read("Dune")
        self.assertTrue(self.test,"It does not show the book as read")
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        self.person = BookLover("Carter", "cart@gmail.com", "scifi")
        self.person.add_book("Dune", 5)
        self.test = self.person.has_read("Foundation")
        self.assertFalse(self.test,"It does show the book as read")
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        self.person = BookLover("Carter", "cart@gmail.com", "scifi")
        self.person.add_book("Dune", 5)
        self.person.add_book("Foundation", 4)
        self.person.add_book("Project Hail Mary", 5)
        self.actual = 3
        self.test = self.person.num_books_read()
        self.assertEqual(self.actual,self.test,"It did not count the correct amount of books read")

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        self.person = BookLover("Carter", "cart@gmail.com", "scifi")
        self.person.add_book("Dune", 5)
        self.person.add_book("Foundation", 3)
        self.person.add_book("Project Hail Mary", 5)
        self.person.add_book("Lord of the Rings", 1)
        self.fav_books = self.person.fav_books()
        self.assertTrue(all(self.fav_books['book_rating'] > 3), "It added books with a book rating <=3")
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)