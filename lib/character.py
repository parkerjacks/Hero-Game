
class Characters(): 
    def __init__(self,name,health,power): 
        self.name = name
        self.health = health 
        self.power = power 
    
    def __repr__ (self): 
        return(f'{self.name}, I got the power of {self.power} earths and I got a health of {self.health}. \n')

    
    def attack(self,enemy): 
        print(f'{self.name} has chosen to attack {enemy.name}.\n')
        enemy.health = enemy.health - self.power
        print(f'{self.name} does {self.power} damage to {enemy.name}.\n')
        if enemy.health <= 0:
            print(f'The {enemy.name} is dead.')
            
        else: 
            print(f'{enemy.name} now has a health of {enemy.health}.')

    def is_alive (self): 
        self.health > 0

    def print_status(self):
        return f'{self.name} retains a health of {self.health}.'