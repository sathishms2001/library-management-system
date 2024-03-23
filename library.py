class Library:
    def show_books(self, books):
        for book in books:
            print(book)

    def get_book(self, books, title):
        if title in books:
            print(f"""
Yes! The book is available. You want {title} book
1. Yes
2. No
            """)
            choice = input("Enter your Choice : ")
            if choice == '1':
                print(f"You have got {title} from library.")
                books.remove(title)
            else:
                print("Thank you for visiting us. Come Again")

        else:
            print("Sorry! This book is not available.")

    def submit_book(self, books, title, Original_books):
        if title in Original_books and title in books:
            print("This book is already in the library collection.")

        elif title in Original_books and title not in books:
            books.append(title)
            print(f'{title} has been added to the library')

        else:
           print("Sorry this book is authorized") 


books = ["HTML", "CSS", "JavaScript", "Python", "Ruby", "PHP", "Java"]
Original_books = ["HTML", "CSS", "JavaScript", "Python", "Ruby", "PHP", "Java"]

obj = Library()

while True:
    print("""
1. Show all Books
2. Get a Book
3. Submit a Book
4. Exit
    """)

    user_input = input("Enter your choice : ")
    try:
        user_input=int(user_input)
        if user_input == 1:
            obj.show_books(books)
        elif user_input == 2:
            title = input("Enter the title of the book you want to search : ")
            obj.get_book(books, title)
        elif user_input == 3:
            title = input("Enter the title of the book you want to submit : ")
            obj.submit_book(books, title, Original_books)
        elif user_input == 4:
            print("Thank you for using the library!")
            break
    except:
        print("Invalid Input")
