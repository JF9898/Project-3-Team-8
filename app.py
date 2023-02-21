# Import Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template
import psycopg2
from credentials import username, password

# Database Setup
engine = create_engine(f"postgresql+psycopg2://{username}:{password}@localhost:5432/soccer_db")

# Set up a base using the existing table in the database
Base = automap_base()
Base.prepare(autoload_with=engine)
Base.classes.keys()

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def index():
    return render_template('index.html')



# @app.route("/api/v1.0/teams")
# def teams():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all team names"""
#     # Query all teams
#     results = session.query(Teams).all()

#     session.close()

#     # Convert list of tuples into normal list
#     all_names = list(np.ravel(results))

#     return jsonify(all_names)



if __name__ == '__main__':
    app.run(debug=True)
