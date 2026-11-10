
import os

from flask import Flask
from flask_session import Session

from app.routes.main_routes import main_bp
from app.routes.battle_routes import battle_bp


app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "clave-solo-para-desarrollo"
)

app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_FILE_DIR"] = "./.flask_session"

Session(app)

app.register_blueprint(main_bp)
app.register_blueprint(battle_bp)


if __name__ == "__main__":
    app.run("127.0.0.1", 5038, debug=True)
