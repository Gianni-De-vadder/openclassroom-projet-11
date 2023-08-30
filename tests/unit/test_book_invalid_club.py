import pytest

def test_book_invalid_club(client):
    club_name = "Invalid Club"
    competition_name = "Spring Festival"
    expected_message = "Club or competition not found"  # Utilisez une chaîne de caractères

    response = client.get(
        f"/book/{competition_name}/{club_name}",
        data={"places": 2},
        follow_redirects=True,
    )
    
    assert expected_message.encode() in response.data  # Encodez la chaîne en bytes pour la comparaison
