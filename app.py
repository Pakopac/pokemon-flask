from flask import Flask, render_template
from jinja2 import Template 
import json
import os

port = int(os.environ.get("PORT", 5000))

# json importation
pokemon_file = "./static/assets/pokemon_datas/pokedex.json"
with open(pokemon_file) as json_file:
    pokemon_load = json.load(json_file)
pokemon_dump = json.dumps(pokemon_load)
pokemon_json = json.loads(pokemon_dump)

type_file = "./static/assets/pokemon_datas/types.json"
with open(type_file) as json_type_file:
    file_load = json.load(json_type_file)
file_dump = json.dumps(file_load)
type_file_json = json.loads(file_dump)

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pokemons')
def project():
    return render_template('pokemons.html', pokemons=pokemon_json, types=type_file_json)

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)