# Sintaktični denormalizator

Sintaktični denormalizator oblikuje golo besedilo, ki je v celoti zapisano s črkovnimi znaki, v lažje berljivo obliko, kjer so besede, ki so tipično zapisane z nečrkovnimi znaki ali v krajši obliki primerno spremenjene (npr. ure, datumi, simboli, okrajšave).


## Uporaba:

Glavna metoda se nahaja v datoteki ```denormalize.py```, kliče pa se z uporabo `denormalize(inp, config="default")`.



## Vhodno besedilo

Podprti so trije tipi vhodnega besedila.

#### Niz

Vhod je lahko niz znakov, na primer: ```"Danes je lep sončen dan.```

#### Seznam

Če želite uporabiti drugačen tokenizator ali imate besedilo že tokenizirano, je lahko vhod v normalizator seznam tokenov, na primer:

```["Danes",  "je",  "lep",  "sončen",  "dan",  "."]```

#### Slovar

Če želite denormalizirati besedilo, ki ima dodane elemente, je lahko vhod slovar (dictionary). Struktura mora biti sledeča:

```
[
  {
    "text":"Danes"
  },
  {
    "text":"je"
  },
  {
    "text":"lep"
  },
  {
    "text":"dan"
  }
]
```

Dodatno lahko vhodnemu besedilu v takšni obliki dodate še polji ```startTime``` in ```endTime```. Ta dva parametra vplivata na denormalizacijo zaporednih števil, kjer je več možnih rezultatov.

```
[
    {
      "text":"Danes",
      "startTime":0.67,
      "endTime":1.23
    },
    {
      "text":"je",
      "startTime":1.24,
      "endTime":1.34
    },
    {
      "text":"lep",
      "startTime":1.89,
      "endTime":2.03
    },
    {
      "text":"dan",
      "startTime":2.24,
      "endTime":2.78
    }
  ]
```
V primeru več zaporednih števil, kjer je možnih več načinov denormalizacije (na primer: "dva tisoč tri tisoč"), bodo v primeru, da ni podatka o začetnem in končnem času izgovora besede, številke konstruirano linearno (2003 1000). Če so ti podatki podani, bodo števila razdeljena tam, kjer je med dvema tokenoma večji premor. Na primer:

 "dva tisoč (0.03 s premora) tri (0.02 s premora) tisoč" -> "2000 3000"

### Nastavitve

Izberete lahko med tremi različnimi prednastavljenimi sklopi nastavitev, in sicer ```default```, ```technical``` in ```everyday```.

Denormalizator uporablja 10 nastavitev.



Nastavitev ```punct_is_included``` (prednastavljeno ```False```) nastavimo, ali besedilo, ki ga denormaliziramo, vsebuje ločila ali ne. To vpliva na denormalizacijo nekaterih kategorij.

Z nastavitvijo ```include_slash``` (prednastavljeno ```False```, technical: ```True```) izberemo, ali naj se številke in enote združijo v en sam token, če je to primerno (na primer: 120 skozi 80 -> 120/80; kilometrov na uro -> km/h).

Z nastavitvijo ```include_numbers``` (prednastavljeno ```True```) izberemo, ali naj se številke denormalizirajo.

Z nastavitvijo ```include_numbers_part_token``` (prednastavljeno ```True```) izberemo, ali naj se normalizirajo števila, ki so del besed (na primer: enajstletni -> 11-letni).

Nastavitev ```include_units``` (prednastavljeno ```True```, everyday: ```False```) vpliva na to, ali se merske enote denormalizirajo v pripadajočo okrajšavo oziroma simbol.

Vključene so naslednje enote: meter, gram, liter, tona, bar, newton, kelvin, herc, joule, stopinja, Celzija, promil, odstotek, procent, evro, dolar; in naslednje predpone: piko, nano, mikro, mili, centi, deci, deka, hekto, kilo, mega, giga, tera.

Nastavitev ```include_email``` (prednastavljeno ```True```) se nanaša na e-naslove z domeno ".si" in ".com".

Z nastavitvijo ```include_title``` (prednastavljeno ```True```) izberemo, ali naj se nazivi zapišejo kot okrajšave.

Vključeni so naslednji nazivi: doktor/-ica, profesor/-ica, diplomiran/-a, gospa, gospodična, gospod, docent, specialist/-ka, primarij/-ka, magister/-ica, redni, izredni, univerzitetni.

Nastavitev ```includeAbbr``` (prednastavljeno ```True```) vpliva na okrajšave, ki niso zajeti v kategoriji "nazivi".

Vključene so naslednje okrajšave: oziroma, in tako dalje, in tako naprej, in podobno, tako imenovan.

Z nastavitvijo ```include_stylistic``` (prednastavljeno ```True```, technical: ```False```) izberemo, ali naj se uveljavijo stilistične spremembe (npr: številke, manjše od 11, ki jim ne sledi merska enota, bodo zapisane z besedo, ne s ciframi).

Nastavitev ```proper_tokenization``` (prednastavljeno ```True```) tokenizira niz znakov. Nastavite na ```False```, če za anotiranje uporabljate posebne znake, ki morda ne bodo pravilno tokenizirani. Če je nastavljeno na  ```False```, se vhodni niz loči na praznem prostoru (whitespace).

Če ni podanih drugih nastavitev, se uporabi konfiguracijska datoteka ```default```.


## Nastavitve

Če ni podanih drugih nastavitev, se uporabi konfiguracijska datoteka ```default```.

Pod parameter ```custom_config``` lahko specificirate, katere nastavitve naj se upoštevajo pri denormalizaciji.

Izberete lahko katerega od prednastavljenih sklopov nastavitev, in sicer tako, da kot ```custom_config``` definirate ime sklopa v obliki niza, na primer ```custom_config="technical"```.

Če želite spremeniti posamezne parametre, lahko kot ```custom_config``` definirate slovar s posameznim parametrom, na primer:

```custom_config={"include_numbers": False}```. Za vse ostale nastavitve, ki v parametru ```custom_config``` niso definirane, se uporabijo nastavitve iz konfiguracijske datoteke ```default```.

## Izhod

Denormalizator vrne slovar, ki je sestavljen iz denormalizirane povedi pod poljem ```denormalized_string``` in denormalizirane vsebine pod poljem ```denormalized_content```.

Pllje "denormalized_string" vrne normalizirano besedilo v obliki niza, če je bilo vhodno besedilo v obliki niza, sicer vrne ```None```.

Denormalizirana vsebina je seznam vseh denormaliziranih tokenov. Vsak token je v obliki slovarja in vsebuje polji ```text```, ki je denormalizirano besedilo, in ```index```, ki je seznam indexov tokenov v izvirnem besedilu.

Primer rabe: 

```denormalize("Danes, osmega sedmega dva tisoč dvaindvajset, je lep sončen dan, saj je zunaj prijetnih petindvajset stopinj Celzija.")```

Izhod:
```
{'denormalized_content': [{'text': 'Danes', 'index': [0]}, {'text': ',', 'index': [1]}, {'text': '8.', 'index': [2]}, {'text': '7.', 'index': [3]}, {'text': '2022', 'index': [4, 5, 6]}, {'text': ',', 'index': [7]}, {'text': 'je', 'index': [8]}, {'text': 'lep', 'index': [9]}, {'text': 'sončen', 'index': [10]}, {'text': 'dan', 'index': [11]}, {'text': ',', 'index': [12]}, {'text': 'saj', 'index': [13]}, {'text': 'je', 'index': [14]}, {'text': 'zunaj', 'index': [15]}, {'text': 'prijetnih', 'index': [16]}, {'text': '25', 'index': [17]}, {'text': '°C', 'index': [18, 19]}, {'text': '.', 'index': [20]}], 'denormalized_string': 'Danes, 8. 7. 2022, je lep sončen dan, saj je zunaj prijetnih 25 °C.'}
```