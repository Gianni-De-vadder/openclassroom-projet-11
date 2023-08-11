import json
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary', methods=['POST'])
def showSummary():
    email = request.form.get('email')
    club = next((c for c in clubs if c['email'] == email), None)

    if club is None:
        flash('Unknown email address')
        return render_template('index.html')

    return render_template('welcome.html', club=club, competitions=competitions)



@app.route('/book/<competition>/<club>', methods=['GET', 'POST'])
def book(competition, club):
    foundClub = next((c for c in clubs if c['name'] == club), None)
    foundCompetition = next((c for c in competitions if c['name'] == competition), None)

    if foundClub is None or foundCompetition is None:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)

    if request.method == 'POST':
        places_to_book = int(request.form['places'])

        if places_to_book > 12:
            flash("Cannot book more than 12 places")
            return render_template('booking.html', club=foundClub, competition=foundCompetition)

        if places_to_book > foundCompetition['numberOfPlaces']:
            flash("Not enough places available for booking")
            return render_template('booking.html', club=foundClub, competition=foundCompetition)

        # Mettre à jour le nombre de places de la compétition
        foundCompetition['numberOfPlaces'] -= places_to_book

        flash("Booking complete!")
        return render_template('welcome.html', club=foundClub, competitions=competitions)

    return render_template('booking.html', club=foundClub, competition=foundCompetition)



@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition_name = request.form['competition']
    club_name = request.form['club']
    places_required = int(request.form['places'])

    competition = next((c for c in competitions if c['name'] == competition_name), None)
    club = next((c for c in clubs if c['name'] == club_name), None)

    if club is None or competition is None:
        flash('Club or competition not found')
        return render_template('index.html')

    if places_required > club['available_points']:
        flash('Cannot use more points than available')
        return render_template('club.html', club=club)

    competition['numberOfPlaces'] -= places_required
    club['available_points'] -= places_required

    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)



@app.route('/logout')
def logout():
    return redirect(url_for('index'))