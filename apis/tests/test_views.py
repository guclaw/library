from django.urls import reverse


def test_api_listview(book, client):
    endpoint = reverse('apis:book_list')
    response = client.get(endpoint)

    assert response.status_code == 200
    assert book.title in response.content.decode('utf-8')
    assert 'ala' in response.content.decode('utf-8')

