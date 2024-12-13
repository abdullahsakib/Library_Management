
from add import add_books
from view import book_view
from restore import restore_book
from delete import delete_books
from update import update_books
from lend import lend_book, load_lends, save_lends

all_books = []
lends=load_lends()

while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Book Update")
    print("4. Book Remove/Delete")

    all_books=restore_book()

    
    menu = input("Select any number: ")
    
    if menu == "0":
        print("Thanks for using Library Management System ")
        break
    elif menu == "1":
        all_books = add_books(all_books)
    elif menu == "2":
        # for b in all_books:
        #     print(b)
        book_view()
    elif menu == "3":
        update_books(all_books)
    elif menu == "4":
        delete_books(all_books)

    elif menu == "5":
        def lend_book(all_books,lends)
   

    else:
        print("Choose a valid number")

