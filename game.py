from sqlite3 import Timestamp
from mechanic import Train, Score
from scoreFile import *
from datetime import datetime, tzinfo


front_train = "<[''']>"
wagon_empty = "<|___|>"
wagon_half = "<|---|>"
wagon_full = "<|===|>"
wagon_20 = "<|__-|>"
wagon_40 = "<|_--|>"
wagon_60 = "<|--=|>"
wagon_80 = "<|-==|>"
wagon_smashed = "<|###|>"

def print_t():
    for wagon in train.wagons:
        print(wagon, end="")
    print(front_train)

print("Hello, this is my first try of a game in Python \n The idea of the game is:")
print("You have a train with wagons, each wagon can carry a certain amount of weight.")
print("You have to load the wagons with the right amount of weight to get to the next station.")
print("Each wagon has a weight limit, if you extend the weight it causes the train to crash.")
print("If you manage to load the train until the last station, you win the game.")
print("\n")
play = True
rounds = 0
last_weight = 0
train = Train()
train.add_wagon()
while play == True:
   
    print_t()
    rounds += 1
    print("Round: " + str(rounds))
    print("Enter an amount of weight to load the train with:")
    weight = int(input())
    last_weight = weight
    user = True
    while user == True:
        if not (train.fill_wagon(weight)):
            print("You can't load more than the wagon can hold.")
            user = False
            play = False
        else:
            print("You loaded the train with " + str(weight) + " kg.")
            print_t()
            print("Do you want to load more inside the wagon? (y/n)")
            user_input = input()
            if user_input == "y" or user_input == "Y":
                print("Enter an amount of weight to load the wagon with:")
                weight = int(input())
                last_weight = weight
                user = True
            elif user_input == "n" or user_input == "N":
                print("Loading next wagon...")
                user = False
            else:
                print("You entered an invalid input.")
                user = False

    if train.if_crashed():
        print("The train crashed!")
        print(wagon_smashed)
        play = False
    else:
        train.add_wagon()

print_t()
print("You finish the game! Here are your results:")
print("\n")
print("max weight of all the wagons was:")
for max in train.get_max_weight():
    print(max, end=" ")
    print(",", end=" ")
print("\n")
round = rounds
print("You played " + str(rounds) + " rounds.")
round = int(rounds)
print("These are the different weights you loaded:")
for wagon in train.wagons:
    print(wagon.weight, end=" ")

print("\n")
print("The total weight of the train is: " + str(train.train_weight()) + " kg.")
train_weight = int(train.train_weight())


print("This is the max weight of all wagon: ")
max_weight = 0
for wagon in train.wagons:
    max_weight += int(wagon.max_weight)
    
max_weight -= int(train.wagons[-1].max_weight)
print(max_weight)
print("\n")
fscore = Score()
sc = fscore.get_score(max_weight, train_weight, round)
print("The final score of your is: " + str(sc) + " points.")

curDT = datetime.now()
date = curDT.strftime("%Y-%m-%d %H:%M:%S")
print("Do you wish to have your score saved? (y/n)")
question = input()
if question == "y" or question == "Y":
    print("Enter your name:")
    name = input()
    commit_a_score(sc, date, name)

print("\n")
get_score()
print("\n")    

print("Thank you for playing my game!")
# train.add_wagon()
# train.add_wagon()
# if train.fill_wagon(1000):
#     print("You loaded the wagon with", 100, "kg.")
#     train.add_wagon()
# else:
#     print("You can't load more than the wagon can hold.")
# train.print_train()
# print(str(train.crash))
# print(train.wagons[-1].weight)


# if __name__ == '__main__':     
#     app.run(debug=True)