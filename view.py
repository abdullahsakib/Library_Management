from save import save_book
import json

def book_view():
    with open("books.json",'r') as file:
        books =json.load(file)

    if books!=[]:
        for b in books:
            print(b)
    else:
        print('no book found')

