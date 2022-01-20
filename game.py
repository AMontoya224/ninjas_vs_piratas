from classes.ninja import Ninja
from classes.pirate import Pirate
import random

print("\n---------------------")
print("| Ninjas vs Piratas |")
print("---------------------\n")

nombre_ninja = input("Introduzca su nombre: ")
ninja = Ninja(nombre_ninja)
enemigo = input("Piratas disponibles: \n(1) Barbanegra \n(2) Jack Sparrow \n(3) Henry Morgan \nA quien deseas enfrentar? ")

while True:
    if enemigo == "1":
        pirata = Pirate("Barbanegra", 20, 5, 80)
        break
    elif enemigo == "2":
        pirata = Pirate("Jack Sparrow", 10, 10, 120)
        break
    elif enemigo == "3":
        pirata = Pirate("Henry Morgan", 5, 15, 150)
        break
    else:
        enemigo = input("Selección inválida, elija nuevamente: ")

print("\n" + nombre_ninja.upper() + " ahora eres un ninja! Que comience la batalla.\n")
print("-----------------------------------------------------\n")

option = ""
while option != "4":
    option = input("Movimientos disponibles: \n(1) Ataque \n(2) Ataque crítico \n(3) Curarte \n(4) Terminar juego \nQue movimiento desea realizar? ")
    if option == "4":
        break

    if option == "1":
        ninja.attack(pirata)

    elif option == "2":
        ninja.criticAttack(pirata)
    
    elif option == "3":
        ninja.cure()
    else:
        print("Movimiento no disponible, pierdes un turno")
    
    randon = random.randrange(3)
    if randon == 0:
        pirata.attack(ninja)

    elif randon == 1:
        pirata.criticAttack(ninja)
    
    elif randon == 2:
        pirata.cure()

    print("\nRESULTADOS:\n")
    resultado1 = pirata.show_stats()
    resultado2 = ninja.show_stats()
    if resultado1 <= 0 or resultado2 <= 0:
        if resultado1 < resultado2:
            print("Ganaste la batalla!!!")
        else:
            print("Perdiste la batalla...")
        break

    print("-----------------------------------------------------\n")