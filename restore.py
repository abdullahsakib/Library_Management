import json

def restore_book():
    try:
        with open("books.json",'r') as file:
            all_books =json.load(file)
        return all_books
    except FileNotFoundError:
            return []