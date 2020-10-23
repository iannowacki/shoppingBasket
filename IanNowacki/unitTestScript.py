import unittest
#import courseWork python file then from it import two classes Shop and ShoppingBasket
import courseWork
from courseWork import Shop, ShoppingBasket

#set up test class versions of our classes inheriting from a class the unittest library 
class Test_Shop(unittest.TestCase):
    
    #this test to check the loadInitialStock function works
    def test_loadInitialStock(self):
        s1 = Shop()
        #load in csv which is known to contain quantity 10 for each item.
        s1.loadInitialStock("itemQty.csv")
        itemObj = s1.stockItems["beans"]

        #test checks that the value 10 was read back from the quantity successfully saved to the shop
        self.assertEqual(10, itemObj.quantity )

    #test for itemsInStock uses addItemAndQty() function from Shop class to add in items then tests if this
    #function returns the correct
    def test_itemsInStock(self):
        s2 = Shop()
        s2.addItemAndQty("bananas", 0.49, 5)
        
        #tests if bananas were added correctly by comparing the quantity stored conpared to expected value 5
        self.assertEqual(5, s2.itemsInStock("bananas")  )

#creating test class for ShoppingBasket
class Test_ShoppingBasket(unittest.TestCase):
    #testing addItemAndQty function by creating shop, adding items to it, then testing if value stored matches expected
    def test_addItemAndQty(self):
        s3 = Shop()
        s3.stockItems = {}
        s3.addItemAndQty("donuts", 0.79, 10)
        s3.addItemAndQty("crab", 4.79, 10)
        s3.addItemAndQty("beans", 0.49, 60)
        s3.addItemAndQty("beans", 0.49, 60)
        itemObj = s3.stockItems["beans"]
        #we added two lots of 60 beans so 120 is to be expected back
        self.assertEqual(120, itemObj.quantity)
    #this test adds items to shop, creates a basket then adds items to basket. the total expected cost has
    #been manually calculated and tested against actual result of function
    def test_totalCost(self):
        s4 = Shop()
    
        s4.addItemAndQty("beans", 0.49, 5)
        s4.addItemAndQty("oats", 1.00, 5)
        s4.addItemAndQty("bananas", 0.25, 5)
        s4.addItemAndQty("cheese", 2.99, 5)
        s4.addItemAndQty("beans", 0.49, 5)
        
        b1 = ShoppingBasket(s4)
        #same items that were added to shop now added to basket
        b1.addItemAndQty("beans", 5)
        b1.addItemAndQty("oats", 5)
        b1.addItemAndQty("bananas", 5)
        b1.addItemAndQty("cheese", 5)
        b1.addItemAndQty("beans", 5)
        #total of basket manually calculated is checked against result of totalCost() function
        self.assertEqual(26.10, b1.totalCost()  )

    

if __name__ == "__main__":
    #entry point for unittest functions
    unittest.main()
