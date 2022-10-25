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
**Note:** I apologise for the background which might make some things harder to read! I probably should have left it to plain white, but otherwise this is the best background in terms of reading the words, that I had. Other backgrounds were too annoying to read on.

{: .box-note}
**Note:** Collaborator(s) - Henry

{: .box-note}
**Note:** videos watched for knapsack problem: https://youtu.be/xOlhR_2QCXY, https://youtu.be/dT6dvdbpChA

{: .box-note}
**Note:** GeeksForGeeks

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

        #if x alone is greater than aMin, return only x (all elements in m are 15 or less)
        if a[x] >= aMin:
            return x, None, None

        #only check for an x + y combo if x <= mMax - 1, as y has a min value of 1
        if m[x] <= mMax-1:
            #Check each y value for x + y (+ z) combo where y is each next element after x
            for y in range(x-1, -1, -1):

                # if x + y is greater than aMin, and less than mMax, return x and y
                if a[x] + a[y] >= aMin and m[x] + m[y] <= mMax:
                    return x, y, None

                #if x + y memory > 14 then the combo with z is not within the Memory capacity
                if m[x] + m[y] <= mMax-1:
                    #Check each z value for x + y + z combo where z is each next element after y
                    for z in range(y, -1, -1):

                        #If the combo >= minimum value, then check memory
                        # else - no other z value will reach minimum (Attack) value needed
                        # (as the a array is sorted least to greatest) so break z for loop
                        # and iterate to next y value
                        if a[x] + a[y] + a[z] >= aMin:
                        
                            #If also Within memory constraints, return x, y, z
                            if m[x] + m[y] + m[z] <= mMax:
                                return x, y, z
                                
                        else:
                            break
    
    #Prints that no combo was found
    print("No combination adds to at least 300 attack AND within memory of 15")
    return None, None, None
    
#calls function – Find combo of up to 3 digimon that have at most 15 memory, and at least 300 attack – and prints result in terminal
print("Digimon – " + str(attack_limit(15, 300)) + " – have at least 300 combined attack and within 15 combined memory")
{% endhighlight %}

### Explanation, discussion and ways to improve
This piece of code uses three functions. 2 of the functions are called during the ```attack_limit``` function.
The attack_limit function runs as follows:

* open file
* create a 2 dimensional list called ```attackMem``` - a list that contains three lists. The 1st inner list is to contain the ```Attack``` values, the 2nd is to contain the ```Memory``` values, and the 3rd is to contain the ```Number``` of the digimon being referred to.
* A for loop then runs and checks to make sure the given row has a value for ```Attack```, ```Memory```, and ```Number```, and that the memory value is within 15
    - Then add  ```Attack``` values to the 1st list in ```attackMem``` with binary insert so as to make the 1st list of ```attackMem``` sorted from least to greatest
    - add ```Memory``` and ```Number``` to matching indexes in their lists
* The ```attackMem``` list should be sorted for the ```Attack``` values in the 1st list, with corresponding ```Memory``` and ```Number``` values in corresponding indexes in the other 2 lists
* call ```MemTotCheck``` on ```AttackMem``` list to get up to 3 index values that meet restrictions on ```Attack``` and ```Memory```
    - 3 for loops –– ```x```, ```y```, ```z``` –– go through each possible combination of digimon from the given list
    - ```x```iterates through each index in the list (top to bottom), ```y``` iterates through each index after ```x``` (from top to bottom), and ```z``` iterates through each index after ```x``` (from top to bottom)
    - since the attack list is organised smallest to biggest, if an ```x``` + ```y``` + ```z``` combo fails to reach the minAttack, then no succeeding ```z``` values will reach minAttack, so you can skip to the next iteration of ```y```
    - before each for loop, check the current combo value (e.g only ```x```, or only ```x``` + ```y```) to see if they fulfill the requirements. If so, return only 1 (```x```) or 2 (```x``` + ```y```) elements
* return the number of the digimon(s) that fulfill the combo

This code was fairly simplet to write as I wrote a method for binary sort, and another with three for loops iterating over each value, each for loop living within the previous for loop. One big limitation of this function is that ```memTotCheck``` is hardcoded to return up to 3 digimons/indexes. To stop this, you could write a recursive function - pseudocode:

~~~
def memTotCheck(Memory, Attack, number, maxMem, end):
#where Memory and Attack are lists, number is the amount of elements (digimon) to include, end is the current element (starting at the top), and maxMem #is the most Memory that can be used

if number or Capacity or end are 0: return 0

result = [0, None, None, None] #- the first index will act as the total value/attack added to this function, the next 3 as indexes which make up the value
#I will refer to the first element of result as val, and the next 3 as indexes

if Memory[end] > Capacity: call this function without adding the current element –– set result to the returned sum value

else if (the val value of calling this function while including this element(reduce number by 1, reduce MaxMem by Memory[end], and reduce end by 1) + Attack[end]) > than the val of calling this function with end - 1 (calling this function but not including this element)):
    result's val = the val of calling this function while including this element + Attack[end]
    result's next index = end
    go through the index elements of result which are not None and insert the index elements of (calling this function while including this element)

else: 
    result's val = the val of calling this function with end - 1
    go through the index elements of result which are not None and insert the index elements of (calling this function with end - 1)
return result
~~~

which would give you back the max combination value of Attack and the indexes of digimon used to make up that attack value —— given ```Memory```, ```Attack```, the ```Number``` of digimon to include, and ```len(Attack)-1``` (i.e the end index of the Attack or Memory lists).
The reason I did not implement a function like this in the final piece of code is because while I had tried to implement something somewhat similar to this recursive idea[^1], it did not work. So I did not want to write any more recursive functions and instead used 3 for loops.

 [^1]:See Knapsack Problem section

#### Knapsack Problem ####
Due to your mention of it in class, I decided to look into the Knapsack problem. The basic idea is that you take a default recursive function that tries both including and discluding the current item for each item of a weight and value list and finding the max of those two returned values. With dynamic coding, you add a memorization table to keep track of item and MaxWeight value, with each individual value being a subproblem of the larger problem, as when you reach an item and maxWeight value that you've reached before, you don't have to recursively check it again, as you've stored the value. I did manage to get a normal, 1 weight, knapsack problem code to function at some point in time, which felt pretty good. However afterwards I decided to implement a merged weight value to get over the hurdle of including only a limited number of digimon/items, as you had mentioned in class. This was a mistake. I struggled with this as I had forgotten some of what you had said in class, and found no online help other than pdf files which I could not understand as they were filled with calculus and DUTCH. I then tried to revert back to a regular knapsack problem piece of code. When I did this, however, the code did not work anymore. I tried to fix it, but I could not. I could not use the knapsack problem code to help me answer question 3 or even as a demonstation/proof of a code solution to the knapsack problem. So I gave up on it.

**The End**

knapsack code:
{% highlight python linenos %}
#Below is code that I wrote but unfortunately did not use because it didn't work for some reason


#attempted to merge 2 weights into one for knapsack problem
#code in knapsack function was slightly different when I used this function
"""def callknapsack(w, w_Two, v, C, C_Two, n):
    global recursVals
    recursVals = [[-1] * ((C_Two * 1000000) + C)]*n
    #print((C_Two * 1000) + C)
    mergeC = ((C_Two * 1000000) + C)
    return knapsack(w, w_Two, v, mergeC, n)"""

#makes a global 2d memory array of n by C, then calls knapsack problem
#this function did not exist when the code worked, but was implemented afterwards to try and fix whatever had stopped working in the code
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
{% endhighlight %}
