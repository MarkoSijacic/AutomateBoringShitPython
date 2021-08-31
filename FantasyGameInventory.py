#make a dictionary inventory

myInv = {'gold': 24, 'potion': 3, 'sword': 1}

#create and run a function which will show a dictionary inventory in a fantasy RPG formating

def showInv(inv):
	print ('Items in inventory')
	x = list(inv.values())
	y = list(inv.keys())

	totalItems = 0
	for i in range (len(inv)):
		print (x[i], y[i])
		totalItems += x[i]

	print ('Total number of items: ', totalItems, '.' )
	print ('')
	
showInv(myInv)

#make a list of additional inventory items

loot1 = ['gold', 'potion', 'gold', 'gold', 'arrow']

#create and run a function which will turn the list values into dictionary items and add them to the exciting dictionary

def addLoot(loot, inv):
	for i in range (len(loot)):
		x = loot[i]
		if x in inv:
			inv[x] +=1
		if x not in inv:
			inv.setdefault (x, 1) 

addLoot(loot1, myInv)
showInv(myInv)