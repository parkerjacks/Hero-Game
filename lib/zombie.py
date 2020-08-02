from lib.character import Characters 

class Zombie(Characters): 
    def speak(self): 
        print(f'{self.name}: "ARRRGHHHHH" *coughs* *coughs* *drools*\n')

    def defense (self,enemy): 
        self.health = self.health 
        enemy.health = enemy.health - self.power
        print(f'{self.name} health = {self.health}. \n {enemy.name} health = {enemy.health}') 