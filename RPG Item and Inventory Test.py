class Item():

    def __init__(self, name, cost, weight, rarity):
        self.name = name
        self.cost = cost
        self.weight = weight
        self.rarity = rarity


    #Accessors
    def getName(self):
        return self.name

    def getCost(self):
        return self.cost

    def getWeight(self):
        return self.weight

    def getRarity(self):
        return self.rarity

    #Modifiers
    def setName(self, name):
        self.name = name

    def setCost(self, cost):
        self.cost = cost

    def setWeight(self, weight):
        self.weight = weight

    def setRarity(self, rarity):
        self.rarity = rarity


class Inventory():

    def __init__(self, inventory):
        self.inventory = inventory


    def addItem(self, item):
        inventory.append(item)

    #Accessors
    def getInventory(self):
        return self.inventory

    #Modifiers
    def setInventory(self, inventory):
        self.inventory = inventory

inventory = []
sword = Item('sword', 20, 15, 'common')
inventoryObj = Inventory(inventory)
inventoryObj.addItem(sword)

print(sword.getCost())
print(sword.getRarity())

print(inventory)
print(inventoryObj.getInventory())

    
