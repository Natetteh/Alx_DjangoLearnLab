book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
print(book)
# Output: Nineteen Eighty-Four by George Orwell
