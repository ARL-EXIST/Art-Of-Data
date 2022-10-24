import csv
from pickletools import read_bytes1

#Collaborator: Henry
#videos watched for knapsack problem: https://youtu.be/xOlhR_2QCXY, https://youtu.be/dT6dvdbpChA



#knapsack average of digimon values for a specific header (e.g Speed)
#go through each row, add the value found in a specified column and add that to the suum
#count increases by one every time a value gets added to sum
#divide suum by count to get the average
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



#Takes header to knapsack the correct column and matches all pokemon whose header value is the specifier
#to knapsack how many pokemon have that specific specifier
def count_digimon(header, specifier):
    with open("digimon.csv", "r") as f:  
        data = csv.DictReader(f)

        attribute = 0

        for rows in data:
            #checks if column value is specifier
            if ((rows[header]) == specifier):
                attribute += 1
    
        return (attribute)


#combination of at most 3 Digimon with at most memoryMax and at least attackMin
# Returns the Number of the Digimon to use
def attack_limit(memoryMax, attackMin):
    with open("digimon.csv", "r") as f:  
        data = csv.DictReader(f)

        #attackMem stores 3 arrays - 1st for Attack, 2nd for Memory, 3rd for their Number to know which digimon matches to the attack/mem values
        attackMem = [[],[],[]]

        #go through each row and add the memory, attack and number value in a sorted array with binary insert
        # dont add any row elements where the memory is greater than the memorMax
        for rows in data:
            if (rows['Memory'] != "" and rows['Atk'] != "" and rows['Number'] != "") and (int(rows['Memory']) <= memoryMax):

                insert = binary_insert(attackMem[0], len(attackMem[0]) - 1, 0, int(rows["Atk"]))

                attackMem[0].insert(insert ,int(rows['Atk']))
                attackMem[1].insert(insert ,int(rows['Memory']))
                attackMem[2].insert(insert, int(rows['Number']))
        
        # list indexes stores result (3 elements with int or None values)of memTotCheck 
        # - combination of up to 3 numbers that meet memMax and attackMin constraints
        indexes = memTotCheck(attackMem[1], attackMem[0], memoryMax, attackMin)


        #       global recursVals - debugging code
        #       recursVals = [[None] * (memoryMax + 1) ] * (len(attackMem[1]) + 1) - debugging code
        #       print(str(len(attackMem[0]) + 1) + ", " + str(memoryMax + 1)) - debugging code
        #       print(callKnapsack(attackMem[1], attackMem[0], memoryMax, len(attackMem[0])-1)) - debugging code
        #       print(str(indexes[0]) + ", " + str(indexes[1]) + ", " + str(indexes[2])) - debugging code

        #if index's first value is not None, include it in final combo answer
        if indexes[0] != None:
            #if index's second value is not None, include it in final combo answer
            if indexes[1] != None:
                #if index's third value is not None, include it in final combo answer
                if indexes[2] != None:
                    return attackMem[2][indexes[0]], attackMem[2][indexes[1]], attackMem[2][indexes[2]]
                #if indexes's third value is none then there is no 3rd digimon to include
                return attackMem[2][indexes[0]], attackMem[2][indexes[1]]
            #if indexes's second value is none then there is no 2nd or 3rd digimon to include
            return attackMem[2][indexes[0]]
        #if indexes's first value is none then NO combo of Digimon meets the restraints
        return None

#Binary insert algorithm to insert new elements into a list
def binary_insert(list, high, low, item):
    
    #reached a single element
    if (high < low):
        return low
    
    # get halfway between low and high
    mid = int((high + low) / 2)

    #if the item is in the mid of the list, return that index
    if item == list[mid]:
        return mid

    #otherwise if item is greater, repeat this method but with low set to mid+1
    elif item > list[mid]:
        return (binary_insert(list, high, mid + 1, item))

    #otherwise if item is lower, repeat this method but with high set to mid-1
    else:
        return (binary_insert(list, mid - 1, low, item))

#check each element from top to bottom ––– x is the 1st set value, y the 2nd, and z the 3rd
# then check wether the x or the x + y, or the x + y + z, combo adds up to 300 or more within memory confines
# This function requires that you are searching for a combo with at most 3 elements/digimon
# does not work for bigger or smaller group compositions - hard coded for 3 group size
def memTotCheck(m, a, mMax, aMin):

    #Check each x value for x (+ y (+ z)) combo
    for x in range(len(m)-1, -1, -1):

        #       print("x = " + str(a[x])) - debugging code

        #if x alone is greater than aMin, return only x (all elements in m are 15 or less)
        if a[x] >= aMin:

            #       print("x") # - debugging code

            return x, None, None

        #only check for an x + y combo if x <= mMax - 1, as y has a min value of 1
        if m[x] <= mMax-1:
            #Check each y value for x + y (+ z) combo where y is each next element after x
            for y in range(x-1, -1, -1):

                #       print("y = " + str(a[y])) - debugging code

                # if x + y is greater than aMin, and less than mMax, return x and y
                if a[x] + a[y] >= aMin and m[x] + m[y] <= mMax:

                    #       print("y") # - debugging code

                    return x, y, None

                #if x + y memory > 14 then the combo with z is not within the Memory capacity
                if m[x] + m[y] <= mMax-1:
                    #Check each z value for x + y + z combo where z is each next element after y
                    for z in range(y, -1, -1):

                        #       print("z = " + str(a[z])) - debugging code
                        #       print(a[x] + a[y] + a[z]) - debugging code

                        #If the combo >= minimum value, then check memory
                        # else - no other z value will reach minimum (Attack) value needed
                        # (as the a array is sorted least to greatest) so break z for loop
                        # and iterate to next y value
                        if a[x] + a[y] + a[z] >= aMin:

                            #       print("300") - debugging code
                            
                            #If also Within memory constraints, return x, y, z
                            if m[x] + m[y] + m[z] <= mMax:

                                #       print("z") #- debugging code

                                return x, y, z
                        else:
                            break
    
    #Prints that no combo was found
    print("No combination adds to at least 300 attack AND within memory of 15")
    return None, None, None


# call functions for terminal

#find average speed
print("Average Speed is: %.2f" % average("Spd"))
#count digimon of Type - Vaccine
print("The number of digimon of Type Vaccine is : " + str(count_digimon("Type","Vaccine")))
#Find combo of up to 3 digimon that have at most 15 memory, and at least 300 attack
print("Digimon – " + str(attack_limit(15, 300)) + " – have at least 300 combined attack and within 15 combined memory")


#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––


#Below is code that I wrote but unfortunately did not use because it didn't work for some reason


#attempted to merge 2 weights into one for knapsack problem
# code in knapsack function was slightly different when I used this function
"""def callknapsack(w, w_Two, v, C, C_Two, n):
    global recursVals
    recursVals = [[-1] * ((C_Two * 1000000) + C)]*n
    #print((C_Two * 1000) + C)
    mergeC = ((C_Two * 1000000) + C)
    return knapsack(w, w_Two, v, mergeC, n)"""

#makes a global 2d memory array of n by C, then calls knapsack problem
def callKnapsack(w, v, C, n):
    global recursVals
    recursVals = [[None] * (C+1) ] * (n+1)
    return knapsack(w, v, C, n)

#Knapsack problem function
#I was trying to add a second weight which didn't work
#And when i redid the code for one weight it didnt work for some reason
#So now this code is broken and doesn't work
def knapsack(w, v, C, n):

    #if the value for n items and C capacity exists, use the value stored
    if recursVals[n][C] != None:
        return recursVals[n][C]

    #Base case - check if n or C is 0, return 0
    if n == 0 or C == 0:
        return 0

    #initialise result
    result = 0

    #if weight at n is greater than c recursively call this function
    # without adding the current element to the knapsack
    if w[n] > C:
        result = knapsack(w, v, C, n - 1)
    #otherwise take the max of recursively calling this function while adding this current element
    # in the knapsack and when not including this element
    else:
        result = max(knapsack(w, v, C, n - 1), v[n] + knapsack(w, v, C - w[n], n - 1))
    
    #store the result of these n and C values and store it in the memory array
    # return result
    recursVals[n][C] = result
    return result