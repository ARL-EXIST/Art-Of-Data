---
layout: post
title: TOM NOOK'S SOCKS
subtitle: they belong to Tom Nook
gh-repo: daattali/beautiful-jekyll
gh-badge: [star, fork, follow]
tags: [test]
comments: true
---

{: .box-note}
**Note:** Collaborator(s) - N/A (in class discussion with class members)

## Tasks
## *Task*
Use the provided API to generate a ```csv``` file, which you will then analyze with Python.

Write a blog post that addresses the following prompts. For questions about the dataset, be sure to explain how your code answers the question.

1. Discuss how you used the API to obtain the dataset.
2. Which sock has the most variations? If there is more than one answer, then list all of them.
3. How many socks of each color are there? If a sock has two different colors, it should be counted in both. However, if a sock has the same Color1 and Color2, make sure you don’t double count it!
4. Discuss your process of how you worked on this lab. Include details such as who you worked with, what methods you tried, what worked or didn’t work, what could have gone better, and what you learned during this lab. Focus more on the programming side of the lab! Feel free to attach images, screenshots, pseudocode, etc to elaborate on your response.
Submit your Python file(s) and a link to your blog post on Google Classroom.

## Answers:

### Question
1. Discuss how you used the API to obtain the dataset.

### Code:
{% highlight python linenos %}
#variables for final file
filepath = "../docs/Socks.csv"
fileDoesNotExist = not path.isfile(filepath)
remakeFile = False

# variables for accessing server - default get request of 1st index (0) from server
BASE_URL = "https://afeingoldhm.pythonanywhere.com"
ENDPOINT = "/socks"
API_KEY = "ArunArtOfDataKEY123ABCsecret"
index = 0
payload = {'key': API_KEY, 'idx': index}
response = requests.get(BASE_URL+ENDPOINT, params=payload)

#if the file doesn't exist or I want to remake it write/rewrite the file
# saves time if this program has already been run, as I can choose to remake the file, 
# and if the file doen't exist, a new one MUST be created
if(fileDoesNotExist or remakeFile):
    with open(filepath, "w") as f:
        
        #keys equals key values of sock dictionary
        keys = []

        if response.ok:
            data = response.json()
            for names in data:
                keys.append(names)

        #make a DictWriter with fieldnames as the columnheaders
        cleanWriter = csv.DictWriter(f, fieldnames=keys)
        cleanWriter.writeheader()

        #go through each sock until no more are available (when response.ok == false)
        # each loop increases index by 1
        # write the dictionary to the next row of the csv
        while(response.ok):
            #effectively a "loading bar" to know program is running and ~ how long until it finishes
            print(index)

            data = response.json()
            cleanWriter.writerow(data)

            response = requests.get(BASE_URL+ENDPOINT, params=payload)
            index += 1
            payload = {'key': API_KEY, 'idx': index}
{% endhighlight %}

### Explanation

* # variables for accessing server - default get request of 1st index (0) from server
* BASE_URL = "https://afeingoldhm.pythonanywhere.com"
* ENDPOINT = "/socks"
* API_KEY = "ArunArtOfDataKEY123ABCsecret"
* index = 0
* payload = {'key': API_KEY, 'idx': index}
* response = requests.get(BASE_URL+ENDPOINT, params=payload)
* {% endhighlight %}

these are the url paths and parameter for accessing the socks server and making a request. Each request will grab a sock depending on the ```index``` provided. The program starts by calling the sock with index 0. 

* #variables for final file
* filepath = "../docs/Socks.csv"
* fileDoesNotExist = not path.isfile(filepath)
* remakeFile = False

I also have a bool to decide whether I want the file to be rewritten, but if no file exists at the location, a new file is written no matter what.

Once the file is open I go through the key values from the first response/sock, and put them in an array called ```keys```. I then make a ```DictWriter()``` using ```keys``` as the ```fieldnames``` parameter, which gives each row the header/dictionary key values in the ```keys``` array. Then I use a while loop with ```request.ok```. Each loop ```index``` increases by 1 and a new request is made, so the while loop runs until ```index``` gives an invalid request. 
Each loop the sock dictionary given from the request is entered into the next row of the ```csv```.
Each loop also prints the value of ```index``` to serve as a loading bar to know how much progress until the file is written and to know that the program is running/requests are being made. 

### Notes

This was the hardest and most interesting section of the code to do and finish. this was my first full implementations of API's and helped me understand how server adresses work, as well as how parameters work (specifically due to figuring out how ```index``` fit into ```requests``` and using ```requests.ok``` for the while loop).
I also learnt how to use a ```DictWriter()``` which I had to learn a little extra documentation about the csv such as the fieldnames parameter.

### Question
2. Which sock has the most variations? If there is more than one answer, then list all of them.

### Answer:

argyle crew socks, color-blocked socks, frilly knee-high socks, holey tights, kiddie socks, mixed-tweed socks, no-show socks, semi-opaque socks, semiopaque tights, sequin leggings, simple-accent socks, striped socks, striped tights, tube socks, ultra no-show socks, vivid leggings, vivid socks, vivid tights, all have 8 variations.

### Code:
{% highlight python linenos %}
# read csv and get/return/print desired data from it
with open(filepath, "r") as g:
    table = csv.DictReader(g)

    # go through csv and add each name to variations dictionary and increase it by 1 every time it repeats
    variations = {}
    for rows in table:
        n = rows["Name"]
        if(n in variations.keys()):
            variations[n] += 1
        else:
            variations[n] = 1

    #reset fileReaders position
    g.seek(0)
    
    # get an array of key values from  which have the largest values, print them
    maxKeys = getMaxDictValue(variations)
    print("\nLIST OF SOCKS WITH MOST VARIATION = ")
    for k in maxKeys:
        print(str(k) + ", ")
    print("all have " + str(variations[k]) + " variations")
{% endhiglight %}

{% highlight python linenos %}
#method to return max Value(s) in a dictionary with key:value pairs of string:int
def getMaxDictValue(dic):
    tempMax = 0
    maxKey = []
    for k in dic:
        #if this key has an identical int size to the current maxKey count, add it to the list of key values
        if tempMax == dic[k]:
            maxKey.append(k)
        #if this key has a larger int size to the current maxKey count, reset the list and add this key to it
        elif tempMax < dic[k]:
            tempMax = dic[k]
            maxKey = [k]
    return maxKey
{% endhiglight %}

### Explanation
Make the ```csv``` and ```DictReader()```
Check the Name of each sock on each row and add it to the ```variations``` dictionary with a count of 1, if it has already been added to the dictionary (meaning it's a repeat) increase the count of the dictionary value by 1.
```g.seek(0)``` sets the file reader's position back to the start so next time the file is read it reads from the correct position.
The ```getMaxDictValue()``` function is called on the ```variations``` dictionary. This function grabs the key value with the largest value and returns it in a list. If a key has the same value (but not greater), it is added to this list. If a key has a greater value the array is reset. The function returns a list of all the key values in the dictionary which contain the greatest value which then get printed along with the number of variations.

### Notes



### Question
3. How many socks of each color are there? If a sock has two different colors, it should be counted in both. However, if a sock has the same Color1 and Color2, make sure you don’t double count it!

### Answer:

aerobics leggings have 12 colors, Aran-knit socks have 6 colors, argyle crew socks have 16 colors, back-bow socks have 12 colors, bobby socks have 4 colors, color-blocked socks have 16 colors, compression tights have 10 colors, country socks have 8 colors, crocheted socks have 4 colors, denim leggings have 4 colors, dotted knee-high socks have 4 colors, embroidered-flower tights have 12 colors, everyday socks have 6 colors, everyday tights have 6 colors, fishnet, tights have 3 colors, flowery-dot tights have 8 colors, frilly knee-high socks have 16 colors, frilly socks have 11 colors, funny-face socks have 10 colors, garter socks have 4 colors, geometric-print socks have 12 colors, hand-knit socks have 3 colors, holey socks have 3 colors, holey tights have 8 colors, horizontal-striped tights have 11 colors, Kerokerokeroppi socks have 2 colors, kiddie socks have 16 colors, Kiki & Lala socks have 2 colors, knee bandages have 1 colors, knee braces have 10 colors, Labelle socks have 6 colors, Labelle tights have 6 colors, lace socks have 9 colors, layered socks have 12 colors, leg warmers have 6 colors, mixed-tweed socks have 8 colors, neon leggings have 10 colors, neon tights have 10 colors, no-show socks have 16 colors, Nook Inc. socks have 2 colors, nordic socks have 14 colors, patterned stockings have 2 colors, pom-pom socks have 10 colors, puckered socks have 5 colors, running tights have 8 colors, semi-opaque socks have 8 colors, semi-opaque tights have 8 colors, sequin leggings have 8 colors, sheer socks have 6 colors, simple knee-high socks have 4 colors, simple-accent socks have 16 colors, soccer socks have 14 colors, spider-web tights have 4 colors, stockings have 5 colors, stretch leggings have 7 colors, striped socks have 16 colors, striped tights have 16 colors, tabi have 3 colors, terry-cloth socks have 14 colors, tube socks have 16 colors, ultra no-show socks have 8 colors, vivid leggings have 8 colors, vivid socks have 8 colors, vivid tights have 8 colors, wave-print socks have 9 colors.

### Code:
{% highlight python linenos %}
# read csv and get/return/print desired data from it
with open(filepath, "r") as g:
    table = csv.DictReader(g)

{% endhiglight %}
{% highlight python linenos %}
    # go through csv and add each name to variations dictionary and count it twice every time it repeats
    # unless Color 1 and Color 2 are the same in which case count it for 1
    colorsOfType = {}
    for row in table:
        names = row["Name"]
        cOne = row["Color 1"]
        cTwo = row["Color 2"]
        if(names in colorsOfType.keys()):
            if(cOne == cTwo):
                colorsOfType[names] += 1
            else:
                colorsOfType[names] += 2
        else:
            if(cOne == cTwo):
                colorsOfType[names] = 1
            else:
                colorsOfType[names] = 2
    g.seek(0)

    print("\nNUMBER OF COLORS OF EACH SOCK = ")
    # prints the number of colors of socks and ignores Name key in dictionary
    for i in colorsOfType:
        #for some reason colorsOfType dictionary contains Names as a key value even though variations does not
        if not i == "Name":
            print(str(i) + " has " + str(colorsOfType[i]) + " colors")
{% endhiglight %}

### Explanation

This code runs in the same ```with open``` command as the previous question's code.
Going through each row, ```Name```, ```Color 1```, and ```Color 2``` values are taken and used to construct the ```colorsOfType``` dictionary. This loop works the same as the loop for making the ```variations``` dictionary, except if cOne != cTwo, it is counted twice. Then the key:value pairs in the dictionary are printed out.

### FULL CODE
{% highlight python linenos %}
import requests
import csv
from pickletools import read_bytes1
import os.path
from os import path

#I tried having a class to store fileReader to keep everything contained, 
# as well as to try to make it so I didn't have to reset the position of the reader
"""class SockCsv:
    def __init__(self, fileReader):
        self.file = fileReader
        self.rows = self.getNumRows()

    def getColumn(self, columnHeader):
        if not columnHeader in self.file.__next__():
            print("No columnHeader exists with used name")
            return 1
        arr = []
        for rows in self.file:
            arr.append(rows[columnHeader])
        return arr

    def getNumRows(self):
        count = 0
        for rows in self.file:
            count += 1
        return count"""

#method to return max Value(s) in a dictionary with key:value pairs of string:int
def getMaxDictValue(dic):
    tempMax = 0
    maxKey = []
    for k in dic:
        #if this key has an identical int size to the current maxKey count, add it to the list of key values
        if tempMax == dic[k]:
            maxKey.append(k)
        #if this key has a larger int size to the current maxKey count, reset the list and add this key to it
        elif tempMax < dic[k]:
            tempMax = dic[k]
            maxKey = [k]
    return maxKey

#variables for final file
filepath = "../docs/Socks.csv"
fileDoesNotExist = not path.isfile(filepath)
remakeFile = False

# variables for accessing server - default get request of 1st index (0) from server
BASE_URL = "https://afeingoldhm.pythonanywhere.com"
ENDPOINT = "/socks"
API_KEY = "ArunArtOfDataKEY123ABCsecret"
index = 0
payload = {'key': API_KEY, 'idx': index}
response = requests.get(BASE_URL+ENDPOINT, params=payload)

#if the file doesn't exist or I want to remake it write/rewrite the file
# saves time if this program has already been run, as I can choose to remake the file, 
# and if the file doen't exist, a new one MUST be created
if(fileDoesNotExist or remakeFile):
    with open(filepath, "w") as f:
        
        #fieldnames equals key values of sock dictionary
        keys = []

        if response.ok:
            data = response.json()
            for names in data:
                keys.append(names)

        #make a DictWriter with fieldnames as the columnheaders
        cleanWriter = csv.DictWriter(f, fieldnames=keys)
        cleanWriter.writeheader()

        #go through each sock until no more are available (when response.ok == false)
        # each loop increases index by 1
        # write the dictionary to the next row of the csv
        while(response.ok):
            #effectively a "loading bar" to know program is running and ~ how long until it finishes
            print(index)
            
            data = response.json()
            cleanWriter.writerow(data)

            response = requests.get(BASE_URL+ENDPOINT, params=payload)
            index += 1
            payload = {'key': API_KEY, 'idx': index}


# read csv and get/return/print desired data from it
with open(filepath, "r") as g:
    table = csv.DictReader(g)

    # go through csv and add each name to variations dictionary and increase it by 1 every time it repeats
    variations = {}
    for rows in table:
        n = rows["Name"]
        if(n in variations.keys()):
            variations[n] += 1
        else:
            variations[n] = 1

    #reset fileReaders position
    g.seek(0)
    
    # get an array of key values from  which have the largest values, print them
    maxKeys = getMaxDictValue(variations)
    print("\nLIST OF SOCKS WITH MOST VARIATION = ")
    for k in maxKeys:
        print(str(k) + ", ")
    print("all have " + str(variations[k]) + " variations")


    # go through csv and add each name to variations dictionary and count it twice every time it repeats
    # unless Color 1 and Color 2 are the same in which case count it for 1
    colorsOfType = {}
    for row in table:
        names = row["Name"]
        cOne = row["Color 1"]
        cTwo = row["Color 2"]
        if(names in colorsOfType.keys()):
            if(cOne == cTwo):
                colorsOfType[names] += 1
            else:
                colorsOfType[names] += 2
        else:
            if(cOne == cTwo):
                colorsOfType[names] = 1
            else:
                colorsOfType[names] = 2
    g.seek(0)

    print("\nNUMBER OF COLORS OF EACH SOCK = ")
    # prints the number of colors of socks and ignores Name key in dictionary
    for i in colorsOfType:
        #for some reason colorsOfType dictionary contains Names as a key value even though variations does not
        if not i == "Name":
            print(str(i) + " has " + str(colorsOfType[i]) + " colors")
{% endhiglight %}
