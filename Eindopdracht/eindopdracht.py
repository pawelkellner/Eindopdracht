import os, time

def beginverhaal():
    print("Je wordt wakker... Zoals altijd hoor je schoten en bommen in de achtergrond.")
    

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
    print("DD")

os.system("cls")

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

while gameRunning == True:
    beginverhaal()
