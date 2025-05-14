# Capstone-1-Book-Borrowing-Program
A simple Python command-line application to manage a library’s book collection. 
This program allows users to add new books, update existing book details, delete books, and track their availability status. 
It includes confirmation prompts to help prevent accidental changes.

Features
1.	Add new books with unique IDs, titles, authors, and genres
2.	Update book details including title, author, genre, and status (Available/Borrowed)
3.	Delete books safely with confirmation
4.	Confirmation prompts before any data modification to avoid mistakes
5.	Simple and user-friendly command-line interface

How It Works
1. The program stores book data in a list of dictionaries, each representing a book with keys like BookID, Title, Author, Genre, and Status.
2. When adding a book, the program checks for unique IDs to avoid duplicates.
3. Updating and deleting books requires entering the book’s ID and confirming the action.
4. Status can be set to "Available" or "Borrowed" to track book availability.
