import pytest


def test_logout(client):
    response = client.get('/logout', follow_redirects=True)
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data

if __name__ == '__main__':
    pytest.main()