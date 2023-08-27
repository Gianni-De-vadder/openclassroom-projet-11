import pytest

def test_book_invalid_club(client):
    response = client.post('/book/Spring%20Festival/Invalid%20Club', data={'places': '5'}, follow_redirects=True)
    assert b"Something went wrong, you don't have enough points." in response.data


if __name__ == '__main__':
    pytest.main()