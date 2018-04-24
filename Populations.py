import random, matplotlib.pyplot as plt

a = int(input("Increasing/decreasing value?: "))
startingAmount = int (input ("How many members will be at the start?: "))
global adding
adding = [a, -a]


def plotResults (plotTime, plotAmount, timeAmount):
	#plt.axis([0, time, startingAmount, amount])
	print ("Your population has gone extinct after ",timeAmount,"periods.")
	plt.title("Population oscilation")
	plt.xlabel("Time")
	plt.ylabel("Amount of members of population")
	plt.plot(plotTime, plotAmount)
	#plt.table(cellText=None, cellColours=None, cellLoc='right', colWidths=None, rowLabels=None, rowColours=None, rowLoc='left', colLabels=None, colColours=None , colLoc='center',loc='bottom', bbox=None)
	plt.show()
	
def extinctionSym (startingAmount):
    amount = int(startingAmount)
    time = int()
    timeArray = [0]
    amountArray = [startingAmount]
    #adding = [1,-1]
    choice = int()
    while (amount > 0):
    	time = time + 1
    	timeArray.append(time)
    	choice = random.choice(adding)
    	amount = amount + choice
    	if (amount >= 0):
    	    amountArray.append(amount)
    	    print (amount)
    	else:
    	    amount = 0
    	    amountArray.append(amount)
    	    print (amount)
            	
    return (timeArray, amountArray, time)

generated_data = extinctionSym(startingAmount)
plotResults (generated_data[0], generated_data[1], generated_data[2])
	


