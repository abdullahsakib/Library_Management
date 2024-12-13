
import json

def save_book(all_books):
    # with open("all_books.json", "w") as fp:
    #     json.dump(all_books, fp, indent=4)
    with open("books.json",'w') as file:
        json.dump(all_books, file, indent=4)