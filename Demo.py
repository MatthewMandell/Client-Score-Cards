import csv
Dict = {}

def consolidate(val):
    alist = list(val)
    if len(alist)> 16:
        if ''.join(alist[:17]) == 'JPM Chase Bank NA':
            return 'JPM Chase Bank NA'
    if len(alist)> 3:
        if ''.join(alist[:3]) == 'GS ' or ''.join(alist[:3]) == 'J. ':
            return 'GS/J. Aron & Co'


    if len(alist)> 4:
        if ''.join(alist[:4]) == 'HSBC':
            return 'HSBC'
    if len(alist)> 4:
        if ''.join(alist[:4]) == 'Citi':
            return 'Citibank'
    if len(alist)> 5:
        if ''.join(alist[:5]) == 'DB AG':
                return 'DB AG'
    if len(alist)> 2:
        if ''.join(alist[:2]) == 'MS':
            return 'MS'


    return val
def convertDate(val):
    alist = list(val)
    x = 0
    mon = int(''.join(alist[:2]))

    if mon == 1:
        x = 0
    elif mon == 2:
        x = 31
    elif mon == 3:
        x = 59
    elif mon == 4:
        x =90
    elif mon == 5:
        x = 120
    elif mon == 6:
        x = 151
    elif mon == 7:
        x = 181
    elif mon == 8:
        x =212
    elif mon == 9:
        x =243
    elif mon == 10:
        x = 273
    elif mon == 11:
        x =304
    elif mon == 12:
        x = 334
    if ''.join(alist[5:7]) == '20':
        x += 365
    return x


def convert(val):
    alist = list(val)
    x = 0
    y = 0
    bool = False
    for i in range(len(alist)):
        if alist[i] == 'E':
            x = float(''.join(alist[0:i]))
            y = float(''.join(alist[i+1:]))
            bool = True
    if bool:
        return x * (10**y)
    else:
        return float(val)

with open('/Users/matthewmandell/Desktop/Work/EBScoreCards.csv') as csvfile:


    readCSV = csv.reader(csvfile, delimiter=',')
    EB = []
    notational = []
    total = []

    for row in readCSV:
        if row[14] == 'Completed':
            client = consolidate(row[7])


            if Dict.get(client) == None:
                Dict[client] = {}
                eb = consolidate(row[0])



                Dict[client][eb] = [convert(row[17]), 1]

                Dict[client][eb] = [convert(row[17]), 1]
            else:
                eb = consolidate(row[0])


                if Dict[client].get(eb) == None:
                    Dict[client][eb] = [convert(row[17]), 1]
                else:
                    tempN = Dict[client][eb][0] +convert(row[17])
                    tempT = Dict[client][eb][1]+1
                    Dict[client][eb] = [tempN, tempT]
                    print(Dict[client][eb][0])











for k in Dict:
    val = str(k)

    directory='/Users/matthewmandell/Desktop/Output1/'+k+'.csv'
    file = open(directory, 'w+')
    with file:
        writer = csv.writer(file)
        writer.writerow([k])
        writer.writerow(['                                          BB BREAKDOWN                                        '])
        writer.writerow(['EB','Notational','Notational%','TradeCount','TradeCount%'])
        sumN = 0.0
        sumT = 0.0
        for key in Dict[k]:
            sumN = sumN + Dict[k][key][0]
            sumT = sumT + Dict[k][key][1]
        for key in Dict[k]:
            arr = [key]
            print(Dict[k][key][0])
            percentN = round(Dict[k][key][0]/sumN,4)
            percentT = round(Dict[k][key][1]/sumT,4)
            #avgDays = Dict[k][key][2]/Dict[k][key][1]
            arr.append(Dict[k][key][0])
            arr.append(percentN*100)
            arr.append(Dict[k][key][1])
            arr.append(percentT*100)
            #arr.append(avgDays)
            writer.writerow(arr)
            print('test')

        writer.writerow(['Total:', sumN, '100%', int(sumT), '100%'])
