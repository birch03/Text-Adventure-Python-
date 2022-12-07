#Author: Quinn Stone
#Project: A5 CSCI 141
#Date: 3/2/22
import time
import random
import math

#Start adventure
def main():
    #Sets up health file and writes into it
    f = open("health.txt", "w")
    f.write("30")
    f.close()
    f = open("health.txt", "r")
    main.health = f.read()
    f.close()
    #Creates stats [health, damage]
    main.stats = [int(main.health), 5, "helper?"]
    #Start Adventure in full, Name?
    main.name = input("What is the name of your adventurer?")
    
    print("You awaken under a single large oak tree in the middle of a vast open field. As you are getting up you remember who you are. You are",main.name,"with",main.health,"health and you deal", main.stats[1],"damage. As you look around you see a man fade into the distance. There are two paths you see before you.")
    print()
    print("To your left you see a dark forest with a gloomy aura around it.")
    print("Straight ahead you can see far on the horizon a small house utop a hill.")
    
    choice = input("What path do you choose? (r/s)")
    print()
    #What happens to them
    if choice == "r":
        forest()
    elif choice == "s":
        house()
    else:
        print("You decide to take neither of the choices before you and instead settle down where you are. Rather boring end huh?")
        exit()

def house():
    print()
    main.stats[0] = main.stats[0]+5
    
    print("You decide to head towards the house. As you apporach you realize that is has been abandoned for years. Opening the door you see a dark room with a packet or chips. You eat them gaining 5 health. You now have", main.stats[0],"health")
    print("You continue snooping around and find a lone sword with a pile of bones around it.")
    
    choice=""
    choice = input("Do you take it or leave it alone? (take/leave)")
    if choice == "take":
        #Updates stats of character (0=health, 1=damage)
        main.stats[0] = main.stats[0]-20
        main.stats[1] = main.stats[1]+17
        print()
        print("As you take the sword into your hand you can feel its power. You hold it up to get a better look and instantly pain overcomes you; You feel weaker, much weaker than before but now weild this powerful weapon.")
        print("You take 20 damage and have",main.stats[0],"health left, but the power of your weapon increases your damage by 17 and now deal", main.stats[1],"damage.")
    elif choice == "leave":
        print()
        print("You decide to leave the sword alone, fearing the fate of the dead around it may happen to you.")
    else:
        print()
        print("Invalid choice, you decide to stay in the house for all eternity")
        exit()
    print()
    #Using choice2 because already used variable choice one before in this function
    choice2 = input("After resting in the house for a while you leave out the back door and see off in the distance a town to your right, and a castle to your left. Which will you journey to? (castle/town)")
    if choice2 == "town":
        town()
    elif choice2 == "castle":
        castle()
    else:
        #dummies
        print()
        print("Invalid choice, you decide to stay in the house for all eternity")
        exit()

def town():
    print("As you make your way towards the town you see a ploom of smoke rising up from the nearby forest. You decide to investigate and find nobody at the lit fire.")
    choice = input("You feel a big uneasy in this dark forest, the only sound that is heard is that of the crackling fire. Do you wait to see who shows up or leave and continue onto the town? (wait/leave)")
    if choice == "wait":
        wait()
        exit()
    if choice == "leave":
        print()
        print("You decide to leave and live a simple life and settle down in a small town filled with nice people.")
        print()
        print("The End")
        exit()
        
        #This gave me a bit of trouble for some reason
    elif choice != "wait" or choice != "leave":
        print("Invalid response, God smites you for your misdeeds")
        exit()

def forest():
    print("Your curiocity gets the better of you and you wander alone into the dark forest.")
    print("It is dead quiet but every so often you can hear a faint noise calling your name")
    print('"',main.name,'..."',sep="")
    print("You look around but see nothing. As you continue on your way you stuble across a still lit fire. There is a sword laying on a log.")
    choice = ""
    while True:
        choice = input("Do you take the sword and run, or wait for the stranger to return? (run/wait)")
        if choice == "run":
            run()
            break
        elif choice == "wait":
            wait()
            break
        else:
            print("Invalid answer, try again")
def run():
    print()
    print("You decide to take the sword, gaining 3 attack power, and run away, while you are running you stumble over a tree branch and take 5 damage.")
    #Updating character stats
    main.stats[0] = main.stats[0]-5
    main.stats[1] = main.stats[1]+3
    
    #update health.txt
    write_health()
    
    print("You have",main.stats[0],"health left")
    print()
    print("As you slowly make your way through the forest you see a clearing. You head towards it and see a Castle on a hill...")
    castle()

def wait():
    print()
    #Adds helper as damage
    main.stats[2]="helper"
    main.stats[1]=main.stats[1]+5
    print("You sit down by the fire and wait for the stranger to return.")
    print("You're about to nod off when you hear footsteps behind you. You jump up to see who it is and a man comes out of the shadows. He slowly approaches, sits down, and eats his dinner.")
    print("After some time he speaks up, 'I am on a quest to save a friend trapped in a castle not too far from here, If you should join me I am sure they would give you a nice sum of gold in return. If not there is a village north of here you can settle down at and I shall go alone to fight the 'Big Scary Monster' keeping them captive. ")
    choice = input("Do you accept his request or travel to the village? (accept/village)")
    if choice == "accept":
        print("You accept his invitatoin and join him, he does 5 damage, adding his power to your own. You now deal", main.stats[1],"damage.")
        castle()
    elif choice =="village":
        print()
        print("You decline his invitation and decide to live a simple life and settle down in a small town filled with nice people.")
        print()
        print("The End")
        exit()
    else:
        print("invalid response, Game over")
        exit()
        
    
def castle():
    print()
    print("As you approach the castle you see a help wanted poster on a tree, it's even notarized.")
    print("It says, 'Greetings to whomever readith this, I'm trapped in this here castle against my will by 'Big Scary Monster', rescue me I've got some gold waiting for you.")
    choice = ""
    
    #if you came with helper you already accepted so this becomes redundant
    if main.stats[2] != "helper":
        choice = input("Do you accept the quest to save whoever is trapped in the castle or would you rather settle down in the nice town you see off in the distance and work in a nice little gift shop? (accept/town)")
        if choice == "town":
            print()
            print("You decide to live a simple life and settle down in a small town filled with nice people.")
            print()
            print("The End")
            exit()
        elif choice == "accept":
            print()
            print("The allure of gold was too strong, you decide to go save the stranger and get that reward!")
        else:
            print("Invalid")
            exit()
    print("As you walk upto the castle it is eerily quiet, nothings moving, and nothing makes a noise")
    print("Suddenly as you approach the courtyard the ground starts rumbling and the 'Big Scary Monster' appears!")
    bossfight()
    
def bossfight():
    print()
    #setting up boss and telling user their stats
    #Use of dictionary to store information below
    monster_stats = {"health":43, "damage":8}
    print("The monster is strong with a total of", monster_stats["health"],"health, and",monster_stats["damage"],"damage.")
    if main.stats[2] == "helper":
       print("You have", main.stats[0],"health, and do", main.stats[1], "damage")
    else:
        print("You have", main.stats[0],"health, and do", main.stats[1], "damage")
    
    #start of boss fight
    while monster_stats["health"] > 0:
        print()
        #Give time for user to read
        time.sleep(2)
        
        #Crit chance is decided and damage is calculated for you and boss
        crit = random.randint(1, 4)
        damage = main.stats[1]+random.randint(-1, 3)        
        m_damage = monster_stats["damage"]+random.randint(-2, 2)
        
        if crit == 1:
            damage = damage*2
            monster_stats["health"]=monster_stats["health"]-damage
            print("You attack dealing", damage,"to the monster, Critical hit! it has", monster_stats["health"],"left.")
        else:    
            monster_stats["health"]=monster_stats["health"]-damage
            print("You attack dealing", damage,"damage to the monster, it has", monster_stats["health"],"health left.")
        
        main.stats[0] = main.stats[0]-m_damage
        print("The monster delt ", m_damage," damage, you have ",main.stats[0], " health left.",sep="")
        if main.stats[0] == 0 or main.stats[0] < 0 and monster_stats["health"] < 0 or monster_stats["health"] == 0:
            print("With its last breat the monster takes you down with it, you have died, but you succeded in your mission.")
            write_health()
            exit()
        elif main.stats[0] == 0 or main.stats[0] < 0:
            print("The monster has defeated you, game over")
            write_health()
            exit()
   #End text, YOU WIN! YAY
    print()
    print("You defeated the monster!")
    #Final save of health to health.txt
    write_health()
    print("As you open the door it was guarding you find a man who introduces himslef as Freddricksun III of aglison. 'Thank you for your help sir, here's like a zillion gold")
    print
    
#So I don't have to write it out every time
def write_health():
    f = open("health.txt", "w")
    f.write(str(main.stats[0]))
    f.close

#Execute code with one line :)
if __name__ == "__main__":
    main()

