# Toteutusdokumentti

## Ohjelman rakenne
Ohjelman koodi löytyy src hakemistosta. Tiedostoista löytyvät luokat GameController, GameBoard, Ai, EventQueue. GameController luokka vastaa ohjelman pyörittämisestä ja pelin kulusta.
GameBoard hallitsee pelilaudan ylläpitämisestä mm. voittojen tarkastelu ja pelilaudalle nappuloiden asettaminen. Ai vastaa tekoälyn liikkeiden valitsemisesta. EventQueue kysyy pelaajan syötteitä.

## Aika- ja tilavaatimukset
Ai luokan käyttämä minimax algoritmi, jota käytetään parhaimman siiron löytämiseen toimii aikavaatimuksessa O(n^d), missä n on mahdollisten siirtojen määrä tilanteessa ja d on algoritmin käyttämä syvyys (kuinka pitkälle pelitilanteiden puuta lasketaan).
Tilavaativuus on O(nd).

## Parannusehdotukset
Minimax-algotimia voitaisiin tehdä nopeammaksi optimoimalla algoritmiä siten, että se hylkää toivottomia pelipolkuja ja ei laske niitä eteenpäin. Myöskin heuristiikka funktiosta voitaisiin tehdä parempi, jotta Ai osaisi pelata optimaalisia liikkeitä, silloin kun se ei löydä pakotettua voittoa.
