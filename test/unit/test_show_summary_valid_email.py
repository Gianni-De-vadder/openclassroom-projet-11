import pytest

def test_show_summary_valid_email(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'}, follow_redirects=True)
    assert b'Welcome, john@simplylift.co' in response.data


def test_show_summary_invalid_email(client):
    response = client.post('/showSummary', data={'email': 'invalid@example.com'}, follow_redirects=True)
    assert b'Unknown email address' in response.data

if __name__ == '__main__':
    pytest.main()