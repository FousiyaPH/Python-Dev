class Library:
    
    def __init__(self,listOfBooks):
        self.availableBooks = listOfBooks
    
    def displayAvailableBooks(self):
        print()
        print("Available Books: ")
        for book in self.availableBooks:
            print(book)
        
    def lendBook(self,requestedBook):
        if requestedBook in self.availableBooks:
            print()
            print("You have now borrowed the book ")
            self.availableBooks.remove(requestedBook)
        else:
            print()
            print("Sorry!, the book is not available in the list.")

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have returned the book. Thank you! ")

class Customer:
    def requestBook(self):
        print()
        print("Enter the name of the book you would like to borrow: ")
        self.book = input()
        return self.book

    def returnBook(self):
        print()
        print("Enter the name of the book which you returning: ")
        self.book = input()
        return self.book


library = Library(['Days','You can win','The Spanish Girl'])
customer = Customer()
1
while True:
    print()
    print("Enter 1 to display the avilable books ")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book ")
    print("Enter 4 to exit")

    userChoice = int(input())
    if userChoice == 1:
        library.displayAvailableBooks()
    elif userChoice == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice == 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice == 4:
        quit()
        

