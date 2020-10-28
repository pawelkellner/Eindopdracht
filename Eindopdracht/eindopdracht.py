import os, time

## Alle verhaal stukjes

def beginverhaal():
    print("Je wordt wakker... Zoals altijd hoor je schoten en bommen in de achtergrond. Je mist je famillie heel erg, \nmaar je weet dat je sterk moet blijven en dat je niet moet opgeven. Je zat op deze dag zich lang voor te bereiden. \nJe weet dat dit je enige kans is voordat de terroristen weer terugkomen.")
    print("Je hoort iemand aankomen!")
    print("\n\n\nWat ga je doen?\nA: Alleen je telefoon en tas pakken\nB: Alle spullen inpakken en proberen te ontsnappen")
    answer0 = input()

    if answer0 == "A":
        verhaalstukje14()
    elif answer0 == "B":
        verhaalstukje13()

def verhaalstukje13():
    answer13 = input()

    if answer13 == "A":
        verhaalstukje5()
    elif answer13 == "B":
        verhaalstukje19()

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
