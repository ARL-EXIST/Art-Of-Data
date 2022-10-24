---
layout: post
title: Digimon Lab
subtitle: dawn of the digimon
gh-repo: daattali/beautiful-jekyll
gh-badge: [star, fork, follow]
tags: [test]
comments: true
---

## Boxes
I apologise for the background which might make some things harder to read!

## Boxes
Collaborator: Henry
videos watched for knapsack problem: https://youtu.be/xOlhR_2QCXY, https://youtu.be/dT6dvdbpChA

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

**Question**
1.  What is the average speed (```Spd```) of all Digimon?

**Code:**
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

**Explanation**
For this function I went through each row using ```for rows in data:```. I had two variables ```suum``` and ```count```, one to take the sum of all values in a specific ```header```'s column, and another to count the number of rows where I added a value to ```suum```. And then to get the average I just divided ```suum``` by ```count```.

**Question**
2.  Write a function that can count the number of Digimon with a specific attribute. For example, count_digimon("Type", "Vaccine") would return 70.

**Code:**
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
{% endhighlight %}

**Explanation**
For this function I take a ```header``` and ```specifier```. ```Attribute``` is effectively a count tracker, which increases when the ```header``` value for each row matches the given ```Specifier```.
