from flask import Flask
from connect_to_db import init_db
from routes.members import members_bp
from routes.workout_sessions import workouts_bp

app = Flask(__name__)

# Configure your database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:your_password@localhost/fitness_center_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
init_db(app)

# Register blueprints
app.register_blueprint(members_bp)
app.register_blueprint(workouts_bp)

if __name__ == "__main__":
    app.run(debug=True)
