import pytest

def test_book_invalid_competition(client):
    response = client.post('/book/Invalid%20Competition/Simply%20Lift', data={'places': '5'}, follow_redirects=True)
    assert b"Something went wrong" in response.data

if __name__ == '__main__':
    pytest.main()