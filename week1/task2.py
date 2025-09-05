# task2.py
import json, os

FILE = "library.json"

def load_books():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save_books(books):
    json.dump(books, open(FILE, "w"), indent=2)

def add_book():
    books = load_books()
    book = {
        "ID": input("Enter Book ID: "),
        "Title": input("Enter Book Title: "),
        "Author": input("Enter Author Name: "),
        "Qty": int(input("Enter Quantity: "))
    }
    books.append(book)
    save_books(books)
    print("✅ Book added!\n")

def view_books():
    books = load_books()
    if not books: return print("⚠ No books available.\n")
    print("\nID | Title            | Author          | Qty")
    print("-"*50)
    for b in books:
        print(f"{b['ID']:<2} | {b['Title']:<15} | {b['Author']:<15} | {b['Qty']}")

def borrow_book():
    books = load_books()
    bid = input("Enter Book ID to borrow: ")
    for b in books:
        if b["ID"] == bid and b["Qty"] > 0:
            b["Qty"] -= 1
            save_books(books)
            return print(" Book borrowed!\n")
    print(" Not available.\n")

def return_book():
    books = load_books()
    bid = input("Enter Book ID to return: ")
    for b in books:
        if b["ID"] == bid:
            b["Qty"] += 1
            save_books(books)
            return print(" Book returned!\n")
    print(" Book not found.\n")

while True:
    choice = input("\n1.Add  2.View  3.Borrow  4.Return  5.Exit → ")
    if choice=="1": add_book()
    elif choice=="2": view_books()
    elif choice=="3": borrow_book()
    elif choice=="4": return_book()
    elif choice=="5": break
    else: print(" Invalid choice")
