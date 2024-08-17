from random import randint
from time import sleep
from data import player, enemies
from helpers import fight, display_enemy, display_player, training, shop, inventory

name = input('Введи своё имя, путник: ')
player['name'] = name
current_enemy = 0

choice = input("Выберите действие: ")
while choice != "quit" and player["hp"] > 0:
    if choice == "1":
        fight(current_enemy)
    elif choice == "2":
        current_enemy += 1
        if current_enemy == len(enemies):
            current_enemy = 0
        print("Выбранный противник:", enemies[current_enemy]["name"])
    elif choice == "3":
        display_enemy(current_enemy)
    elif choice == "4":
        display_player()
    elif choice == "5":
        training("armor")
    elif choice == "6":
        training("attack")
    elif choice == "7":
        shop()
    elif choice == "8":
        inventory()
    choice = input("Выберите действие: ")
print("GAME OVER")