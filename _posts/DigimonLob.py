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

def callFind(w, w_Two, v, C, C_Two, n):
    global recursVals
    recursVals = [[-1] * ((C_Two * 1000) + C)]*n
    mergeC = (C_Two * 1,000) + C
    return find(w, w_Two, v, mergeC, n)


def find(w, w_Two, v, C, n):

    #global recursVals
    #recursVals = [[None]*len(w)]*len(v)

    if recursVals[n][C] != -1:
        return recursVals[n][C]
    
    if C == 0 or n < 0 :
        return 0
    
    result = 0

    if(w_Two[n] > C / 1,000,000 and w[n] > C % 1,000,000):
        result = find(w, w_Two, v, C, n - 1)
    else:
        result = max(find(w, w_Two, v, C, n - 1), v[n] + find(w, w_Two, v, C - w[n] - (w_Two[n] * 1,000,000), n - 1))
    
    recursVals[n][C] = result
    return result

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