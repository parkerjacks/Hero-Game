from lib.character import Characters
from lib.Hero import Hero 
from lib.goblin import Goblin
from lib.zombie import Zombie

"""In this simple RPG game, the hero fights the goblin."""

 
"""1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee"""



#Hero object 
Boots = Hero("Boots",10,5) 
Boots.trash_talk()

#Goblin object 
Ricky = Goblin("Ricky Jay",6,2)
Ricky.speak()

#Zombie object 
Drooly = Zombie("Drooly",5,2) 
Drooly.speak()
while True: 
    
    print(f'Boots has {Boots.health} health and the power of {Boots.power} earths.\n') 
    print(f'Ricky J has {Ricky.health} health and the power of {Ricky.power} earths.\n') 

    while Boots.is_alive and Ricky.is_alive:
            print("What do you want to do?...\n") 
            print("1. fight goblin")
            print("2. do nothing")
            print("3. flee") 
            print("4. zombie attacks")
            print(">>>>>",)
            user_input = int(input())
            if user_input == 1:
                Boots.attack(Ricky)
            
            elif user_input == 2: 
                print(f'{Boots.name} has choosen to do nothing.')
                Ricky.attack(Boots)

            elif user_input == 3:
                print("Goodbye") 
                break
            
            elif user_input == 4: 
                print
                Drooly.attack(Boots) 
                if Boots.health > 0: 
                    print(f'{Drooly.name} unexpectedly attacks {Boots.name} again!')
                    y_n = input("Would you like to continue fighting the zombie? Enter Y to continue or N to go back to main menu.")
                    y_n = y_n.upper()
                    if y_n == "Y":
                        if Boots.health >= Drooly.power:
                            Drooly.defense(Boots) 
                        else: 
                            print(f'{Boots.name} is Dead!')
                        break
                    
                else: 
                    print(f'{Boots.name()} is Dead') 
                    break 
                
            else:
                print("Invalid input %r" % user_input)

  

