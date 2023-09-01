import pytest

def test_book_invalid_competition(client):
    response = client.get(
        "/book/Invalid%20Competition/Simply%20Lift",
        data={"places": "5"},
        follow_redirects=True,
    )

    # Get the raw response content as text
    response_text = response.get_data(as_text=True)
    print(response_text)  # Print the response content for inspection

    # Check if the expected message is in the response content
    assert "Club or competition not found" in response_text
