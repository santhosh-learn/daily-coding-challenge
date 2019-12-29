inputArrayValue=[4, 5, 1, 8]
inputSumValue=6

tempArray=[]
for number in inputArrayValue:
    additionNumber=inputSumValue - number
    if additionNumber in tempArray:
        print('Data found:['+str(additionNumber)+","+str(number)+']')
        break
    else:
        tempArray.append(number)