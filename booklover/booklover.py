import pandas as pd
class BookLover:
    """
    PURPOSE:    Maintain a Database of the books read by a user 
                in a DataFrame and methods to retrieve top rated books
    """
    
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame(columns = ['book_name','book_rating'])):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
                 
                 
    def add_book(self,book_name, book_rating):
        new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
            
        if book_name not in list(self.book_list.book_name):
            self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)
        else:
            print(f"Book - {book_name} already in list")
                                       
    def has_read(self, book_name):              
        return book_name in list(self.book_list.book_name)
                                       
    def num_books_read(self):
        return self.book_list.shape[0]
                                       
    def fav_books(self):
        fav_books = self.book_list[self.book_list.book_rating > 3]
        return fav_books
                                       
    
                 
        
if __name__ == '__main__':
    
    user = BookLover("Vishwanath Guruvayur", "qtf7du@virginia.edu", "scifi")
    user.add_book("Kafka on the Shore", 4)
    fav = user.fav_books()
    print(fav)
            
        
    
        
        