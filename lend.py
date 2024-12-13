import json
from datetime import datetime, timedelta
from save import save_book

def load_lends():
    try:
        with open("lends.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_lends(lends):
    with open("lends.json", 'w') as file:
        json.dump(lends, file, indent=4)

def lend_book(all_books,lends):
    title=input("enter book title")
    for book in all_books:
        if book["title"] == title and book["quantity"] > 0:
            borrower_name = input("Enter Borrower's Name: ")
            phone_number = input("Enter Borrower's Phone Number: ")
            return_date = (datetime.now() + timedelta(days=14)).strftime("%d-%m-%Y")

            lend_record = {
                "borrower_name": borrower_name,
                "phone_number": phone_number,
                "book_title": title,
                "lend_date": datetime.now().strftime("%d-%m-%Y"),
                "return_due_date": return_date
            }

            lends.append(lend_record)
            book['quantity']-=1

            save_book(all_books)

            save_lends(lends)
            
            print(f"Book '{title}' lent successfully to {borrower_name}. Due date: {return_date}")


