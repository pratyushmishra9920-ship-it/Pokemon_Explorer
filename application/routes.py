from flask import render_template, jsonify, url_for, request
from application import character, validate_input, get_character
from application import app
import requests, json

print("ROUTES APP:", id(app))

@app.route("/")
def main():

    return render_template("home_page.html")

@app.route("/character", methods = ["GET","Post"])
def info():

    if request.method == "GET":
        return render_template("forms.html")


    charname, type, ability, move = character()

    error = validate_input(charname, type, ability, move)
        
    if error:
        result = {
                    "success": False,
                    "error": error,
                    "status": 404
                }
        return render_template(
            "forms.html",
            result = json.dumps(result, indent=4)
        )
    
    try: 
        data = get_character(charname)
    except requests.exceptions.Timeout:
        result = {
                    "success": False,
                    "error": "External API took long to respond",
                    "status": 504
                }
        return render_template(
            "forms.html",
            result = json.dumps(result, indent=4)
        )


    
    found_name = None
    found_type = None
    found_ability = None
    found_move = None
    found_base = []
    found_stat_name = []

    if data["name"] == charname:
        found_name = data["name"]
    for key in data["types"]:
        if key["type"]["name"] == type:
            found_type = key["type"]["name"]
    for key in data["abilities"]:
        if key["ability"]["name"] == ability:
            found_ability = key["ability"]["name"]
    for key in data["moves"]:
        if key["move"]["name"] == move:
            found_move = key["move"]["name"]
    for key in data["stats"]: 
        found_base.append(key["base_stat"])
        found_stat_name.append(key["stat"]["name"])

    if found_name and found_type and found_ability and found_move:
        result = {
                "success": True,
                "Data": {
                        "Id": data["id"],
                        "Name": found_name,
                        "Height": data["height"],
                        "Weight": data["weight"],
                        "Base Experience": data["base_experience"],
                        "Type": found_type,
                        "Ability": found_ability,
                        "Move": found_move,
                        "Stats": found_stat_name,
                        "Base Stats": found_base
                    }
                }
        return render_template(
                "forms.html",
                result=json.dumps(result, indent=4)
               )
    else:
        result = {
                    "success": False,
                    "error": "Some Input's are missing!"
                }
        return render_template(
                "forms.html",
                result=json.dumps(result, indent=4)
                )
    
@app.route("/rawapi")
def rawapi():
    result1 = "https://pokeapi.co/api/v2/pokemon/"
    result2 = {
                "count": 1351,
                "next": "https://pokeapi.co/api/v2/pokemon/?offset=20&limit=20",
                "previous": None,
                "results": [
                                {
                                    "name": "bulbasaur",
                                    "url": "https://pokeapi.co/api/v2/pokemon/1/"
                                },
                                {
                                    "name": "ivysaur",
                                    "url": "https://pokeapi.co/api/v2/pokemon/2/"
                                },
                                {
                                    "name": "venusaur",
                                    "url": "https://pokeapi.co/api/v2/pokemon/3/"
                                },
                                {
                                    "name": "charmander",
                                    "url": "https://pokeapi.co/api/v2/pokemon/4/"
                                },
                                {
                                    "name": "charmeleon",
                                    "url": "https://pokeapi.co/api/v2/pokemon/5/"
                                },
                                {
                                    "name": "charizard",
                                    "url": "https://pokeapi.co/api/v2/pokemon/6/"
                                },
                                {
                                    "name": "squirtle",
                                    "url": "https://pokeapi.co/api/v2/pokemon/7/"
                                },
                                {
                                    "name": "wartortle",
                                    "url": "https://pokeapi.co/api/v2/pokemon/8/"
                                },
                                {
                                    "name": "blastoise",
                                    "url": "https://pokeapi.co/api/v2/pokemon/9/"
                                },
                                {
                                    "name": "caterpie",
                                    "url": "https://pokeapi.co/api/v2/pokemon/10/"
                                },
                                {
                                    "name": "metapod",
                                    "url": "https://pokeapi.co/api/v2/pokemon/11/"
                                },
                                {
                                    "name": "butterfree",
                                    "url": "https://pokeapi.co/api/v2/pokemon/12/"
                                },
                                {
                                    "name": "weedle",
                                    "url": "https://pokeapi.co/api/v2/pokemon/13/"
                                },
                                {
                                    "name": "kakuna",
                                    "url": "https://pokeapi.co/api/v2/pokemon/14/"
                                },
                                {
                                    "name": "beedrill",
                                    "url": "https://pokeapi.co/api/v2/pokemon/15/"
                                },
                                {
                                    "name": "pidgey",
                                    "url": "https://pokeapi.co/api/v2/pokemon/16/"
                                },
                                {
                                    "name": "pidgeotto",
                                    "url": "https://pokeapi.co/api/v2/pokemon/17/"
                                },
                                {
                                    "name": "pidgeot",
                                    "url": "https://pokeapi.co/api/v2/pokemon/18/"
                                },
                                {
                                    "name": "rattata",
                                    "url": "https://pokeapi.co/api/v2/pokemon/19/"
                                },
                                {
                                    "name": "raticate",
                                    "url": "https://pokeapi.co/api/v2/pokemon/20/"
                                }
                    ]
                }
    
    return render_template("rawapi.html", 
                        result1 = json.dumps(result1, indent=4), 
                        result2 = json.dumps(result2, indent=4)
                    )
