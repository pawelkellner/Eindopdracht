import os, time

## Nodige functies

def Enterknop():
    time.sleep(1)
    print("\n\n\nOm door te gaan klick op 'ENTER'!")

    answer0 = input()

    if answer0 == "":
        print("")

    os.system("clear")



## Alle verhaal stukjes

def beginverhaal():
    os.system("clear")
    print("Je wordt wakker... Zoals altijd hoor je schoten en bommen in de achtergrond. Je mist je famillie heel erg, \nmaar je weet dat je sterk moet blijven en dat je niet moet opgeven. Je zat op deze dag zich lang voor te bereiden. \nJe weet dat dit je enige kans is voordat de terroristen weer terugkomen.")
    print("Je hoort iemand aankomen!")
    print("\n\n\nWat ga je doen?\n A: Alleen je telefoon en tas pakken en proberen te ontsnappen\n B: Alle spullen inpakken en proberen te ontsnappen")
    answer0 = input()

    if answer0 == "A":
        verhaalstukje14()
    elif answer0 == "B":
        verhaalstukje13()

def verhaalstukje1():
    os.system("clear")
    print("De groepjes willen in 2 groepjes gaan omdat ze andere routes willen nemen. Je kan of met Ali of met Mohamed gaan")
    print("\n\n\nWat ga je doen?\n A: Je gaat met Ali\n B: Je gaat met Mohamed")
    answer1 = input()

    if answer1 == "A" or answer1 == "B":
        verhaalstukje4()

def verhaalstukje2():
    os.system("clear")
    print("Je komt een groepje mensen tegen die naar een smokkelaar gaan om naar Nederland te gaan. Je kan met het gropje mee gaan of op je zelf de weg te vinden")
    print("\n\n\nWat ga je doen?\n A: Je vraagt voor aanwijzingen een je gaat alleen door\n B: Je probeerd op je zelf het weg te vinden \nC: Je gaat met het groepje mee")
    answer2 = input()

    if answer2 == "A":
        verhaalstukje18()
    elif answer2 == "B":
        verhaalstukje21()
    elif answer2 == "C":
        verhaalstukje1()

def verhaalstukje3():
    os.system("clear")
    print("Je loopt naar binnen en je wordt direct door de mensen binnen geholpen. Je krijgt eten, drinken en een plek waar je kan slapen. Na een half kom je een man tegen en jullie beginnen te praten waarom jullie hier zijn en waar jullie heen willen. Na een heel lang gesprek eindigt de man het gesprek met een heel raar vraag 'Zou je ooit ISIS vergeven voor wat ze doen, als ze de oorlog zouden stoppen'")
    print("\n\n\nWat wil je zeggen?\n A: 'Nee, je kan nooit vergeven wat ze iedereen aan doen'\n B: 'Ja, want iedereen maakt fouten'")
    answer3 = input()

    if answer3 == "A":
        verhaalstukje11()
    elif answer3 == "B":
        verhaalstukje17()

def verhaalstukje4():
    os.system("clear")
    print("Jullie komen elkaar weer tegen bij het kust waar de smokkelaar zit. Jullie besluiten om 1 groep te maken zodat iedereen veiliger is. Je kan kiezen of je met de boot gaat of je via de grens in een vrachtwagen gaat.")
    print("\n\n\nWat ga je doen?\n A: Met de boot\n B: Met de vrachtwagen")
    answer4 = input()

    if answer4 == "A":
        verhaalstukje10()
    if answer4 == "B":
        verhaalstukje8()
    
def verhaalstukje5():
    os.system("clear")
    print("Je hebt gekozen ervoor om zich over te geven en met de terroristen mee te helpen want anders gaan ze je dood maken")
    Enterknop()
    Einde1()

def verhaalstukje6():
    os.system("clear")
    print("Je komt bij de veilige slaap plek. Je wordt binnen geholpen, je krijgt eten en drinken. Je hoort dat andere ook met de smokkelaar mee gaan. Er zijn 2 groepjes. Je kan of met Mohamed gaan of met Ali gaan.")
    print("\n\n\nWat ga je doen?\n A: Je gaat mee met Mohamed\n B: Je gaat mee met Ali")
    answer6 = input()

    if answer6 == "A":
        verhaalstukje4()
    elif answer6 == "B":
        verhaalstukje4()
    
def verhaalstukje7():
    os.system("clear")
    print("Tijdens het afwachten help je Hamza met het regelen van een oplossing. Je loop het stad door dagen lang om te kijken of er iemand is die je kan helpen. Helaas na 2 weken vragen en zoeken heb je nog steeds niks, de volgende dag heb je \neindelijk iemand die je wilt helpen! Je hebt een afspraak gemaakt voor de volgende dag bij het huis van Hamza...")
    Enterknop()
    Einde2()

def verhaalstukje8():
    os.system("clear")
    print("Je gaat naar de smokkelaar en vraagt of je met de vrachtwagen kan zodat  het veiliger is, maar je hoort van hem dat het al vol zit en dat je met de boot alleen kan gaan.")
    Enterknop()
    verhaalstukje10()

def verhaalstukje9():
    os.system("clear")
    print("Na de 2 dagen gaan jullie met de kleine boot richting Nederland. Je komt bent in Nederland! Ali wilt naar de vluchtelingenkamp gaan en daar afwachten, maar Mohamed zegt dat hij iemand kent die een verblijfsvergunning kan regelen en dan hoef je niet zo lang te wachten.")
    print("\n\n\nWat ga je doen?\n A: Je gaat met Mohamed mee\n B: Je gaat met Ali mee")
    answer9 = input()

    if answer9 == "A":
        verhaalstukje20()
    elif answer9 == "B":
        verhaalstukje16()
    

def verhaalstukje10():
    os.system("clear")
    print("Je gaat met de boot. De reis gaat over 2 dagen weg. Wil extra geld proberen te verdienen in die 2 dagen om met een beter boot te gaan?")
    print("\n\n\nWat ga je doen?\n A: Nee, je wacht de vertrek tijd af\n B: Je gaat extra verdienen")
    answer10 = input()

    if answer10 == "A":
        verhaalstukje9()
    elif answer10 == "B":
        verhaalstukje15()

def verhaalstukje11():
    os.system("clear")
    print("De man loop weg zonder wat te zeggen, maar jij denkt er niks van want je bent heel moe en je wilt hier zo snel mogelijk weg.")
    Enterknop()
    Einde2()
    
def verhaalstukje12():
    os.system("clear")
    print("Je hebt gekozen om de volgende dag naar de smokkelaar te gaan. Je pakt al je spullen en je hebt een map van Hamza gekregen waar je naar toe moet gaan. Op de map zijn plekken gemarkeerd waar je kan overnachten, na een hele dag lopen zie je een plek waar je kan slapen maar hij is niet gemarkeerd op de map en de volgende is 2 uur verder.")
    print("\n\n\nWat ga je doen?\n A: Je loopt naar de volgende slaap plek\n B: Je blijft hier slapen")

    answer12 = input()

    if answer12 == "A":
        verhaalstukje6()
    elif answer12 == "B":
        verhaalstukje3()

def verhaalstukje13():
    os.system("clear")
    print("Je hoort iemand al bij de deur. Je hebt geen genoeg tijd om er wat tegen te doen. Enige wat je kan doen is jezelf overgeven en helpen of uit het raam springen.")
    print("\n\n\nWat ga je doen?\n A: Je wacht tot ze binnen zijn \n B: je springt uit het raam")
    answer13 = input()

    if answer13 == "A":
        verhaalstukje5()
    elif answer13 == "B":
        verhaalstukje19()

def verhaalstukje14():
    os.system("clear")
    print("Je hebt net op tijd weg kunnen gaan. Je rent verder weg zodat ze niet achter je kunnen aankomen. Onderweg kom je mensen tegen...")
    Enterknop()
    verhaalstukje2()

def verhaalstukje15():
    os.system("clear")
    print("Je hebt besloten om andere te helpen en wat bij te verdienen. Na de 2 dagen heb je heel weinig bij verdient maar wel iets. Je bent heel moe na de hele dag anderen helpen, je gaat slapen......")
    Enterknop()
    Einde3()

def verhaalstukje16():
    os.system("clear")
    print("Je hebt besloten om met Ali mee te gaan naar het vluchtelingenkamp.")
    Enterknop()
    Einde5()
    
def verhaalstukje17():
    os.system("clear")
    print("De man loop weg zonder wat te zeggen, maar jij denkt er niks van want je bent heel moe en je wilt hier zo snel mogelijk weg.")
    Enterknop()
    Einde2()

def verhaalstukje18():
    os.system("clear")
    print("Je hebt het weg naar de smokkelaar kunnen vinden. Je hoort dat je met de boot of met een vrachtwagen kan gaan")
    print("\n\n\nWat doe je?\n A: Je gaat met de boot\n B: Je gaat met de vrachtwagen")
    answer18 = input()

    if answer18 == "A":
        verhaalstukje10()
    elif answer18 == "B":
        verhaalstukje8()

def verhaalstukje19():
    os.system("clear")
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

def verhaalstukje20():
    os.system("clear")
    print("Je hebt besloten om met Mohamed te gaan. De volgende dag heeft hij voor jou een verblijfsvergunning die 30 jaar geldig is. Je hebt je famillie kunnen vinden en je eindelijk veilig in Nederland")
    Enterknop()
    Einde4()

def verhaalstukje21():
    os.system("clear")
    print("Je loop al 3 dagen en je hebt geen idee waar je bent. Al je eten en drinken is op en je weet niet wat je moet doen, je loopt door en hoop dat je iemand tegenkomt...")
    Enterknop()
    Einde6()

## Eindes
    
def Einde1():
    os.system("clear")
    print("                  EINDE")
    print("Je bent een lid van ISIS geworden en nu kan je niet meer terug naar je famillie. Enige wat je kan doen is je famillie vergeten en een slechte leven hebben")
    Enterknop()

def Einde2():
    os.system("clear")
    print("                  EINDE")
    print("Je bent vermoordt in je slaap.")
    Enterknop()

def Einde3():
    os.system("clear")
    print("                  EINDE")
    print("Je hebt je voor de boot verslapen en je bent opgepakt door ISIS")
    Enterknop()

def Einde4():
    os.system("clear")
    print("                  EINDE")
    print("Je bent met je famillie in Nederland")
    Enterknop()

def Einde5():
    os.system("clear")
    print("                  EINDE")
    print("Je zit al 5 jaar in de vluchtelingenkamp en je weet nog steeds niet wanneer je je famillie weer zult zien")
    Enterknop()

def Einde6():
    os.system("clear")
    print("                  EINDE")
    print("Je bent dood gegaan door honger en dorst")
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

os.system("clear")

## Laden animatie

while loader < 4:
    print("Aan het laden.")
    time.sleep(0.5)
    os.system("clear")
    print("Aan het laden..")
    time.sleep(0.5)
    os.system("clear")
    print("Aan het laden...")
    time.sleep(0.5)
    os.system("clear")
    loader = loader + 1

## "GAME ENGINE"

while gameRunning == True:
    beginverhaal()
    os.system("clear")
    print("Wil je het spel nog een keer spelen of wil je afsluiten?\n\n\n\n A: Afsluiten\n B: Spelen")
    antwoord = input()

    if antwoord == "A":
        break
    elif antwoord == "B":
        continue
