import csv #one import required for csv file handling

#Declaring ItemAndQty class which is used to create objects containing item name, price and quantity data members.  
class ItemAndQty:
    #Default constructor is replaced with customer constructor requiring name, price and quantity arguments which
    # are transferred into non static data members with their types cast as String, float and integer respectively
    def __init__(self, name, price, quantity):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)
    #Cost function which takes price and quantity values arguments then returns the product of them (ie cost of them) 
    def cost(self, price, quantity):
        return float(self.price * self.quantity)
    #__repr__ function replaces default string representation function. Allows us to define settings for making
    # the string representations of classes more useful & legible
    def __repr__(self):
        return '{self.__class__.__name__}(itemName: {self.name}, price: {self.price}, quantity: {self.quantity})'.format(self=self)

#Defining class called Shop (no inheritance)
class Shop:
    #Creating blank dictionary to act as a 'stockroom' for the shop
    stockItems = {}
    #function for reading csv file
    def loadInitialStock(self, fileName):
        #open existing csv file in read mode then create reader
        csvFile = open(fileName, "r", newline='')
        csvReader = csv.reader(csvFile, delimiter=',', quotechar='"')
        #Create list newStock[] as temporary holding container for holding lists of csv rows from csvReader
        # allows easier indexing into class constructor at next stage
        newStock = []
        for row in csvReader:
            newStock.append([row[0], float(row[1]), int(row[2])])
        csvFile.close()
        
        #len(newStock) returns how many rows were contained in csv so we can use this info to iterate the
        # correct number of times to call addItemAndQty for each row which, in turn, adds items to stockroom
        for i in range(len(newStock)):
            self.addItemAndQty(newStock[i][0], newStock[i][1], newStock[i][2])
       
    #function for creating an ItemAndQty object from name, price and quantity input arguments. object is then
    #added to stockroom
    def addItemAndQty(self, name, price, quantity):
        #create temporary ItemAndQty object named 'item' to be used 
        # to check if a key of this name already exists in stockItems {}
        item = ItemAndQty(name, price, quantity)

        #search stockItems dictionary to see if an item of this name already exists
        if item.name in self.stockItems:
            #if the name already exists in stockItems, create temporary holder for
            # the existing object (to easily access it's current value of 'quantity' at next step)
            sI = self.stockItems[item.name]
            
            #add the new ItemAndQty object to stockItems dict. Get current quantity value 
            # (sI.quantity as above) and add new quantity to existing stock
            self.stockItems[item.name] = ItemAndQty(item.name, item.price, (sI.quantity + item.quantity))
            

        else:
            #if new stock item object doesn't exist on stockItems list then a new entry is created with the item
            #previously created
            self.stockItems[item.name] = item
            
    #Function which takes item name as argument, checks if named item is in stockItems
    def itemAndQtyByName(self, name):
        #if item is founc in stockItems, it returns the associated object, if not found, returns string "None"
        if name in self.stockItems:
            return self.stockItems[name]
        else:
            return "None"
    #itemsInStock function takes name as argument and returns integer value of quantity of items in stock
    def itemsInStock(self, name):
        #if no item is found when searching for item of that name then string "zero" is returned
        if self.itemAndQtyByName(name) == "None":
            return "zero"
        #if item is found then temporary object is made to index the quantity value of it and that value is returned
        else:
            sI = self.stockItems[name]
            return sI.quantity

#defining ShoppingBasket class
class ShoppingBasket:
    #default constructor is replaced with one requiring that objects are passed a reference to a Shop object
    #empty basket dictionary object created
    def __init__(self, Shop):
        self.basket = {}
    #addItemAndQty function creates an ItemAndQty object and adds it to basket dictionary with object name as key
    def addItemAndQty(self, name, quantity):
        #check if item thats trying to be added to basket is available in shop's stockItems, if not return "zero"
        if name not in Shop.stockItems:
            return "zero"
        #if it is found then the options are 1. if this type of item is not in the basket currently then a temporary 
        # object sI is created and added to basket which takes the price from object itself to fill in what is needed
        # for constructor requirements of ItemAndQty objects. initiated with a zero value to give starting place for 
        # subsequent addition of items to basket.   
        else:
            sI = Shop.stockItems[name]

            if name not in self.basket:
                self.basket[name] = ItemAndQty(name, sI.price, 0)
           
            #if quantity in shop is greater than or equal to requested amount then it is taken from shop's
            #  stockItems{} and the same value is added to the basket dictionary
            if sI.quantity >= quantity:
                bI = self.basket[name]
                updQuantity = bI.quantity
                #add quantity to basket
                self.basket[sI.name] = ItemAndQty(sI.name, sI.price, (updQuantity + quantity) )
                #take quantity from stockItems
                Shop.stockItems[name] = ItemAndQty(sI.name, sI.price, (sI.quantity - quantity))
                return quantity
            #else if quantity in basket is greater than quantity in shop then "insufficient stock is returned"    
            else:
                return "insufficient stock"    
    #totalCost function to count up cost of all items in basket.
    def totalCost(self):
        #temporary subTotals holder to hold sub total of each item value
        subTotals = []
        #iterate through all items in basket
        for item in self.basket:
            sI = self.basket[item]          
            subTotals += [sI.cost(sI.price, sI.quantity)]
        #sum up all subTotals and return value   
        return sum(subTotals)
    #function to clear basket simply re-declare basket dictionary empty
    def empty(self):
        self.basket = {}
                