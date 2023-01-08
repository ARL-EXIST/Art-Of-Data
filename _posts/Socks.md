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
**Note:** Collaborator(s) - N/A (in class discussion)

## Tasks
## *Task*
Use the provided API to generate a csv file, which you will then analyze with Python.

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
makeNewFile = not path.isfile(filepath)

# variables for accessing server - default get request of 1st index (0) from server
BASE_URL = "https://afeingoldhm.pythonanywhere.com"
ENDPOINT = "/socks"
API_KEY = "ArunArtOfDataKEY123ABCsecret"
index = 0
payload = {'key': API_KEY, 'idx': index}
response = requests.get(BASE_URL+ENDPOINT, params=payload)

#if the file already exists dont write over the file
# saves time if this program has already been run, and prevents overwriting of another file that might have the same name and location
if(makeNewFile):
    #write sock csv
    with open(filepath, "w") as f:
        
        #fieldnames equals key values of sock dictionary
        fieldnames = []

        if response.ok:
            data = response.json()
            for names in data:
                fieldnames.append(names)

        #make a DictWriter with fieldnames as the columnheaders
        cleanWriter = csv.DictWriter(f, fieldnames=fieldnames)
        cleanWriter.writeheader()

        #go through each sock until no more are available (when response.ok == false)
        # each loop increases index by 1
        # write the dictionary to the next row of the csv
        while(response.ok):
            #effectively a "loading bar" to know program is running and ~ how long until it finishes
            print(index)
            
            #if response.ok:
            data = response.json()
            cleanWriter.writerow(data)

            response = requests.get(BASE_URL+ENDPOINT, params=payload)
            index += 1
            payload = {'key': API_KEY, 'idx': index}
{% endhighlight %}

### Explanation
