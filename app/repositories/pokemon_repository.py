import json
from pathlib import Path

from app.models.pokemon import Pokemon
from app.models.movimiento import Movimiento


RUTA_JSON = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "pokemons-cute.json"
)


def cargar_pokemons():
    with open(RUTA_JSON, encoding="utf-8") as archivo:
        datos = json.load(archivo)

    pokemons = []

    for dato in datos:
        ataques = []

        for ataque in dato["moves"]:
            movimiento = Movimiento(
                ataque["name"],
                ataque["type"],
                ataque["accuracy"],
                ataque["power"]
            )

            ataques.append(movimiento)

        pokemon = Pokemon(
            dato["id"],
            dato["name"],
            dato["height"],
            dato["weight"],
            dato["stats"],
            dato["sprites"],
            dato["types"],
            ataques
        )

        pokemons.append(pokemon)

    return pokemons


POKEMONS = cargar_pokemons()


def obtener_pokemons():
    return list(POKEMONS)