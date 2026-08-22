import requests
from flask import request

def character():

    charname = request.form.get("charname")
    type = request.form.get("type")
    ability = request.form.get("ability")
    move = request.form.get("move")

    return charname, type, ability, move

def get_character(charname):

    url = f"https://pokeapi.co/api/v2/pokemon/{charname}"
    
    response = requests.get(url, timeout=5)

    return response.json()

def validate_input(charname, type, ability, move):

    if not charname:
        return "Pokemon name is required"

    if not type:
         return "Pokemon type is required"

    if not ability:
        return "Pokemon ability is required"

    if not move:
        return "Pokemon move is required"

    return None