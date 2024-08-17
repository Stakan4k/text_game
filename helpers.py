from time import sleep
from random import randint
from data import player, enemies, items

def fight(current_enemy):
    round = randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]['hp']
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    input('Enter чтобы продолжить')
    print()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            choice = input("1 - меч\n2 - Фаербол\n3 - Карманная кража\n4 - выстрел")
            if choice == "1":
                enemy_hp -= player['attack']
            elif choice == "2":
                enemy_hp -= player['attack']/100*enemy_hp
            elif choice == "3":
                amount = player['luck']/100*enemy["money"]
                player["money"] += amount
                enemy["money"] -=amount
            elif choice == "4":
                if player["luck"] >= randint(0, 100):
                    enemy_hp -= player['attack']*3
                    print("ХЕАДШОТ")
                else:
                    enemy_hp -= player['attack']*0.7
            sleep(1)
            print(f'''{player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}.')
            player['hp'] -= enemy['attack']*player["armor"]
            sleep(1)
            print(f'''{player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            sleep(1)
        round += 1

    if player['hp'] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
        
def display_enemy(current_enemy):
    print()
    print("Имя:", enemies[current_enemy]["name"])
    print("Атака:", enemies[current_enemy]["attack"])           
    print("Здоровье:", enemies[current_enemy]["hp"])
    print()

def display_player():
    print()
    print("Имя:", player["name"])
    print("Атака:", player["attack"])           
    print("Здоровье:", player["hp"])
    print()

def training(type):
    for i in range(0, 101, 20):
        print(f"Тренеровка завершена на {i}%")
        sleep(1)
    if type == "armor":
        player["armor"] -= 0.05
        print(f"Ваша броня: {player ['armor']}")
    elif type == "attack":
        player["attack"] += 5
        print(f"Ваша атака: {player ['attack']}")

def shop():
    for item in items:
        print(item["name"], "-", item["cost"])
        if "luck" in item:
            print(f"{item['luck']} к удаче")
        if "armor" in item:
            print(f"{item['armor']*100}% к входящему урону")
        if "hp" in item:
            print(f"{item['hp']*100} к здоровью")
        if "attack" in item:
            print(f"{item['attack']*100} к урону")
    print(f"Баланс: [player{"money"}]")
    choice = int(input("Выберите предмет(1,2,3...)"))
    if choice >= len(items):
        choice = len(items)-1
    if choice < 1:
        choice = 1
    if items [choice-1]["cost"] > player["money"]:
        print("Не хватает денег")
    else:
        player["money"] -= items[choice-1]["cost"]
        player["inventory"].append(items[choice-1])
        print(f"Вы купили {items[choice-1]["name"]}")

def inventory():
    for item in player["inventory"]:
        print(item["name"], "-", item["cost"])
        if "luck" in item:
            print(f"{item['luck']} к удаче")
        if "armor" in item:
            print(f"{item['armor']*100}% к входящему урону")
        if "hp" in item:
            print(f"{item['hp']*100} к здоровью")
        if "attack" in item:
            print(f"{item['attack']*100} к урону")    
        if item["mode"] == "unequipment":
            print("Не эквипереван")
        if item["mode"] == "equipment":
            print("Эквипириван")

    choice = int(input("Выберите предмет(1,2,3...)"))
    if choice >= len(items):
        choice = len(items)-1
    if choice < 1:
        choice = 1 
    item = player["inventory"][choice-1]
    if item["mode"] == "unequipment":
        item["mode"] == "equipment"
        if "luck" in item:
            player["luck"] -= item["luck"]
        if "armor" in item:
            player["armor"] -= item["armor"]
        if "hp" in item:
            player["hp"] -= item["hp"]
        if "attack" in item:
            player["attack"] -= item["attack"]
    if item["mode"] == "single":
        if "luck" in item:
            player["luck"] -= item["luck"]
        if "armor" in item:
            player["armor"] -= item["armor"]
        if "hp" in item:
            player["hp"] -= item["hp"]
        if "attack" in item:
            player["attack"] -= item["attack"]
        del player["inventory"][choice-1]
        