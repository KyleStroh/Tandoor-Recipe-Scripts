#!/usr/bin/python3
# this script isnt very fast, about 10 second for 9 recipes in my tests. I have this run via cron so speed isnt important
import json
import requests


api_token = ""
base_url = "http://ip-here:8081/api/recipe/"
headers = {"Authorization": f"Bearer {api_token}"}
output_dir = ""


def get_recipe_ids():
    response = requests.get(base_url, headers=headers)
    # gets the ids for each recipe and add them to a list
    if response.status_code == 200:
        recipes = response.json()
        return [recipes['results'][i]['id'] for i in range(len(recipes['results']))]
    else:
        print(response.status_code)
        print(response.content)


def export_recipe(id):
    # gets the json per recipe
    recipe_url = base_url + str(i)
    response = requests.get(recipe_url, headers=headers)
    return response.json()


def save_recipe(id, name, recipe_json):
    # saves each recipe into a seperate file
    file_name = output_dir + name + "_" + str(id) + ".json"
    print(f"writing {file_name}")
    with open(file_name, 'w', ) as f:
        json.dump(recipe_json, f)


if __name__ == "__main__":
    # do the stuff
    ids = get_recipe_ids()
    print(ids)
    for i in ids:
        recipe_json = export_recipe(ids)
        name = recipe_json['name'].lower().replace(' ', '_')
        save_recipe(i, name, recipe_json)
