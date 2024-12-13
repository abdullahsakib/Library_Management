
import json

def save_book(all_books):
    with open("books.json",'w') as file:
        json.dump(all_books, file, indent=4)