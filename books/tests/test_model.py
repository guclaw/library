def test_book_contect(book):
    assert book.title == 'A good title'
    assert book.subtitle == 'an excellent book'
    assert book.author == 'John Doe'
    assert book.isbn == '123456781'
