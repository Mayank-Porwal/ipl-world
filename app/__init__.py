from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.teams.routes import teams
    app.register_blueprint(teams)

    return app
