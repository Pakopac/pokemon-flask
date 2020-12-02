# Pokemon Flask Application

## Fonctionnement

Le but de l'application est de lister les différents pokémons et d'afficher leurs informations (comme un pokédex).  
Elle se compose de quatres pages:  
- Une page acceuil simple
- Une page pokemons pour lister les différents pokemons
- Une page de détail lorsque l'on clique sur un pokemon
- Une page de contact avec un formulaire

## Utilisation


Vous pouvez simplement cliquer sur ce lien: https://pokemon-flask.herokuapp.com/ si vous voulez tester l'application en production.  

Vous pouvez également récupérer l'application et la lancer en local, il vous faudra donc cloner le dépôt:
```
git clone git@github.com:Pakopac/pokemon-flask.git
```
Rentrez dedans:
```
cd /pokemon-flask
```
Puis deux choix s'offrent à vous:


## Simple commande
Executez la commande:
```
python app.py
```
Et rendez-vous sur le lien http://localhost:5000

##  Docker

Pour lancer l'application depuis docker:  
```
docker build -t pokemon-flask .
``` 
Puis
```
docker run -d -p 5000:5000 pokemon-flask
```
Rendez-vous enfin sur http://localhost:5000  
Et tout devrait fonctionner !!
