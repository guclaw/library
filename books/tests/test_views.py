from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_book_listview_contain_books(client, book):
    endpoint = reverse('books:home')
    response = client.get(endpoint)

    assert response.status_code == 200
    assert 'A good title' in response.content.decode('utf-8')
    assert 'books/book_list.html' in (t.name for t in response.templates)
    assertTemplateUsed(response, 'books/book_list.html')
