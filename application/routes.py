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
                        "Stats Name": found_stat_name,
                        "Base Stat": found_base
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
    
