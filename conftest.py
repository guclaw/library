import pytest

from books import models


@pytest.fixture
def book(db):
    return models.Book.objects.create(
        title='A good title',
        subtitle='an excellent book',
        author='John Doe',
        isbn='123456781'
    )
