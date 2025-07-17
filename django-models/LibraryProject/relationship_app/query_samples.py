from relationship_app.models import Author, Book, Library, Librarian

# Get all books by a specific author
author = Author.objects.get(name='George Orwell')
books = Book.objects.filter(author=author)

# List all books in a library
library = Library.objects.get(name='Central Library')
library_books = library.books.all()

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)