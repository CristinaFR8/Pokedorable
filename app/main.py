import json
from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)

RUTA_DATOS = Path(__file__).resolve().parent.parent / \
    "data" / "pokemons-cute.json"

with RUTA_DATOS.open(encoding="utf-8") as f:
    pokemons = json.load(f)


@app.route('/')
def index():
    proyecto = "Pokemon Battle Web"
    nombre = "Cristina Fernández"
    anio = 2026

    return render_template(
        'index.html',
        proyecto=proyecto,
        nombre=nombre,
        anio=anio
    )


@app.route('/pokemons/')
def listado_pokemons():
    return render_template(
        'pokemons.html',
        pokemons=pokemons
    )


@app.route('/pokemons/<int:id>/')
def detalle_pokemon(id):
    for pokemon in pokemons:
        if pokemon['id'] == id:
            return render_template(
                'pokemon.html',
                pokemon=pokemon
            )

    return "Pokemon no encontrado", 404


if __name__ == '__main__':
    app.run('127.0.0.1', 5038, debug=True)