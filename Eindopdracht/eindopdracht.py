import os, time

loader = 0

def beginverhaal():
    print("xd")


gameRunning = True

print("--------------------------------------------------------------------------------")
print("Hallo! Dit is mijn vluchteling Simulator!")
print("De bedoling van het spel is dat je ervaart hoe het voelt om een vluchteling \nte zijn.")
print("Het spel werkt als volgt. Je hebt meer keuzen vragen en aan de hand wat je hebt geantwoordt, krijg je andere eindes en scenario's.")
print("--------------------------------------------------------------------------------")
time.sleep(1)
print("\n\n\nAls je wilt beginnen klick op 'ENTER'!")

answer0 = input()

if answer0 == "":
    print("XD")
    os.system("clear")

    
while loader < 5:
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

os.system("clear")

#while gameRunning == True:
    
