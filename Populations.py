import random, matplotlib.pyplot as plt

amount = int()
startingAmount = input ("How many members will be at the start?: ")
startingAmount = int (startingAmount)
amount = startingAmount
time = int()
timeArray = int()
timeArray = [0]
amountArray = [startingAmount]
adding = int()
adding = [1,-1]
choice = int()

def plotResults (plotTime, plotAmount, timeAmount):
	#plt.axis([0, time, startingAmount, amount])
	print ("Your population has gone extinct after ",timeAmount,"periods.")
	plt.title("Population oscilation")
	plt.xlabel("Time")
	plt.ylabel("Amount of members of population")
	plt.plot(plotTime, plotAmount)
	#plt.table(cellText=None, cellColours=None, cellLoc='right', colWidths=None, rowLabels=None, rowColours=None, rowLoc='left', colLabels=None, colColours=None , colLoc='center',loc='bottom', bbox=None)
	plt.show()
	

while (amount > 0):
	time = time + 1
	timeArray.append(time)
	choice = random.choice(adding)
	amount = amount + choice
	amountArray.append(amount)
	print (amount)


plotResults(timeArray, amountArray, time)



	


