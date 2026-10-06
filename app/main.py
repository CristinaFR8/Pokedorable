import json
from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)

RUTA_DATOS = Path(__file__).resolve().parent.parent / \
    "data" / "pokemons-cute.json"

TRADUCCION_TIPOS = {
    "normal": "Normal",
    "fire": "Fuego",
    "water": "Agua",
    "electric": "Eléctrico",
    "grass": "Planta",
    "ice": "Hielo",
    "fighting": "Lucha",
    "poison": "Veneno",
    "ground": "Tierra",
    "flying": "Volador",
    "psychic": "Psíquico",
    "bug": "Bicho",
    "rock": "Roca",
    "ghost": "Fantasma",
    "dragon": "Dragón",
    "dark": "Siniestro",
    "steel": "Acero",
    "fairy": "Hada"
}

TRADUCCION_ESTADISTICAS = {
    "hp": "PS",
    "attack": "Ataque",
    "defense": "Defensa",
    "special-attack": "Ataque especial",
    "special-defense": "Defensa especial",
    "speed": "Velocidad"
}

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

            if pokemon['weight'] < 20:
                clasificacion_peso = "Ligero"
            elif pokemon['weight'] <= 60:
                clasificacion_peso = "Medio"
            else:
                clasificacion_peso = "Pesado"

            tipos_traducidos = []

            for tipo in pokemon['types']:
                tipos_traducidos.append(TRADUCCION_TIPOS[tipo])

            estadisticas_traducidas = []

            for stat in pokemon['stats']:
                estadisticas_traducidas.append({
                    "nombre": TRADUCCION_ESTADISTICAS[stat['name']],
                    "valor": stat['value']
                })

            return render_template(
                'pokemon.html',
                pokemon=pokemon,
                clasificacion_peso=clasificacion_peso,
                tipos_traducidos=tipos_traducidos,
                estadisticas_traducidas=estadisticas_traducidas
            )

    return "Pokemon no encontrado", 404


if __name__ == '__main__':
    app.run('127.0.0.1', 5038, debug=True)
