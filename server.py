import json
from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime as dt

date = dt.now()

def loadClubs():
    file_path = 'clubs.json'
    if app.config['TESTING']:
        file_path = '/Users/nicolasfrenay/Desktop/Formation/P11_amelioration_application_web/Python_Testing/clubs.json'
    with open(file_path) as c:
        listOfClubs = json.load(c)['clubs']
        # print(app.config)
        return listOfClubs


def loadCompetitions():
    file_path = 'competitions.json'
    if app.config['TESTING']:
        file_path = '/Users/nicolasfrenay/Desktop/Formation/P11_amelioration_application_web/Python_Testing/competitions.json'
    with open(file_path) as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

clubs = loadClubs()

all_competitions = loadCompetitions()
past_competitions = []
competitions = []

# loop to separate past competitions
for comp in all_competitions:
    if dt.strptime(comp['date'],'%Y-%m-%d %H:%M:%S') < date:
        past_competitions.append(comp)
    else:
        competitions.append(comp)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    # add a try/except to avoid index error with unknown email
    try:
        club = \
            [club for club in clubs if club['email'] == request.form['email']][
                0]
    except IndexError:
        error = True
        return render_template('index.html', error=error)
    return render_template('welcome.html', club=club,
                           competitions=competitions,
                           past_competitions=past_competitions,
                           club_list=clubs)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    # add try/except to avoid indexerror with unknown club or competition
    try:
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = \
            [c for c in competitions if c['name'] == competition][0]
        return render_template('booking.html', club=foundClub,
                               competition=foundCompetition)
    except IndexError:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club,
                               competitions=competitions,
                               past_competitions=past_competitions,
                               club_list=clubs)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = \
        [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])

    # check if nbr of place not > 12
    if placesRequired > 12:
        flash("Vous ne pouvez prendre que 12 places au maximum !")
        return render_template('welcome.html', club=club,
                               competitions=competitions,
                               past_competitions=past_competitions,
                               club_list=clubs)

    # check if club as enough points
    if int(club['points']) < placesRequired:
        flash("Vous ne disposez pas d'assez de points !")
        return render_template('welcome.html', club=club,
                               competitions=competitions,
                               past_competitions=past_competitions,
                               club_list=clubs)

    # check if there is enough place available
    elif int(competition['numberOfPlaces']) < placesRequired:
        flash("Il n'y a pas assez de places disponibles !")
        return render_template('welcome.html', club=club,
                               competitions=competitions,
                               past_competitions=past_competitions,
                               club_list=clubs)
    else:
        competition['numberOfPlaces'] = int(
            competition['numberOfPlaces']) - placesRequired
        # Fix club point update
        club['points'] = int(club['points']) - placesRequired
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club,
                               competitions=competitions,
                               past_competitions=past_competitions,
                               club_list=clubs)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
