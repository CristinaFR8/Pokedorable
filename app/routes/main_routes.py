
from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, session

from app.forms.entrenador_form import EntrenadorForm
from app.services.pokemon_service import obtener_todos_pokemons


main_bp = Blueprint("main", __name__)

proyecto = "Pokédorable"
nombre = "Cristina Fernández"
anio = datetime.now().year


@main_bp.route("/", methods=["GET", "POST"])
def index():

    form = EntrenadorForm()

    if not session.get("trainer") and form.validate_on_submit():
        session["trainer"] = form.trainer.data
        return redirect(url_for("battle.listado_pokemons"))

    pokemons = obtener_todos_pokemons()

    return render_template(
        "index.html",
        proyecto=proyecto,
        nombre=nombre,
        anio=anio,
        pokemon_destacado=pokemons[0],
        pokemon_aliado=pokemons[1],
        form=form,
        trainer=session.get("trainer", "")
    )


@main_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("main.index"))
