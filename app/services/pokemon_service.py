import random

from app.repositories.pokemon_repository import obtener_pokemons


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


def obtener_todos_pokemons():
    return obtener_pokemons()


def obtener_pokemons_portada():
    pokemons = obtener_todos_pokemons()
    return pokemons[0], pokemons[1]


def obtener_pokemon_por_id(id):
    pokemons = obtener_todos_pokemons()

    for pokemon in pokemons:
        if pokemon.id == id:
            return pokemon

    return None


def obtener_pokemon_por_nombre(nombre):
    pokemons = obtener_todos_pokemons()

    for pokemon in pokemons:
        if pokemon.nombre.lower() == nombre.lower():
            return pokemon

    return None


def traducir_tipos(tipos):
    tipos_traducidos = []

    for tipo in tipos:
        tipo_traducido = TRADUCCION_TIPOS.get(tipo, tipo.title())
        tipos_traducidos.append(tipo_traducido)

    return tipos_traducidos


def traducir_estadisticas(estadisticas):
    estadisticas_traducidas = []

    for estadistica in estadisticas:
        estadistica_traducida = {
            "nombre": TRADUCCION_ESTADISTICAS.get(
                estadistica["name"],
                estadistica["name"]
            ),
            "valor": estadistica["value"]
        }

        estadisticas_traducidas.append(estadistica_traducida)

    return estadisticas_traducidas


def traducir_ataques(ataques):
    ataques_traducidos = []

    for ataque in ataques:
        ataque_traducido = {
            "nombre": TRADUCCION_ATAQUES.get(
                ataque.nombre,
                ataque.nombre.replace("-", " ").title()
            ),
            "tipo": TRADUCCION_TIPOS.get(
                ataque.tipo,
                ataque.tipo.title()
            ),
            "precision": ataque.precision,
            "potencia": ataque.potencia
        }

        ataques_traducidos.append(ataque_traducido)

    return ataques_traducidos


def filtrar_pokemons(nombre="", tipo=""):
    pokemons = obtener_todos_pokemons()
    pokemons_filtrados = []

    for pokemon in pokemons:
        coincide_nombre = nombre.lower() in pokemon.nombre.lower()

        coincide_tipo = (
            tipo == "" or tipo.lower() in pokemon.tipos
        )

        if coincide_nombre and coincide_tipo:
            pokemons_filtrados.append(pokemon)

    return pokemons_filtrados


def obtener_tipos_disponibles():
    pokemons = obtener_todos_pokemons()
    tipos_disponibles = {}

    for pokemon in pokemons:
        for tipo in pokemon.tipos:
            tipos_disponibles[tipo] = TRADUCCION_TIPOS.get(
                tipo,
                tipo.title()
            )

    return tipos_disponibles


def obtener_datos_pokedex(nombre="", tipo=""):
    pokemons_filtrados = filtrar_pokemons(nombre, tipo)

    tipos_pokemons = []

    for pokemon in pokemons_filtrados:
        tipos_pokemons.append(traducir_tipos(pokemon.tipos))

    return (
        pokemons_filtrados,
        tipos_pokemons,
        obtener_tipos_disponibles()
    )


def obtener_datos_detalle_pokemon(id):
    pokemon = obtener_pokemon_por_id(id)

    if pokemon is None:
        return None, [], [], []

    tipos_traducidos = traducir_tipos(pokemon.tipos)
    estadisticas_traducidas = traducir_estadisticas(pokemon.estadisticas)
    ataques_traducidos = traducir_ataques(pokemon.ataques)

    return (
        pokemon,
        tipos_traducidos,
        estadisticas_traducidas,
        ataques_traducidos
    )


def obtener_pokemon_rival(id_pokemon):
    pokemons = obtener_todos_pokemons()
    posibles_rivales = []

    for pokemon in pokemons:
        if pokemon.id != id_pokemon:
            posibles_rivales.append(pokemon)

    if not posibles_rivales:
        return None

    return random.choice(posibles_rivales)


def obtener_ataques_aleatorios(pokemon):
    return random.sample(pokemon.ataques, 4)