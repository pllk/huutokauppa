# Pylint-raportti

Pylint antaa seuraavan raportin sovelluksesta:

```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:5:0: E0401: Unable to import 'flask' (import-error)
app.py:6:0: E0401: Unable to import 'flask' (import-error)
app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:21:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:28:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:34:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:39:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:47:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:57:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:69:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:79:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:85:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:118:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:142:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:160:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:173:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:198:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:215:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:250:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:264:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:250:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:271:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:275:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:292:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:301:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:292:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:311:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:2:0: E0401: Unable to import 'flask' (import-error)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
************* Module items
items.py:1:0: C0114: Missing module docstring (missing-module-docstring)
items.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:38:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:49:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:53:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:57:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:62:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:66:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:70:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:79:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:92:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:105:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:115:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:1:0: E0401: Unable to import 'werkzeug.security' (import-error)
users.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:19:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:27:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)

------------------------------------------------------------------
Your code has been rated at 7.82/10 (previous run: 7.82/10, +0.00)
```

Käydään seuraavaksi läpi tarkemmin raportin sisältö ja perustellaan, miksi kyseisiä asioita ei ole korjattu sovelluksessa.

## Docstring-ilmoitukset

Suuri osa raportin ilmoituksista on seuraavan tyyppisiä ilmoituksia:

```
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
```

Nämä ilmoitukset tarkoittavat, että moduuleissa ja funktioissa ei ole docstring-kommentteja. Sovelluksen kehityksessä on tehty tietoisesti päätös, ettei käytetä docstring-kommentteja.

## Import-ilmoitukset

Raportissa on seuraavat ilmoitukset liittyen `import`-komentoihin:

```
app.py:5:0: E0401: Unable to import 'flask' (import-error)
app.py:6:0: E0401: Unable to import 'flask' (import-error)
db.py:2:0: E0401: Unable to import 'flask' (import-error)
users.py:1:0: E0401: Unable to import 'werkzeug.security' (import-error)
```

Pylint antaa jostain syystä nämä ilmoitukset, vaikka Flask-kirjasto on asennettu kehitysympäristössä. Nämä ilmoitukset eivät haittaa, koska `import`-komennot toimivat sovelluksessa.

## Tarpeeton else

Raportissa on seuraavat ilmoitukset liittyen `else`-haaroihin:

```
app.py:264:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:301:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
users.py:27:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
```

Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa koodia:

```python
if "remove" in request.form:
    items.remove_item(item_id)
    return redirect("/")
else:
    return redirect("/item/" + str(item_id))
```

Tämä koodi olisi mahdollista kirjoittaa seuraavasti tiiviimmin:

```python
if "remove" in request.form:
    items.remove_item(item_id)
    return redirect("/")
return redirect("/item/" + str(item_id))
```

Kuitenkin sovelluksen kehittäjän näkemyksen mukaan tällaisissa tapauksissa on selkeämpää kirjoittaa `else`-haara, koska se tuo esille kaksi vaihtoehtoa, miten koodi voi toimia eri tilanteissa.

## Puuttuva palautusarvo

Raportissa on seuraavat ilmoitukset liittyen funktion palautusarvoon:

```
app.py:250:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:292:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```

Nämä ilmoitukset liittyvät tilanteeseen, jossa funktio käsittelee metodit `GET` ja `POST` mutta ei muita metodeja. Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa funktiota:

```python
@app.route("/remove_item/<int:item_id>", methods=["GET", "POST"])
def remove_item(item_id):
    require_login()

    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_item.html", item=item)

    if request.method == "POST":
        check_csrf()
        if "remove" in request.form:
            items.remove_item(item_id)
            return redirect("/")
        else:
            return redirect("/item/" + str(item_id))
```

Tässä funktio palauttaa arvon, kun `request.method` on `GET` tai `POST`, mutta periaatteessa voisi tulla tilanne, jossa `request.method` on jotain muuta eikä koodi palauttaisi arvoa. Käytännössä tällainen tilanne ei ole kuitenkaan mahdollinen, koska funktion dekoraattorissa on vaatimus, että metodin tulee olla `GET` tai `POST`. Niinpä tässä tapauksessa ei ole riskiä, että funktio ei jossain tilanteessa palauttaisi arvoa.

## Vakion nimi

Raportissa on seuraava ilmoitus liittyen vakion nimeen:

```
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
```

Tässä koodin päätasolla määritelty muuttuja tulkitaan vakioksi, jonka nimen tulisi olla kirjoitettu suurilla kirjaimilla. Kuitenkin sovelluksen kehittäjän näkemyksen mukaan tässä tilanteessa näyttää paremmalta, että muuttujan nimi on pienillä kirjaimilla. Muuttujaa käytetään koodissa näin:

```python
app.secret_key = config.secret_key
```

## Vaarallinen oletusarvo

Raportissa on seuraavat ilmoitukset liittyen vaaralliseen oletusarvoon:

```
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```

Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa funktiota:

```python
def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()
```

Tässä parametrin oletusarvo `[]` on tyhjä lista. Tässä ongelmaksi voisi tulla, että sama oletusarvona oleva tyhjä listaolio on jaettu kaikkien funktion kutsujen kesken ja jos jossain kutsussa listan sisältöä muutettaisiin, tämä muutos näkyisi myös muihin kutsuihin. Käytännössä tässä tapauksessa tämä ei kuitenkaan haittaa, koska koodi ei muuta listaoliota.
