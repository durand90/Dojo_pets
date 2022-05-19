class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def info(self):
        print(f'pet name: {self.name}')
        print(f'pet type: {self.type}')
        print(f'pet tricks: {self.tricks}')
        print(f'pet health: {self.health}')
        print(f'pet energy: {self.energy}')

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5

    def noise(self):
        print('woof')






class Ninja(Pet):
    def __init__(self, name, type, tricks, health, energy, first_name, last_name, pet, treats, pet_food):
        super().__init__(name, type, tricks, health, energy)
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def info(self):
        super().info()
        print(f'first name: {self.first_name}')
        print(f'last name: {self.last_name}')
        print(f'pet: {self.pet}')
        print(f'treats: {self.treats}')
        print(f'pet food: {self.pet_food}')


    def walk(self):
        super.play()

    def feed(seflf):
        super.eat()

    def bathe(self):
        super.noise()


rock_lee = Ninja('fluffy', 'pitbull', 'roll over', 200, 1500, 'Rock', 'Lee', 'dog', 'chew toy', 'bacon bits')

rock_lee.info()