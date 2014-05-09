class Library(object):
  def __init__(self, my_library):   
    self.my_library = my_library 
    self.library_shelves = []
  
  def create_new_shelf(self, new_shelf):
    self.library_shelves.append(new_shelf)
   
  def report(self):
    return "The current library, %r, contains the following sections: %r" % (self.my_library, ",".join(self.library_shelves),)
  

class Shelf(object):  
    def __init__(self, shelf_type):
        self.shelf_type = shelf_type
        self.books_on_this_shelf = []
        
    def put_book_on_shelf(self, this_book):
        self.books_on_this_shelf.append(this_book)
    
    def pull_book_off_shelf(self, this_book):
        self.books_on_this_shelf.remove(this_book)
  
    def report(self):
        return "The shelf, %r, currently contains the following books: %r" % (self.shelf_type, ",".join(self.books_on_this_shelf),)

class Book(object): 
    def __init__(self, title, author, shelf_type):
        self.title = title
        self.author = author
        self.shelf_type = shelf_type

    def enshelf(self, shelf_type):
        shelf_type.put_book_on_shelf(self.title)
  
    def unshelf(self, shelf_type):
        shelf_type.pull_book_off_shelf(self.title)
        
    def report(self):
        return "The title of this book is %s, the author is %s, and it is currently on the %s shelf." % (self.title, self.author, self.shelf_type)
         
my_library = raw_input("Hi! What would you like to name your library?")    
my_library = Library(my_library)   

print "Thanks! " + my_library.report()

new_shelf = raw_input("Let's add a shelf to our library. Please enter a genre (e.g. 'fiction' or 'reference materials').")

my_library.create_new_shelf(new_shelf)
new_shelf = Shelf(new_shelf)

print "Thanks! " + my_library.report()

new_book_title = raw_input("Now let's add a book to the shelf. Please enter the title of a book.")

new_book_author = raw_input("Thanks! Now please enter the author's name.")

latest_addition = Book(new_book_title, new_book_author, new_shelf)

latest_addition.enshelf(new_shelf)

print new_shelf.report()

latest_addition.unshelf(new_shelf)

print "Ok, let's move %r to a different shelf." % (new_book_title,)

new_shelf = raw_input("First we need to add an additional shelf to our library. Please enter another genre (e.g. 'fiction' or 'reference materials').")

my_library.create_new_shelf(new_shelf)
new_shelf = Shelf(new_shelf)

print "Thanks! " + my_library.report()

latest_addition.enshelf(new_shelf)

print new_shelf.report()

