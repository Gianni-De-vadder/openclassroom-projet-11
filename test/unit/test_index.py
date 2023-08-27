import pytest

def test_index(client):
    response = client.get('/')
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data

if __name__ == '__main__':
    pytest.main()