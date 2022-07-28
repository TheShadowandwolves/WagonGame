import random

front_train = "<[''']>"
wagon_empty = "<|___|>"
wagon_half = "<|---|>"
wagon_full = "<|===|>"
wagon_20 = "<|__-|>"
wagon_40 = "<|_--|>"
wagon_60 = "<|--=|>"
wagon_80 = "<|-==|>"
wagon_smashed = "<|###|>"

class Wagon:
    weight = 0
    overweight_limit = 0.1

    def __init__(self, type, range):
        self.wagon_type = type
        self.max_weight = range

    def __repr__(self):
        return self.wagon_type

    def set_type(self, weight):
        if weight < 100:
            self.wagon_type = wagon_empty
        elif weight < 200 and weight >= 100:
            self.wagon_type = wagon_20
        elif weight < 400 and weight >= 200:
            self.wagon_type = wagon_40
        elif weight < 500 and weight >= 400:
            self.wagon_type = wagon_half
        elif weight < 600 and weight >= 500:
            self.wagon_type = wagon_60
        elif weight < 800 and weight >= 600:
            self.wagon_type = wagon_80
        elif weight < 1000 and weight >= 800:
            self.wagon_type = wagon_full
        else:
            self.wagon_type = wagon_smashed

    def weight_overweight(self, amount):
        if (amount + self.weight * self.overweight_limit) > self.max_weight:
            return True
        else:
            return False

    def fill_weight(self, amount):
        if self.weight_overweight(amount):
            self.set_type(1000)
            self.weight += amount
            return False
        else:
            self.weight += amount
            self.set_type(self.weight)
            return True

    def print_weight(self):
        print(self.max_weight)
    
class Train:
 

    crash = False  # if the train crashes, it will be set to True

    wagon_amount = 0
    wagons = []


    def if_crashed(self):
        return self.crash

    def amount_of_wagons(self):
        return self.wagon_amount

    def add_wagon(self):
        if self.crash: 
            print('The train crashed, you can not add more wagons.')
            return False
        else:
            self.wagon_amount += 1
            self.wagons.append(Wagon(wagon_empty, random.choice(range(100, 999))))
            return self.wagon_amount
    
    def fill_wagon(self, amount):
        if self.crash:
            #print('The train crashed, you can not fill the wagon.')
            return False
        else:
            if (self.wagons[-1].fill_weight(amount)):
                return True
            else:
                self.crash = True
                return False
    
    def print_train(self):
        print(front_train)
        num = self.wagon_amount
        for wagon in self.wagons:
            print(wagon)

    def train_weight(self):
        total = 0
        for wagon in self.wagons:
            total += wagon.weight
        return total

    def get_max_weight(self):
        index = []
        for wagon in self.wagons:
            index.append(wagon.max_weight)
        return index


class Score:
    score = 0

    def __repr__(self):
        return str(self.score)

    def get_score(self, max, inputx, rounds):
       
        fscore = int((rounds -1) * 1000 - (max - inputx))
        if fscore < 0:
            self.score = 0
        else:
            self.score = fscore

        return self.score

