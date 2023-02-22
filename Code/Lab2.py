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
filepath = "Socks.csv"
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

    #add colour1 to dictionary or increase count by 1
    #if colour2 is not the same also add it to the dictionary or increase the count by 1
    colorsOfType = {}
    for row in table:
        cOne = row["Color 1"]
        cTwo = row["Color 2"]
        if(cOne in colorsOfType.keys()):
            colorsOfType[cOne] += 1
        else:
            colorsOfType[cOne] = 1
        if(cOne != cTwo):
            if(cTwo in colorsOfType.keys()):
                colorsOfType[cTwo] += 1
            else:
                colorsOfType[cTwo] = 1
    g.seek(0)

    print("\nNUMBER OF COLORS OF EACH SOCK = ")
    # prints the number of colors of socks and ignores Name key in dictionary
    for i in colorsOfType:
        #for some reason colorsOfType dictionary contains Names as a key value even though variations does not
        if not (i == "Color 1" or i == "Color 2"):
            print("there are " + str(colorsOfType[i]) + " socks that are " + str(i))