
from datetime import datetime

from flask import Blueprint, render_template, redirect, url_for, session

from app.forms.entrenador_form import EntrenadorForm
from app.services.pokemon_service import obtener_pokemons_portada


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

    pokemon_destacado, pokemon_aliado = obtener_pokemons_portada()

    return render_template(
        "index.html",
        proyecto=proyecto,
        nombre=nombre,
        anio=anio,
        pokemon_destacado=pokemon_destacado,
        pokemon_aliado=pokemon_aliado,
        form=form,
        trainer=session.get("trainer", "")
    )


@main_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("main.index"))
