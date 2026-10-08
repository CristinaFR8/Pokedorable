import json
from pathlib import Path
from datetime import datetime
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

TRADUCCION_ATAQUES = {
    "fire-blast": "Llamarada",
    "rage": "Furia",
    "thunderbolt": "Rayo",
    "uproar": "Alboroto",
    "last-resort": "Última baza",
    "dream-eater": "Come sueños",
    "dynamic-punch": "Puño dinámico",
    "play-rough": "Carantoña",
    "psychic-noise": "Psicorruido",
    "headbutt": "Cabezazo",

    "mud-shot": "Disparo Lodo",
    "aqua-jet": "Acua Jet",
    "hydro-pump": "Hidrobomba",
    "knock-off": "Desarme",
    "waterfall": "Cascada",
    "bulldoze": "Terratemblor",
    "tera-blast": "Teraexplosión",
    "facade": "Imagen",
    "dive": "Buceo",
    "iron-tail": "Cola Férrea",

    "x-scissor": "Tijera X",
    "signal-beam": "Rayo Señal",
    "fury-cutter": "Cortefuria",
    "skitter-smack": "Golpe Rastrero",
    "seed-bomb": "Bomba Germen",
    "grassy-glide": "Fitoimpulso",
    "false-swipe": "Falso Tortazo",
    "bug-bite": "Picadura",
    "leafage": "Follaje",
    "petal-blizzard": "Tormenta Floral",

    "dig": "Excavar",
    "superpower": "Fuerza Bruta",
    "metal-claw": "Garra Metal",
    "shadow-claw": "Garra Umbría",
    "aerial-ace": "Golpe Aéreo",
    "powder-snow": "Nieve Polvo",
    "trailblaze": "Abrecaminos",

    "alluring-voice": "Canto Encantador",
    "tidy-up": "Limpieza General",
    "u-turn": "Ida y Vuelta",
    "wake-up-slap": "Espabila",
    "mud-slap": "Bofetón Lodo",
    "hidden-power": "Poder Oculto",

    "flare-blitz": "Envite Ígneo",
    "heat-wave": "Onda Ígnea",
    "poltergeist": "Poltergeist",
    "inferno": "Infierno",
    "mystical-fire": "Fuego Místico",
    "secret-power": "Daño Secreto",
    "acid": "Ácido",
    "smog": "Polución",
    "ember": "Ascuas",
    "flame-burst": "Pirotecnia",

    "psychic": "Psíquico",
    "fairy-wind": "Viento Feérico",
    "moonblast": "Fuerza Lunar",
    "magical-leaf": "Hoja Mágica",
    "draining-kiss": "Beso Drenaje",
    "covet": "Antojo",

    "bite": "Mordisco",
    "crunch": "Triturar",
    "rock-slide": "Avalancha",
    "take-down": "Derribo",
    "round": "Canon",
    "rock-climb": "Treparrocas"
}

with RUTA_DATOS.open(encoding="utf-8") as f:
    pokemons = json.load(f)


@app.route('/')
def index():
    proyecto = "Pokemon Battle Web"
    nombre = "Cristina Fernández"
    anio = datetime.now().year
    pokemon_destacado = pokemons[0]

    return render_template(
        'index.html',
        proyecto=proyecto,
        nombre=nombre,
        anio=anio,
        pokemon_destacado=pokemon_destacado
    )


@app.route('/pokemons/')
def listado_pokemons():
    tipos_pokemons = []

    for pokemon in pokemons:
        tipos_traducidos = []

        for tipo in pokemon['types']:
            tipos_traducidos.append(TRADUCCION_TIPOS[tipo])

        tipos_pokemons.append(tipos_traducidos)

    return render_template(
        'pokemons.html',
        pokemons=pokemons,
        tipos_pokemons=tipos_pokemons
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

            ataques_traducidos = []

            for move in pokemon['moves']:
                ataques_traducidos.append(
                    TRADUCCION_ATAQUES[move['name']]
                )

            return render_template(
                'pokemon.html',
                pokemon=pokemon,
                clasificacion_peso=clasificacion_peso,
                tipos_traducidos=tipos_traducidos,
                estadisticas_traducidas=estadisticas_traducidas,
                ataques_traducidos=ataques_traducidos
            )

    return "Pokemon no encontrado", 404


if __name__ == '__main__':
    app.run('127.0.0.1', 5038, debug=True)
