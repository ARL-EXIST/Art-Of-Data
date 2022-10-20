import csv
from pickletools import read_bytes1

DigiDict = {

    }

def average(header):
    with open("digimon.csv", "r") as f:  
        data = csv.DictReader(f)

        suum = 0
        count = 0

        for rows in data:
            suum += int(rows[header])
            count += 1

        average = suum/count

        return average

def count_digimon(header, specifier):
    with open("digimon.csv", "r") as f:  
        data = csv.DictReader(f)

        attribute = 0

        for rows in data:
            if ((rows[header]) == specifier):
                attribute += 1
    
        return (attribute)

def attack_limit(memoryMax, attackMin):
    with open("digimon.csv", "r") as f:  
        data = csv.DictReader(f)

        #totRows = 0
        #for rows in data:
        #    totRows += 1
        
        attackMem = [[],[],[]]

        for rows in data:
            if (rows['Memory'] != "" and rows['Atk'] != "" and rows['Number'] != "") and (int(rows['Memory']) <= (memoryMax - 2)):
                """
                if len(attackMem[0]) == 0:
                    attackMem[0].append(int(rows['Atk']))
                    attackMem[1].append(int(rows['Memory']))
                elif len(attackMem[0]) == 1 and int(rows['Atk'])>attackMem[0][0]:
                    attackMem[0].append(int(rows['Atk']))
                    attackMem[1].append(int(rows['Memory']))
                elif len(attackMem[0]) == 1:
                    attackMem[0].insert(0, int(rows['Atk']))
                    attackMem[1].insert(0, int(rows['Memory']))
                else:
                """
                insert = binary_insert(attackMem[0], len(attackMem[0]) - 1, 0, int(rows["Atk"]))
                attackMem[0].insert(insert ,int(rows['Atk']))
                attackMem[1].insert(insert ,int(rows['Memory']))
                attackMem[2].insert(insert, int(rows['Number']))

                #attackMem[0].append(int(rows['Atk']))
                #attackMem[1].append(int(rows['Memory']))
        
        a = memTotCheck(attackMem[1], attackMem[0])
        #find(attackMem[1], attackMem[0], 15, 3, len(attackMem[1]) - 1)


        return attackMem[2][a[0]], attackMem[2][a[1]], attackMem[2][a[2]]#find(attackMem[1], attackMem[0], 15, 3, len(attackMem[1]) - 1)

def memTotCheck(m, a):

    for x in range(len(m) - 1, -1, -1):
        #print("x = " + str(a[x]))
        for y in range(x, -1, -1):
            #print("y = " + str(a[y]))
            if m[x] + m[y] <= 14:
                for z in range(y+1, -1, -1):
                    #print("z = " + str(a[z]))
                    #print(a[x] + a[y] + a[z])
                    if a[x] + a[y] + a[z] >= 300:
                        #print("300")
                        if m[x] + m[y] + m[z] <= 15:
                            #print("15")
                            return x, y, z
                    else:
                        break
    
    return None

"""def find(m, a, maxM, number, end):

    global recursVals
    recursVals = [[None]*len(m)]*len(a)

    if recursVals[maxM][end] != None:
        return recursVals[maxM][end]
    
    if maxM <= 0 or number <= 0 or end <=0:
        return 0
    
    result = 0

    if(m[end] > maxM):
        result = find(m, a, maxM, number, end - 1)
    else:
        result = max(find(m, a, maxM, number, end - 1), a[end] + find(m, a, maxM - m[end], end - 1))
    
    recursVals[maxM][end] = result
    return result"""

def binary_insert(list, high, low, item):
    
    if (high < low):
        return low
        
    mid = int((high + low) / 2)

    if item == list[mid]:
        return mid

    elif item > list[mid]:
        return (binary_insert(list, high, mid + 1, item))

    else:
        return (binary_insert(list, mid - 1, low, item))


print(average("Spd"))
print(count_digimon("Type","Vaccine"))
print(attack_limit(15, 300))