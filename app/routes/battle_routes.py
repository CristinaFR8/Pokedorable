from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, session

from app.routes.decorators import require_entrenador
from app.services.pokemon_service import (
    obtener_pokemon_por_id,
    obtener_pokemon_por_nombre,
    obtener_pokemon_rival,
    obtener_ataques_aleatorios,
    filtrar_pokemons,
    traducir_tipos,
    traducir_estadisticas,
    traducir_ataques,
    obtener_tipos_disponibles
)


battle_bp = Blueprint("battle", __name__)

proyecto = "Pokédorable"
nombre = "Cristina Fernández"
anio = datetime.now().year


@battle_bp.route("/pokemons", methods=["GET", "POST"])
@require_entrenador
def listado_pokemons():
    error = None

    if request.method == "POST":
        nombre_pokemon = request.form.get("pokemon", "")
        pokemon = obtener_pokemon_por_nombre(nombre_pokemon)

        if pokemon is None:
            error = "Ese Pokémon no existe en la Pokédex."
        else:
            session["pokemon"] = pokemon.id
            session.pop("pokemon_rival", None)
            session.pop("ataques", None)

            return redirect(url_for("battle.batalla"))

    nombre_filtro = request.args.get("nombre", "")
    tipo_filtro = request.args.get("tipo", "")

    pokemons_filtrados = filtrar_pokemons(
        nombre_filtro,
        tipo_filtro
    )

    tipos_pokemons = []

    for pokemon in pokemons_filtrados:
        tipos_pokemons.append(traducir_tipos(pokemon.tipos))

    pokemon_actual = obtener_pokemon_por_id(session.get("pokemon"))

    return render_template(
        "pokemons.html",
        proyecto=proyecto,
        nombre=nombre,
        anio=anio,
        pokemons=pokemons_filtrados,
        tipos_pokemons=tipos_pokemons,
        tipos_disponibles=obtener_tipos_disponibles(),
        trainer=session.get("trainer"),
        error=error,
        pokemon_seleccionado=(
            pokemon_actual.nombre if pokemon_actual else ""
        ),
        nombre_filtro=nombre_filtro,
        tipo_filtro=tipo_filtro
    )


@battle_bp.route("/battle")
@require_entrenador
def batalla():
    pokemon_id = session.get("pokemon")
    pokemon = obtener_pokemon_por_id(pokemon_id)

    if pokemon is None:
        return redirect(url_for("battle.listado_pokemons"))

    rival_id = session.get("pokemon_rival")
    rival = obtener_pokemon_por_id(rival_id)

    if rival is None or rival.id == pokemon.id:
        rival = obtener_pokemon_rival(pokemon.id)

        if rival is None:
            return redirect(url_for("battle.listado_pokemons"))

        session["pokemon_rival"] = rival.id

    ataques = session.get("ataques")

    if not ataques:
        ataques = obtener_ataques_aleatorios(pokemon)
        session["ataques"] = ataques

    ataques_traducidos = traducir_ataques(ataques)

    return render_template(
        "batalla.html",
        proyecto=proyecto,
        nombre=nombre,
        anio=anio,
        pokemon_elegido=pokemon,
        rival=rival,
        pokemon_rival=rival,
        ataques_traducidos=ataques_traducidos,
        trainer=session.get("trainer")
    )


@battle_bp.route("/pokemons/<int:id>/")
@require_entrenador
def detalle_pokemon(id):
    pokemon = obtener_pokemon_por_id(id)

    if pokemon is None:
        return "Pokémon no encontrado", 404

    tipos_traducidos = traducir_tipos(pokemon.tipos)
    estadisticas_traducidas = traducir_estadisticas(pokemon.estadisticas)
    ataques_traducidos = traducir_ataques(pokemon.ataques)

    return render_template(
        "pokemon.html",
        proyecto=proyecto,
        nombre=nombre,
        anio=anio,
        pokemon=pokemon,
        tipos_traducidos=tipos_traducidos,
        estadisticas_traducidas=estadisticas_traducidas,
        ataques_traducidos=ataques_traducidos,
        trainer=session.get("trainer")
    )
