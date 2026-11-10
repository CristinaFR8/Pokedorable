from functools import wraps
from flask import session, redirect, url_for


def require_entrenador(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        trainer = session.get("trainer")

        if not trainer or len(trainer) < 3 or len(trainer) > 15:
            return redirect(url_for("main.index"))

        return func(*args, **kwargs)

    return wrapper