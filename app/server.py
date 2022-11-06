from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime

from app.db_context import DbContext
from app.business import Business


def create_app(config, running_env='production'):
    app = Flask(__name__)
    app.secret_key = 'something_special'
    app.config.from_object(config)

    global business
    business = Business(running_env)

    global db_context
    db_context = DbContext(running_env)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/showSummary', methods=['POST'])
    def show_summary():
        club = business.retrieve_club(request.form['email'])
        if club is None:
            return render_template('index.html', error=True)
        return render_template('welcome.html', club=club, competitions=db_context.competitions, datetime=datetime)

    @app.route('/book/<competition>/<club>')
    def book(competition, club):
        found_club = [c for c in db_context.clubs if c['name'] == club][0]
        found_competition = [c for c in db_context.competitions if c['name'] == competition][0]
        if found_club and found_competition:
            return render_template('booking.html', club=found_club, competition=found_competition)
        else:
            flash("Something went wrong-please try again")
            return render_template('welcome.html', club=club, competitions=db_context.competitions)

    @app.route('/purchasePlaces', methods=['POST'])
    def purchase_places():
        purchase = business.set_club_points_balance(
            request.form['club'], request.form['competition'], request.form['places']
            )
        if purchase['succeeded'] is False:
            competition = [c for c in db_context.competitions if c['name'] == request.form['competition']][0]
            flash("Not enough points available")
            return render_template(
                'booking.html', club=purchase['club'], competition=competition, error=True
                )
        flash("Great! Booking completed!")
        return render_template('welcome.html', club=purchase['club'], competitions=purchase['competitions'])

# TODO: Add route for points display

    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))

    return app
