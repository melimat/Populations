# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt, random

environmentCapacity = int(input("Maximal capacity that environment can handle?: "))

global startingAmount
startingAmount = int(input("How many members would be at the beginning?: "))

global maxTime
maxTime = int(input("How long may simulation take?: "))

global a
a = int(input("Max Increasing/Decreasing value?: "))

global amountArray
amountArray = [startingAmount]

global timeArray
timeArray = [0]

global maxAmount
maxAmount = int(0)

global extinct
extinct = bool(False)


def oscillationSym(capacity, start, maxtime):
    global maxAmount, extinct
    amount = int(start)
    time = 0
    while (time <= maxTime):
        b = int(random.randint(0, a))
        time = time + 1
        timeArray.append(time)
        if (amount > capacity):
            amount = amount - b
            amountArray.append(amount)
        else:
            amount = amount + b
            amountArray.append(amount)
        if (amount > maxAmount):
            maxAmount = amount
        print(("Time: " + str(time) + " : " + "Amount: " + str(amount) + " -> " + "maxAmount: " +  str(maxAmount)))
        if (amount <= 0):
            amountArray.append(0)
            extinct = True
            break


def plotResults(plotTime, plotAmount, envCap):
    global maxAmount, startingAmount, extinct
    if (extinct is True):
        print("Cannot plot graph, your population has gone extinct.")
    else:
        plt.title("Population oscillating around environmental capacity")
        plt.xlabel("Time")
        plt.ylabel("Amount of members of population")
        plt.xlim(0, maxTime)
        plt.ylim(startingAmount, maxAmount + 2)
        capArray = []
        for i in range(len(plotTime)):
            capArray.append(envCap)
        plt.plot(plotTime, capArray, label="Environmental capacity")
        plt.plot(plotTime, plotAmount, label="Population amount")
        plt.legend()
        plt.show()


oscillationSym(environmentCapacity, startingAmount, maxTime)
plotResults(timeArray, amountArray, environmentCapacity)