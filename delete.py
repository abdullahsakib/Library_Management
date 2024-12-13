

from save import save_book

def delete_books(all_books):
    search_book = input("Enter Book Title to Delete: ")
    for book in all_books:
        if book["title"] == search_book:
            print(f"{book['title']} Deleted Successfully")
            all_books.remove(book)
            save_book(all_books)
           
            return all_books
    
    print("Book Not Found")