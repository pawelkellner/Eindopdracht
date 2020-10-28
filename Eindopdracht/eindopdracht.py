import os, time

## Alle verhaal stukjes

def beginverhaal():
    os.system("cls")
    print("Je wordt wakker... Zoals altijd hoor je schoten en bommen in de achtergrond. Je mist je famillie heel erg, \nmaar je weet dat je sterk moet blijven en dat je niet moet opgeven. Je zat op deze dag zich lang voor te bereiden. \nJe weet dat dit je enige kans is voordat de terroristen weer terugkomen.")
    print("Je hoort iemand aankomen!")
    print("\n\n\nWat ga je doen?\nA: Alleen je telefoon en tas pakken en proberen te ontsnappen\nB: Alle spullen inpakken en proberen te ontsnappen")
    answer0 = input()

    if answer0 == "A":
        verhaalstukje14()
    elif answer0 == "B":
        verhaalstukje13()

def verhaalstukje5():
    os.system("cls")
    print("Je hebt gekozen ervoor om zich over te geven en met de terroristen mee te helpen want anders gaan ze je dood maken")
    print("\n\n\nOm door te gaan klick op 'ENTER'!")

    answer0 = input()

    if answer0 == "":
        print("")
    
    Einde1()
    

def verhaalstukje13():
    os.system("cls")
    print("Je hoort iemand al bij de deur. Je hebt geen genoeg tijd om er wat tegen te doen. Enige wat je kan doen is jezelf overgeven en helpen of uit het raam springen.")
    print("\n\n\nWat ga je doen?\nA: Je wacht tot ze binnen zijn \nB: je springt uit het raam")
    answer13 = input()

    if answer13 == "A":
        verhaalstukje5()
    elif answer13 == "B":
        verhaalstukje19()

def verhaalstukje19():
    os.system("cls")
    print("Je gooit alle spullen op de grond en je spring uit het raam...")
    print("Je wordt wakker je heb erg veel pijn aan je benen en bij het vallen ging er iets tegen je hoofd aan. Je ziet dat je ergens zit in een gebouw maar je weet niet waar je bent")
    print("Opeens loopt iemand naar binnen. Je hoort hem wat zeggen.")
    print("Je bent eindelijk wakker' zegt de man."
    print("'Wie ben je?' vraag je terwijl je heelveel kop pijn hebt.")
    print("'Ik ben Hamza. Ik zag je uit het raam springen toen je de terroristen probeerde ontsnappen, als ik er niet was zou je nu dood zijn.")
    
def Einde1():
    os.system("cls")
    print("                  EINDE")
    print("Je bent een van de terroristen geworden en nu kan je niet meer terug naar je famillie. Enige wat je kan doen is je famillie vergeten en een slechte leven hebben")
    print("\n\n\nOm door te gaan klick op 'ENTER'!")

    answer0 = input()

    if answer0 == "":
        print("")    

gameRunning = True

loader = 0

## Start spel / inleiding

print("--------------------------------------------------------------------------------")
print("Hallo! Dit is mijn Vluchteling Simulator!")
print("De bedoling van het spel is dat je ervaart hoe het voelt om een vluchteling \nte zijn.")
print("Het spel werkt als volgt. Je hebt meer keuzen vragen en aan de hand wat je hebt geantwoordt, krijg je andere eindes en scenario's.")
print("--------------------------------------------------------------------------------")
time.sleep(1)
print("\n\n\nAls je wilt beginnen klick op 'ENTER'!")

answer0 = input()

if answer0 == "":
    print("DD")

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
    print("Wil je het spel nog een keer spelen of wil je afsluiten?\n\n\n\nA: Afsluiten\nB: Spelen")
    antwoord = input()

    if antwoord == "A":
        break
    elif antwoord == "B":
        continue
