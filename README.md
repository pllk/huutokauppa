# Huutokauppa

## Sovelluksen toiminnot

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan ilmoituksia.
* Käyttäjä pystyy lisäämään kuvia ilmoitukseen.
* Käyttäjä näkee sovellukseen lisätyt ilmoitukset.
* Käyttäjä pystyy etsimään ilmoituksia hakusanalla.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät tilastoja ja käyttäjän lisäämät ilmoitukset.
* Käyttäjä pystyy valitsemaan ilmoitukselle yhden tai useamman luokittelun (esim. ilmoituksen osasto, tavaran kunto, maksutapa).
* Käyttäjä pystyy huutamaan myytävänä olevia tuotteita.

## Sovelluksen asennus

Asenna `flask`-kirjasto:

```
$ pip install flask
```

Luo tietokannan taulut ja lisää alkutiedot:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Voit käynnistää sovelluksen näin:

```
$ flask run
```
