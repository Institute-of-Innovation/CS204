import random
library_books = []

def add_book(title, author):
    book_id = random.randint(1000, 9999)
    book = {"id": book_id, "title": title, "author": author, "available": True}
    library_books.append(book)
    print("Book '" + title + "' added with ID " + str(book_id) + ".")

def view_books():
    if not library_books:
        print("No books in the library.")
        return

    print("\n--- Available Books ---")
    for book in library_books:
        status = "Available" if book["available"] else "Not Available"
        print(str(book["id"]) + " - " + book["title"] + " by " + book["author"] + " [" + status + "]")

def borrow_book(book_id):
    for book in library_books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                print("You have borrowed '" + book["title"] + "'.")
            else:
                print("Sorry, this book is currently not available.")
            return
    print("Book ID not found.")

def return_book(book_id):
    for book in library_books:
        if book["id"] == book_id:
            book["available"] = True
            print("Thank you for returning '" + book["title"] + "'.")
            return
    print("Book ID not found.")

while True:
    print("\nLibrary Management Menu")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        add_book(title, author)
    elif choice == '2':
        view_books()
    elif choice == '3':
        try:
            book_id = int(input("Enter Book ID to borrow: "))
            borrow_book(book_id)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == '4':
        try:
            book_id = int(input("Enter Book ID to return: "))
            return_book(book_id)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == '5':
        print("Exiting Library Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
