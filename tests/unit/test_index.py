def test_index(client):
    response = client.get('/')
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data
