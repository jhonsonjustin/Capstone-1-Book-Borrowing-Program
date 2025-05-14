# CAPSTONE 1
# Program: Program Peminjaman Buku

# Library
books = [
    {'BookID': 1, 'Title': 'The 7 Habits of Highly Effective People', 'Author': 'Stephen R. Covey', 'Genre': 'Self Improvement', 'Status': 'Available'},
    {'BookID': 2, 'Title': 'How to Win Friends and Influence People', 'Author': 'Dale Carnegie', 'Genre': 'Self Improvement','Status': 'Available'},
    {'BookID': 3, 'Title': 'Atomic Habits', 'Author': 'James Clear', 'Genre': 'Self Improvement', 'Status': 'Available'},
    {'BookID': 4, 'Title': 'Awaken the Giant Within', 'Author': 'Tony Robbins', 'Genre': 'Self Improvement', 'Status': 'Available'},
    {'BookID': 5, 'Title': 'The Power of Now', 'Author': 'Eckhart Tolle','Genre': 'Spirituality', 'Status': 'Available'}
]

# Create Menu
# 1. Read Books
# Pengecekan jika buku ada atau tidak di library
 
def view_books():
    if not books:
        print("No books available in the library.")
        return

    print("\nList of Books:")
    print("-" * 40)
    for book in books:
        for key, value in book.items():
            print(f"{key}: {value}")
        print("-" * 40)

# 2. Add Book
def add_book():
    global books
    # Validasi data yang diinputkan
    try:
        new_id = int(input("Enter new book ID: "))
    except ValueError:
        print("Invalid input. ID must be a number.")
        return

    if any(book['BookID'] == new_id for book in books):
        print("Error: A book with this ID already exists. Please use a unique ID.")
        return

    # User input
    title = input("Enter book title: ").capitalize()
    author = input("Enter author name: ").capitalize()
    genre = input("Enter book genre: ").capitalize()

    # Konfirmasi sebelum menambahkan buku
    while True:
        confirmation = input(f"Are you sure you want to add the book '{title}' by {author}? (Yes/No): ").capitalize()
        if confirmation == 'Yes':
            books.append({'BookID': new_id, 'Title': title, 'Author': author, 'Genre': genre, 'Status': 'Available'})
            print("Book added successfully!")
            return
        elif confirmation == 'No':
            print("Add book cancelled. No changes were made.")
            return
        else:
            print("Please answer 'Yes' or 'No'.")

# 3. Update Book
def update_book():
    global books
    try:
        book_id = int(input("Enter the ID of the book to update: "))
    except ValueError:
        print("Invalid input. ID must be a number.")
        return

    # Check apakaha BookID ada?
    book_to_update = None
    for book in books:
        if book['BookID'] == book_id:
            book_to_update = book
            break

    if not book_to_update:
        print("Book not found.")
        return

    new_title = input("Enter new title (leave blank to keep current): ").capitalize()
    new_genre = input("Enter new genre (leave blank to keep current): ").capitalize()
    new_author = input("Enter new author (leave blank to keep current): ").capitalize()

    while True:
        new_status = input("Enter new status (Available/Borrowed, leave blank to keep current): ").capitalize()
        if new_status in ['Available', 'Borrowed', '']:
            break
        print("Invalid status. Please enter 'Available', 'Borrowed', or leave blank.")

    while True:
        new_confirmation = input("Are you sure you want to update the data? (Yes/No): ").capitalize()
        if new_confirmation == 'Yes':
           
            if new_title:
                book_to_update['Title'] = new_title
            if new_genre:
                book_to_update['Genre'] = new_genre
            if new_author:
                book_to_update['Author'] = new_author
            if new_status in ['Available', 'Borrowed']:
                book_to_update['Status'] = new_status

            print("Book updated successfully!")
            return
        elif new_confirmation == 'No':
            print("Update cancelled. No changes were made.")
            return
        else:
            print("Please answer 'Yes' or 'No'.")

# 4. Delete Book
def delete_book():
    try:
        book_id = int(input("Enter the ID of the book to delete: "))
    except ValueError:
        print("Invalid input. ID must be a number.")
        return
    #Global untuk mengakses variabel books
    global books
    if any(book['BookID'] == book_id for book in books):
         # Konfirmasi delete
         while True:
            confirmation = input("Are you sure you want to delete this book? (Yes/No): ").capitalize()
            if confirmation == 'Yes':
                books = [book for book in books if book['BookID'] != book_id]
                print("Book deleted successfully!")
                return
            elif confirmation == 'No':
                print("Delete cancelled. No changes were made.")
                return
            else:
                print("Please answer 'Yes' or 'No'.")
    else:
        print("Book not found. No changes made.")

# 5. Display Menu
def main():
    while True:
        print("\n=== Book Borrowing System Menu ===")
        print("1. View Books")
        print("2. Add Book")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice < 1 or choice > 5:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == 1:
            view_books()
        elif choice == 2:
            add_book()
        elif choice == 3:
            update_book()
        elif choice == 4:
            delete_book()
        elif choice == 5:
            print("Thank you for using the Book Borrowing System. Goodbye! 👋")
            break


main()
