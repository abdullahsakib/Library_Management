from datetime import datetime
from save import save_book

def update_books(all_books):
    search_book = input("Enter Book Title to Update: ")
    for book in all_books:
        if book["title"] == search_book:
            title = input("Enter Book Title: ") or book["title"]
            author = input("Enter Author Name: ") or book['author']
            year = int(input("Enter Publishing Year Number: ")) or book['year']
            price = int(input("Enter Book Price: "))
            quantity = int(input("Enter Quantity Number: "))

            book_last_updated_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            book["title"] = title
            book["author"] = author
            book["year"] = year
            book["price"] = price
            book["quantity"] = quantity
            book["bookLastUpdatedAt"] = book_last_updated_at

            save_book(all_books)
            print("Book Updated Successfully")
            return all_books

    print("Book Not Found")