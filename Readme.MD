# Een scriptje voor het invullen van Silas' inschrijvingsformulier. 

## Enkele stappen vooraf:

### 1. Python installeren op je computer:

Het scriptje is opgesteld in de programmeertaal Python. Om het te laten werken moet je dit dus ook geïnstalleerd zijn op je computer. Als dit nog niet het geval is, kan je deze downloaden via:

- [Windows: Python 3.11.3](https://www.python.org/ftp/3.11.3/python-3.11.3-amd64.exe)
- [Mac: Python 3.11.3](https://www.python.org/downloads/release/python-3113/)

Of als je me niet vertrouwt, zoek je gewoon in Google naar Python, en zou helemaal bovenaan [Python.org](https://www.python.org/) moeten staan, en download je het zo.

Uiteraard na het downloaden niet vergeten te installeren (dit is redelijk vanzelfsprekend, dubbelklikken op wat je hebt gedownload, en een paar keer op volgende klikken).

### 2. Packages installeren
Het scriptje maakt gebruik van twee packages, nl. selenium en webdriver-manager, die worden gebruikt voor het automatiseren van de browser. 

Deze installeer je via de commandline (na Python te hebben geïnstalleerd in stap 1!)

Open de terminal van je computer, en geef volgende in:

(Indien je onvoldoende toegangsrechten hebt om onderstaande uit te voeren, moet je je terminal openen als administrator. In windows doe je dit door rechts te klikken op het icoontje van je terminal, en kiezen voor "run as adminstrator")

    pip install selenium

en

    pip install webdriver-manager

### 3. Chrome installeren
Dit scriptje werkt enkel met Chrome. Is deze browser niet op je computer geïnstalleerd, dan kan dit via deze [link](https://www.google.com/chrome)

## Het script zelf:

Na bovenstaande te hebben doorlopen, moet je het scriptje zelf laten lopen.

Voor Windows gebruikers:
1. Je gaat naar de locatie waar je het bestandje hebt geplaatst
2. Rechtermuisklik, open in terminal
3. In de terminal: `python .\main.py`

## Het resultaat

Gaat alles goed, dan opent chrome (het is niet nodig dat deze al openstaat, of dat je naar het formulier surft), en wordt het formulier ingevuld.

### Wat doet het wel, wat doet het (nog) niet:
Alles wordt aangeduid of ingevuld.

De submitknop moet je nog in deze versie nog manueel klikken. 
Ook dit kan automatisch, en is eigenlijk al voorzien. Maar dan kan je natuurlijk niets nazien, wat bij deze (proef)versie niet de bedoeling is.

Waarvoor kijk ik nog (mits tijd): De mogelijkheid om het scriptje iets voor 8u op te starten, en dat het zelf kijkt wanneer het 8u is, en dan pas verder gaat. Op deze manier hoef je zelf niet in de gaten te houden wanneer het precies 8u is, om dan pas het scriptje te laten lopen.

### Waar kan het mislopen?
Overal eigenlijk, ben curieus of het gaat werken.

Het scriptje zoekt op een aantal trefwoorden of -zinnen. Voordeel hiervan is dat de volgorde van de vragen mag wijzigen, nadeel is dat de inhoud van de vragen niet, of slechts beperkt mag wijzigen. 