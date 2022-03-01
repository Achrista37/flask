import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a series of precipitations"""
    # Query all passengers
    results_prcp = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    # Create a dictionary from the row data and put into prcp_dict dictionary
    all_prcp =[]
    for date, prcp in results_prcp:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["precipitation"] = prcp
        all_prcp.append(passenger_dict)

    return jsonify(all_prcp)

#@app.route("/api/v1.0/stations")
#def passengers():
#    # Create our session (link) from Python to the DB
#    session = Session(engine)
#
#    """Return a list of passenger data including the name, age, and sex of each passenger"""
#    # Query all passengers
#    results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()
#
#    session.close()
#
#    # Create a dictionary from the row data and append to a list of all_passengers
#    all_passengers = []
#    for name, age, sex in results:
#        passenger_dict = {}
#        passenger_dict["name"] = name
#        passenger_dict["age"] = age
#        passenger_dict["sex"] = sex
#        all_passengers.append(passenger_dict)

#    return jsonify(all_passengers)


#if __name__ == '__main__':
#    app.run(debug=True)
#from flask import Flask, jsonify

#justice_league_members = [
#    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
#    {"superhero": "Batman", "real_name": "Bruce Wayne"},
#    {"superhero": "Cyborg", "real_name": "Victor Stone"},
#    {"superhero": "Flash", "real_name": "Barry Allen"},
#    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
#    {"superhero": "Superman", "real_name": "Clark Kent/Kal-El"},
#    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
#]

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

#@app.route("/api/v1.0/justice-league")
#def justice_league():
#    """Return the justice league data as json"""
#
#    return jsonify(justice_league_members)
#
#
#@app.route("/")
#def welcome():
#    return (
#        f"Welcome to the Justice League API!<br/>"
#        f"Available Routes:<br/>"
#        f"/api/v1.0/justice-league<br/>"
#        f"/api/v1.0/justice-league/superhero/batman"
#    )


#"""TODO: Handle API route with variable path to allow getting info
#for a specific character based on their 'superhero' name """


if __name__ == "__main__":
    app.run(debug=True)
