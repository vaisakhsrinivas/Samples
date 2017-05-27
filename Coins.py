import random


class Coin:

    def __init__(self, rare=False, clean = True, heads = True, **kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)

        self.israre = rare
        self.isclean = clean
        self.heads = heads


        if self.israre:
            self.value = self.original_value * 1.25

        else:

            self.value = self.original_value

        if self.isclean:
            self.color = self.cleancolor
        else:
            self.color = self.rustycolor

    def rust(self):
        self.color = self.rustycolor

    def clean(self):
        self.color = self.cleancolor


    def __del__(self):
        print("Coin spent")

    def flip(self):
        headoptions = [True, False]
        choice = random.choice(headoptions)
        self.heads = choice

    def __str__(self):
        if self.value >= 1.00:
            return "{} coin".format(int(self.value))
        else:
            return "{}p coin".format(int(self.value * 100))

class OnePence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.01,
            "cleancolor": "bronze",
            "rustycolor": "brownish",
            "numedges":1,
            "dia": 20.3,
            "thick": 1.52,
            "mass": 3.56,
        }

        super().__init__(**data)


class TwoPence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.02,
            "cleancolor": "bronze",
            "rustycolor": "brownish",
            "numedges":1,
            "dia": 25.9,
            "thick": 1.85,
            "mass": 7.12,
        }

        super().__init__(**data)


class FivePence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.05,
            "cleancolor": "silver",
            "rustycolor": "None",
            "numedges":1,
            "dia": 18.0,
            "thick": 1.77,
            "mass": 3.25,
        }
        super().__init__(**data)

    def rust(self):
        self.color = self.cleancolor

    def clean(self):
        self.color = self.cleancolor


class TenPence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.05,
            "cleancolor": "silver",
            "rustycolor": "None",
            "numedges":1,
            "dia": 24.5,
            "thick": 1.85,
            "mass": 6.50,
        }
        super().__init__(**data)

    def rust(self):
        self.color = self.cleancolor

    def clean(self):
        self.color = self.cleancolor


class TwentyPence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.20,
            "cleancolor": "silver",
            "rustycolor": "None",
            "numedges":7,
            "dia": 21.4,
            "thick": 1.7,
            "mass": 5.00,
        }
        super().__init__(**data)

    def rust(self):
        self.color = self.cleancolor

    def clean(self):
        self.color = self.cleancolor


class FiftyPence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.50,
            "cleancolor": "silver",
            "rustycolor": "None",
            "numedges":1,
            "dia": 27.3,
            "thick": 1.78,
            "mass": 8.00,
        }
        super().__init__(**data)

    def rust(self):
        self.color = self.cleancolor

    def clean(self):
        self.color = self.cleancolor


class TwoPound(Coin):
    def __init__(self):
        data = {
            "original_value" : 1.00,
            "cleancolor": "gold & silver",
            "rustycolor": "greenish",
            "numedges":1,
            "dia": 28.4,
            "thick": 2.50,
            "mass": 12.00
        }

        super().__init__(**data)


class Pound(Coin):
    def __init__(self):
        data = {
            "original_value" : 1.00,
            "cleancolor": "gold",
            "rustycolor": "greenish",
            "numedges":1,
            "dia": 22.5,
            "thick": 3.15,
            "mass": 9.5
        }

        super().__init__(**data)



coins = [OnePence(), TwoPence(), FivePence(), TenPence(), TwentyPence(), FiftyPence(),
         Pound, TwoPound()]


for coin in coins:
    arguments = [coin, coin.color, coin.value, coin.dia, coin.thick,
                 coin.numedges, coin.mass]

    string ="{} - Color: {}, value:{}, dia(mm):{}, thickness:{}, edges{}, mass:{}".format(*arguments)

    print(string)