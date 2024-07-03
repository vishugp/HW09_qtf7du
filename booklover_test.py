import pandas as pd
from booklover import BookLover
import unittest

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # adding a book and testing if it is in `book_list`.
        user = BookLover("Vishwanath Guruvayur", "qtf7du@virginia.edu", "scifi")
        user.add_book("Kafka on the Shore",4)
        
        self.assertTrue("Kafka on the Shore" in list(user.book_list.book_name))
        

    def test_2_add_book(self):
        # adding the same book twice and testing if it's in `book_list` only once.
        user = BookLover("Vishwanath Guruvayur", "qtf7du@virginia.edu", "scifi")
        new_book = "Kafka on the Shore"
        user.add_book(new_book,4)
        user.add_book(new_book,3)
        
        
        ## Slicing the book_list Dataframe for the book and checking if there is only one row
        self.assertTrue(user.book_list[user.book_list.book_name==new_book].shape[0]==1)
        
                
    def test_3_has_read(self): 
        # passing a book in the list and test if the answer is `True`.
        user = BookLover("Vishwanath Guruvayur", "qtf7du@virginia.edu", "scifi")
        new_book = "Kafka on the Shore"
        user.add_book(new_book,4)
        
        self.assertTrue(user.has_read(new_book))
        
        
        
    def test_4_has_read(self): 
        # passing a book NOT in the list and use `assert False` to test the answer is `True`
        user = BookLover("Vishwanath Guruvayur", "qtf7du@virginia.edu", "scifi")
        new_book = "Kafka on the Shore"
        user.add_book(new_book,4)
        
        unlisted_book = "ABC"
        
        self.assertFalse(user.has_read(unlisted_book))
        
        
        
    def test_5_num_books_read(self): 
        # adding 3 books to the list, and test num_books matches expected.
        user = BookLover("Vishwanath Guruvayur", "qtf7du@virginia.edu", "scifi")
        user.add_book("Kafka on the Shore",4)
        user.add_book("Harry Potter - Chamber of Secrets", 3)
        user.add_book("The Martian", 5)
        
        expected_num = 3
        self.assertEqual(user.num_books_read(), expected_num)
        

    def test_6_fav_books(self):
        # adding some books with ratings to the list, making sure some of them have rating > 3. 
        user = BookLover("Vishwanath Guruvayur", "qtf7du@virginia.edu", "scifi")
        user.add_book("Kafka on the Shore",2)
        user.add_book("Harry Potter - Chamber of Secrets", 3)
        user.add_book("The Martian", 5)
        
        fav_bks = user.fav_books()
        
        # Tests check that the returned books have rating  > 3
        self.assertTrue((fav_bks.book_rating > 3).all())
        self.assertEqual(fav_bks[fav_bks.book_rating<=3].shape[0] , 0)
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
    
    
    