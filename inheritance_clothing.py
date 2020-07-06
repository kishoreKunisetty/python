class Clothing:

    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price
        
    def change_price(self, price):
        self.price = price
        
    def calculate_discount(self, discount):
        return self.price * (1 - discount)
    
    def calculate_shipping(self, weight=0.0, rate=0.0):
        return weight*rate
        
class Shirt(Clothing):
    
    def __init__(self, color, size, style, price, long_or_short):
        '''This function initializes shirt class with attributes color, size, style, price, long_or_short
        
        args : color(String), size(integer), style(String), price(float), long_or_short(String)
        
        return : None
        '''
        Clothing.__init__(self, color, size, style, price)
        self.long_or_short = long_or_short
    
    def double_price(self):
        '''This function doubles the price of shirt
        
        args: None
        
        return: None
        '''
        self.price = 2*self.price
        #obesrvation: No return
    
class Pants(Clothing):

    def __init__(self, color, size, style, price, waist):
        '''This function initializes Pants class with attributes color, size, style, price, long_or_short'
        
        args : color(String), size(integer), style(String), price(float), long_or_short(String)
        
        return : None
        '''
        Clothing.__init__(self, color, size, style, price)
        self.waist = waist
        
    def calculate_discount(self, discount):
        '''This function calculates the discount
        
        args : discount(integer)
        
        return : Modified Price
        '''
        return self.price * (1 - discount / 2)  #observation : the price is not actually modified, it only returned new price as we don't want it to effect the original price.
    
class Blouse(Clothing):
    def __init__(self, color, size, style, price, country_of_origin):
        '''This function initializes Blouse class with attributes color, size, style, country_of_origin'
        
        args : color(String), size(integer), style(String), price(float), country_of_origin(String)
        
        return : None
        '''
        Clothing.__init__(self, color, size, style, price)
        self.country_of_origin = country_of_origin

    def triple_price(self):
        '''This function triples the price of Blouse
        args: None
        
        return : modified price
        '''
        self.price = 3 * self.price
        return self.price               #New price




