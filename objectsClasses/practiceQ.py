class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []
    def display(self):
        if self.no_of_books == 0:
            print('\nNo books available in the library')
        else:
            print('\nBooks available in the library:-')
            for i in self.books:
                print(i)
                
    def add_book(self,book):
        self.books.append(book)
        self.no_of_books += 1
        print(f'\n{book} book added to the library.')
        
    def get_no_of_books(self):
        print(f'\nTotal books in library are :{self.no_of_books}')

             
def main():
    library1 = Library()
    x= 0
    print(x == 0)
    while True:
        print("\n1. Display all books")
        print("2. Add a book")
        print("3. Get the number of books")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library1.display()
        elif choice == "2":
            book = input("Enter the name of the book: ")
            library1.add_book(book)
        elif choice == "3":
            library1.get_no_of_books()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
