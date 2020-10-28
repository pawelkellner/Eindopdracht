import os, time

## Nodige functies

def Enterknop():
    time.sleep(1)
    print("\n\n\nOm door te gaan klick op 'ENTER'!")

    answer0 = input()

    if answer0 == "":
        print("")

    os.system("cls")



## Alle verhaal stukjes

def beginverhaal():
    os.system("cls")
    print("Je wordt wakker... Zoals altijd hoor je schoten en bommen in de achtergrond. Je mist je famillie heel erg, \nmaar je weet dat je sterk moet blijven en dat je niet moet opgeven. Je zat op deze dag zich lang voor te bereiden. \nJe weet dat dit je enige kans is voordat de terroristen weer terugkomen.")
    print("Je hoort iemand aankomen!")
    print("\n\n\nWat ga je doen?\n A: Alleen je telefoon en tas pakken en proberen te ontsnappen\n B: Alle spullen inpakken en proberen te ontsnappen")
    answer0 = input()

    if answer0 == "A":
        verhaalstukje14()
    elif answer0 == "B":
        verhaalstukje13()

def verhaalstukje3():
    os.system("cls")
    print("Je loopt naar binnen en je wordt direct door de mensen binnen geholpen. Je krijgt eten, drinken en een plek waar je kan slapen. Na een half kom je een man tegen en jullie beginnen te praten waarom jullie hier zijn en waar jullie heen willen. Na een heel lang gesprek eindigt de man het gesprek met een heel raar vraag 'Zou je ooit ISIS vergeven voor wat ze doen, als ze de oorlog zouden stoppen'")
    print("\n\n\n\Wat wil je zeggen?\n A: 'Nee, je kan nooit vergeven wat ze iedereen aan doen'\n B: 'Ja, want iedereen maakt fouten'")
    answer3 = input()

    if answer3 == "A":
        verhaalstukje11()
    elif answer3 == "B":
        verhaalstukje17()
    
    
def verhaalstukje5():
    os.system("cls")
    print("Je hebt gekozen ervoor om zich over te geven en met de terroristen mee te helpen want anders gaan ze je dood maken")
    Enterknop()
    
def verhaalstukje7():
    os.system("cls")
    print("Tijdens het afwachten help je Hamza met het regelen van een oplossing. Je loop het stad door dagen lang om te kijken of er iemand is die je kan helpen. Helaas na 2 weken vragen en zoeken heb je nog steeds niks, de volgende dag heb je \neindelijk iemand die je wilt helpen! Je hebt een afspraak gemaakt voor de volgende dag bij het huis van Hamza...")
    Enterknop()
    Einde2()

def verhaalstukje11():
    os.system("cls")
    print("De man loop weg zonder wat te zeggen, maar jij denkt er niks van want je bent heel moe en je wilt hier zo snel mogelijk weg.")
    Enternknop()
    Einde2()
    
def verhaalstukje12():
    os.system("cls")
    print("Je hebt gekozen om de volgende dag naar de smokkelaar te gaan. Je pakt al je spullen en je hebt een map van Hamza gekregen waar je naar toe moet gaan. Op de map zijn plekken gemarkeerd waar je kan overnachten, na een hele dag lopen zie je een plek waar je kan slapen maar hij is niet gemarkeerd op de map en de volgende is 2 uur verder.")
    print("\n\n\nWat ga je doen?\n A: Je loopt naar de volgende slaap plek\n B: Je blijft hier slapen")

    answer12 = input()

    if answer12 == "A":
        verhaalstukje6()
    elif answer12 == "B":
        verhaalstukje3()

def verhaalstukje13():
    os.system("cls")
    print("Je hoort iemand al bij de deur. Je hebt geen genoeg tijd om er wat tegen te doen. Enige wat je kan doen is jezelf overgeven en helpen of uit het raam springen.")
    print("\n\n\nWat ga je doen?\n A: Je wacht tot ze binnen zijn \n B: je springt uit het raam")
    answer13 = input()

    if answer13 == "A":
        verhaalstukje5()
    elif answer13 == "B":
        verhaalstukje19()

def verhaalstukje17():
    os.system("cls")
    print("De man loop weg zonder wat te zeggen, maar jij denkt er niks van want je bent heel moe en je wilt hier zo snel mogelijk weg.")
    Enterknop()
    Einde2()

def verhaalstukje19():
    os.system("cls")
    print("Je gooit alle spullen op de grond en je spring uit het raam...")
    print("Je wordt wakker, je hebt erg veel pijn aan je benen en bij het vallen ging er iets tegen je hoofd aan. Je ziet dat je \nergens zit in een gebouw maar je weet niet waar je bent")
    print("Opeens loopt iemand naar binnen. Je hoort hem wat zeggen.")
    time.sleep(15)
    print("Hamza: 'Je bent eindelijk wakker' zegt de man.")
    time.sleep(2)
    print("Ahmed: 'Wie ben je?' vraag je terwijl je heelveel kop pijn hebt.")
    time.sleep(2)
    print("Hamza: 'Ik ben Hamza. Ik zag je uit het raam springen toen je de terroristen probeerde ontsnappen, als ik er niet was zou je nu dood zijn.'")
    time.sleep(3)
    print("Ahmed: 'Dankjewel... Ik ben Ahmed, ik probeer bij me famillie in Nederland te komen maar ik weet niet waar ik heen moet. Kan je mij daar mee helpen.'")
    time.sleep(3)
    print("Hamza: 'Ik ken een paar mensen die over het grens smokkelen, maar het is erg gevaarlijk en het kost veel geld'")
    time.sleep(1)
    print("Ahmed: 'Is er niks anders wat ik kan doen?'")
    time.sleep(1)
    print("Hamza: 'Je kan nog hier blijven en dan kan ik mischien wat voor je regelen'")
    time.sleep(1)

    print("\n\n\nWat ga je doen?\n A: Een smokkelaar regelen\n B: Blijven een afwachten voor een beter oplossing")

    answer19 = input()

    if answer19 == "A":
        verhaalstukje12()
    elif answer19 == "B":
        verhaalstukje7()

## Eindes
    
def Einde1():
    os.system("cls")
    print("                  EINDE")
    print("Je bent een lid van ISIS geworden en nu kan je niet meer terug naar je famillie. Enige wat je kan doen is je famillie vergeten en een slechte leven hebben")
    Enterknop()

def Einde2():
    os.system("cls")
    print("                  EINDE")
    print("Je bent vermoordt in je slaap.")
    Enterknop()

## Start spel / inleiding

gameRunning = True

loader = 0

print("--------------------------------------------------------------------------------")
print("Hallo! Dit is mijn Vluchteling Simulator!")
print("De bedoling van het spel is dat je ervaart hoe het voelt om een vluchteling \nte zijn.")
print("Het spel werkt als volgt. Je hebt meer keuzen vragen en aan de hand wat je hebt geantwoordt, krijg je andere eindes en scenario's.")
print("--------------------------------------------------------------------------------")
time.sleep(1)
print("\n\n\nAls je wilt beginnen klick op 'ENTER'!")

answer0 = input()

if answer0 == "":
    print("")

os.system("cls")

## Laden animatie

while loader < 4:
    print("Aan het laden.")
    time.sleep(0.5)
    os.system("cls")
    print("Aan het laden..")
    time.sleep(0.5)
    os.system("cls")
    print("Aan het laden...")
    time.sleep(0.5)
    os.system("cls")
    loader = loader + 1

## "GAME ENGINE"

while gameRunning == True:
    beginverhaal()
    os.system("cls")
    print("Wil je het spel nog een keer spelen of wil je afsluiten?\n\n\n\n A: Afsluiten\n B: Spelen")
    antwoord = input()

    if antwoord == "A":
        break
    elif antwoord == "B":
        continue
