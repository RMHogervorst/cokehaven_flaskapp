# flask app op azure
Dit is een app die je kunt gebruiken om competities
te hosten.




## Vaag idee om mee te beginnen.
* testset container ids plus indices en kilos

* hoofdpagina is live scorebord (sqlite backend)
	* er zitten al twee scores in: random keuze uit alle containers en op basis van 			 	 profilering (300 op basis van zuid amerika, fruit, en 100 random)
	* scores worden uitgedrukt in straatwaarde 
* upload is aparte pagina:  csv knop, teamnaam, opmerkingen
	* ontvang csv, tel rijen met predictions keur af bij minder dan 400 of meer dan
	* geef krantenkop terug met straatwaarde en naam van team.

## testen 
`pytest .`

##Hoe draai ik dit project?

start dev server `python flask_app.py`

start prod server with log level INFO `gunicorn flask_app:app --log-level=INFO`


## mogelijke todos:
* eigenlijk ergens nog de optie om data te verwijderen
