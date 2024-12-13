from save import save_book
import json

def book_view():
    with open("books.json",'r') as file:
        all_books =json.load(file)

    if all_books != []:
        for book in all_books:
            print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']} | Book Added At: {book['bookAddedAt']} | Book Last Updated At: {book['bookLastUpdatedAt']}")
    else:
        print("No Book found.")

