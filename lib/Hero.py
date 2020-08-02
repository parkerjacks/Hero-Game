from lib.character import Characters

class Hero(Characters): 
    def trash_talk(self): 
        print(f'{self.name}: "These boots are not made for walking theyre made for kicking Goblin A**! Ive got the strength of {self.power} earths and the health of {self.health}."\n')

    