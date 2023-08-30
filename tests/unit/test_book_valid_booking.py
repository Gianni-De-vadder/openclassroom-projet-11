import pytest


def test_book_valid_booking(client):
    response = client.get(
        "/book/Spring%20Festival/Simply%20Lift",
        data={"places": "5"},
        follow_redirects=True,
    )
    assert b"Spring Festival" in response.data


if __name__ == "__main__":
    pytest.main()
