#! python3

#Ask the user for a number of rows with bricks and the maximum number of bricks per row)
while True:
    print ('Input the number of bricks and rows:')
    userInput = input ()
    if userInput.isdecimal() == False:
        print ('Please input a real number!')
    else:
        break


#Get ASCII ART
rowNumber = int(userInput)
print ('Here, take your bricks with you!\n')

for i in range (rowNumber):
    brickNumber = i+1
    blankNumber = rowNumber - (i)

    sideA = (' ' * blankNumber) + ('#' * brickNumber)
    sideB = '#' * brickNumber

    print (sideA, '', sideB)