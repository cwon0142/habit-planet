# Initialise the Flask app

from flask import Flask
from .models import db

# Initialise the Flask app
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///habits.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    from .routes import main
    app.register_blueprint(main)

    return app