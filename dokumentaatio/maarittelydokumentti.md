# Connect4 Määrittelydokumentti
#####Eero Ranta, Tietojenkäsittelytieteiden kandinaatti
####Pelissä on klassikkopeli, jossa pelaajat vuorotellen tiputtavat oman värisiä palloja 7x6 ruudukkoon ja tarkoitus on saada omaa väriä neljä putkeen.
#####Ohjelmointikieli: Python
#####Osatut ohjelmointikielet: Python
#####Dokumentaation kieli: Suomi
### Käytetyt algoritmit: Minimax-algoritmi alpha-beta karsinnalla
Minimax algoritmia käytetään tekoälyn siirtojen valitsemiseen. Sen tarkoituksena on tutkia mahdollisista seuraavista muutamasta siirrosta paras mahdollinen ja pelata se. Minimax algoritmi toimii hyvin tähän peliin, sillä kyseessä on ns. zero sum game, missä toisen pelaajan etu on toisen pelaajan haitta. Minimax laskee siis parhaimman mahdollisen siirron lopputuloksen olettaen, että vastustaja pelaa optimaalisesti.
####Algoritmin aikavaativuus: Minimax algoritmiin käytetty aika kasvaa exponentiaalisesti, jokaisen mahdollisen siirron jälkeen, joten se on O(n^2).
### Tietorakenteet: Matriisi taulukko pelitilanteesta
Matriisi taulukko pitää yllä vapaista paikoista pelinappuloille, ja missä mikäkin nappula sijaitsee.

####Lähteet: #####[Wikipedia](https://en.wikipedia.org/wiki/Minimax)
######[Tira-labra](https://tiralabra.github.io/2023_p4/fi/aiheet/minimax.pdf)
