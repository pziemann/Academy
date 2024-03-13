import random

class Coin:
    def __init__(self, rare = False, clean = True, heads = True, **kwargs):
        
        for key, value in kwargs.items():
            setattr(self, key, value) #Take all args that were packed in Pound
        
        self.israre = rare
        self.isclean = clean
        if self.israre == True:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value
        if self.isclean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_color
    def rust(self):
        self.colour = self.rusty_colour
    def clean(self):
        self.colour = self.clean_colour
    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice
    def __str__(self):
        if self.original_value >= 1:
            return "$ {} coin".format(int(self.original_value))
        else:
            return "p {} coin".format(int(self.original_value*100))

class One_pence(Coin):
    def __init__(self):
        data ={
            "original_value": 0.01,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56
        }
        super().__init__(**data)

class Two_pence(Coin):
    def __init__(self):
        data ={
            "original_value": 0.02,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 25.9,
            "thickness": 1.85,
            "mass": 7.12
        }
        super().__init__(**data)

class Five_pence(Coin):
    def __init__(self):
        data ={
            "original_value": 0.05,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 18,
            "thickness": 1.77,
            "mass": 3.25
        }
        super().__init__(**data)
    def rust(self):
        self.colour = self.clean_colour
    def clean(self):
        self.colour = self.clean_colour

class Ten_pence(Coin):
    def __init__(self):
        data ={
            "original_value": 0.10,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 24.5,
            "thickness": 1.8,
            "mass": 6.5
        }
        super().__init__(**data)
    def rust(self):
        self.colour = self.clean_colour
    def clean(self):
        self.colour = self.clean_colour

class Twenty_pence(Coin):
    def __init__(self):
        data ={
            "original_value": 0.20,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,
            "diameter": 21.4,
            "thickness": 1.7,
            "mass": 5
        }
        super().__init__(**data)
    def rust(self):
        self.colour = self.clean_colour
    def clean(self):
        self.colour = self.clean_colour
class Fifty_pence(Coin):
    def __init__(self):
        data ={
            "original_value": 0.50,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,
            "diameter": 27.3,
            "thickness": 1.78,
            "mass": 5
        }
        super().__init__(**data)
    def rust(self):
        self.colour = self.clean_colour
    def clean(self):
        self.colour = self.clean_colour
class Two_pound(Coin):
    def __init__(self):
        data ={
            "original_value": 2,
            "clean_colour": "gold and silver",
            "rusty_colour": "greenish",
            "num_edges": 7,
            "diameter": 28.3,
            "thickness": 1.78,
            "mass": 5
        }
        super().__init__(**data)
class Pound(Coin):
    def __init__(self):
        data ={
            "original_value": 1,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 7,
            "diameter": 27.3,
            "thickness": 1.78,
            "mass": 5
        }
        super().__init__(**data)

coins = [One_pence(), Twenty_pence(), Two_pence(), Fifty_pence(), Twenty_pence(), 
         Pound(), Two_pound()]
for coin in coins:
    print("Coin: {}. Value: {} . Colour: {} . Diameter: {} ".format(coin, coin.value, coin.colour, coin.diameter))
