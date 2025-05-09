from flask import Flask, render_template, request, redirect, url_for
from models import db, init_db, Cup, Race, Result, Racer
from track_data import TRACKS
from simulate import simulate_ai_results

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    init_db()

@app.route('/')
def index():
    cups = Cup.query.all()
    return render_template('index.html', cups=cups)

@app.route('/create_cup', methods=['GET', 'POST'])
def create_cup():
    if request.method == 'POST':
        name = request.form['name']
        cup = Cup(name=name)
        db.session.add(cup)
        db.session.commit()
        return redirect(url_for('add_race', cup_id=cup.id))
    return render_template('create_cup.html')

@app.route('/add_race/<int:cup_id>', methods=['GET', 'POST'])
def add_race(cup_id):
    cup = Cup.query.get_or_404(cup_id)
    if request.method == 'POST':
        track = request.form['track']
        race = Race(cup_id=cup.id, track=track)
        db.session.add(race)
        db.session.commit()
        if len(cup.races) >= 30:
            return redirect(url_for('index'))
    return render_template('add_race.html', cup=cup, tracks=TRACKS)

# More routes for inputting results, standings, etc. coming next...

if __name__ == '__main__':
    app.run(debug=True)
