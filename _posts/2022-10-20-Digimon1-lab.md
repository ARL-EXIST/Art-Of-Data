---
layout: post
title: Digimon Lab
subtitle: dawn of the digimon
gh-repo: daattali/beautiful-jekyll
gh-badge: [star, fork, follow]
tags: [test]
comments: true
---

{: .box-note}
**Note:** I apologise for the background which might make some things harder to read!

{: .box-note}
**Note:** Collaborator: Henry
{: .box-note}
**Note:** videos watched for knapsack problem: https://youtu.be/xOlhR_2QCXY, https://youtu.be/dT6dvdbpChA

**This is my Digimon lab**


## Tasks
Write a blog post for your website with responses to the following:


1.  What is the average speed (```Spd```) of all Digimon? 
2.  Write a function that can count the number of Digimon with a specific attribute. For example, ```count_digimon("Type", "Vaccine")``` would return 70.
3.  The Digimon on your team are restricted by the total amount of ```Memory``` that they need. If your team only has ```15 Memory```, name a team of up to 3 Digimon that has at least 300 attack (```Atk```) in total.
4.  Describe your process in finding these answers. Include details such as who you worked with, what methods you tried, what worked or didn’t work, what could have gone better, and what you learned during this lab. Feel free to attach images, screenshots, pseudocode, etc to elaborate on your response!

Submit your Python file using Google Classroom. You can also find the rubric there.

## Answers:

For all of these functions I decided to use DictReader as this allowed me to access a given column by using a name, rather than the element of a row, which I found easier to read while coding.

### Question
1.  What is the average speed (```Spd```) of all Digimon?

### Code:
{% highlight python linenos %}
#go through each row, add the value found in a specified column and add that to the suum
#count increases by one every time a value gets added to sum
#divide suum by count to get the average
def average(header):
    with open("../datasets/digimon.csv", "r") as f:  
        data = csv.DictReader(f)

        suum = 0
        count = 0

        for rows in data:
            suum += int(rows[header])
            count += 1

        average = suum/count

        return average

#calls function – find average speed – and prints the result in terminal
print("Average Speed is: %.2f" % average("Spd"))
{% endhighlight %}

### Explanation
For this function I went through each row using ```for rows in data:```. I had two variables ```suum``` and ```count```, one to take the sum of all values in a specific ```header```'s column, and another to count the number of rows where I added a value to ```suum```. And then to get the average I just divided ```suum``` by ```count```.

### Question
2.  Write a function that can count the number of Digimon with a specific attribute. For example, count_digimon("Type", "Vaccine") would return 70.

### Code:
{% highlight python linenos %}
#Takes header to knapsack the correct column and matches all pokemon whose header value is the specifier
#to knapsack how many pokemon have that specific specifier
def count_digimon(header, specifier):
    with open("../datasets/digimon.csv", "r") as f:  
        data = csv.DictReader(f)

        attribute = 0

        for rows in data:
            #checks if column value is specifier
            if ((rows[header]) == specifier):
                attribute += 1
    
        return (attribute)
        
#calls function – count digimon of Type - Vaccine – and prints the result in terminal
print("The number of digimon of Type Vaccine is : " + str(count_digimon("Type","Vaccine")))
{% endhighlight %}

### Explanation
For this function I take a ```header``` and ```specifier```. ```Attribute``` is effectively a count tracker, which increases when the ```header``` value for each row matches the given ```Specifier```.

### Question
3.  The Digimon on your team are restricted by the total amount of ```Memory``` that they need. If your team only has ```15 Memory```, name a team of up to 3 Digimon that has at least 300 attack (```Atk```) in total.

### Code:
{% highlight python linenos %}
#combination of at most 3 Digimon with at most memoryMax and at least attackMin
#Returns the Number of the Digimon to use
def attack_limit(memoryMax, attackMin):
    with open("../datasets/digimon.csv", "r") as f:  
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
#then check wether the x or the x + y, or the x + y + z, combo adds up to 300 or more within memory confines
#This function requires that you are searching for a combo with at most 3 elements/digimon
#does not work for bigger or smaller group compositions - hard coded for 3 group size
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
    
#calls function – Find combo of up to 3 digimon that have at most 15 memory, and at least 300 attack – and prints result in terminal
print("Digimon – " + str(attack_limit(15, 300)) + " – have at least 300 combined attack and within 15 combined memory")
{% endhighlight %}

### Explanation
Stuff
