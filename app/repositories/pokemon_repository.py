import json
from app.models.pokemon import Pokemon


def obtener_pokemons():
    with open("data/pokemons-cute.json", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    pokemons = []

    for dato in datos:
        pokemon = Pokemon(
            dato["id"],
            dato["name"],
            dato["height"],
            dato["weight"],
            dato["stats"],
            dato["sprites"],
            dato["types"],
            dato["moves"]
        )

        pokemons.append(pokemon)

    return pokemons