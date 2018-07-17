import random, matplotlib.pyplot as plt

a = int(input("Increasing/decreasing value?: "))
startingAmount = int(input("How many members will be at the start?: "))
global adding
adding = [a, -a]
global timeArray
timeArray = [0]
global amountArray
amountArray = [startingAmount]
global time


def plotResults(plotTime, plotAmount):
    timeLenght = int(len(plotTime) - 1)
    print("Your population has gone extinct after " + str(timeLenght) + " periods.")
    plt.title("Population oscilation")
    plt.xlabel("Time")
    plt.ylabel("Amount of members of population")
    plt.plot(plotTime, plotAmount)
    plt.show()


def extinctionSym(startingAmount):
    amount = int(startingAmount)
    time = int()
    while (amount > 0):
        time = time + 1
        timeArray.append(time)
        choice = random.choice(adding)
        amount = amount + choice
        if (amount >= 0):
            amountArray.append(amount)
            print(amount)
        else:
            amount = 0
            amountArray.append(amount)
            print(amount)


extinctionSym(startingAmount)
plotResults(timeArray, amountArray)
