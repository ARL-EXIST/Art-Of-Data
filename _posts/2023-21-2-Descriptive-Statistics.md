---
layout: post
title: Descriptive Statistics
subtitle: nintendo ds
gh-repo: daattali/beautiful-jekyll
gh-badge: [star, fork, follow]
tags: [test]
comments: true
---

{: .box-note}
**Note:** Collaborator(s) - N/A

{: .box-note}
**Note:** Stack overflow used to help with datetime, and use of apply function (https://sparkbyexamples.com/pandas/pandas-apply-function-to-every-row/)

**This is my DS lab**


## Objectives
This lab is intended to evaluate your ability to:
. prepare a dataset for analysis
. calculate summary statistics for a dataset
. describe the distribution of a variable
. analyze associations between variables
. statistically describe a dataset with supporting evidence

## Task
Find a dataset on a topic that you are interested in. You will be writing a Python program (or notebook) to analyze this dataset. This time, you will try to draw conclusions about the dataset based on your analysis of summary statistics. You do not have to analyze every attribute of the entire dataset! You are welcome to analyze smaller sections of the dataset that youʼre interested in. Write a blog post for your website with responses to the following:
. Which dataset did you work with?
. Which aspect of this dataset are you interested in? What do you hope to learn from analyzing this dataset?
. Discuss your analysis of the dataset. Include details such as:
. The variables you looked at
. Distributions of variables (center and variability)
. Relationships between variables
. Visualizations of the dataset
. Limitations of your analysis and the dataset
. What conclusions can you draw about this dataset? What is your supporting evidence? Your blog post should showcase your understanding of the material covered in this unit.

## Academic Honesty
You are allowed to work with others on this lab, as long as you do not share any code or files! Please refer to
the syllabus for more details.
You are allowed to use modules we havenʼt talked about in class, as long as they are cited, and in your blog
post you include an explanation of how and why they are used.

## Answers:

### Question:
1. Which dataset did you work with?

### Answer:
I worked with the NYC accidents 2020 dataset

### Question:
2. Which aspect of this dataset are you interested in? What do you hope to learn from analyzing this dataset?

### Answer:
I was interested in finding connection and correlations in NYC crashes. Initially I had wanted to do a dataset concerning traffic flow in NYC but after struggling to find one that was suitable and spanned over more than a few days, I went with the NYC crash dataset. I was interested principally in learning what factors might see an increase in crashes, such as location, vehicle type, or time of day, and what might correlate with an increase in injury/death.

### Analysis:

  The principle variables I looked at were Time, Number of Persons Injured and/or Killed and Contributing Factors. The clearest graphable connection is the number of crashes compared to the time of day. The first graph shows a histogram of crashes during 24 different  time periods (24 hours, each bin representing 1 hour), along with the number of  crashes depending on the borough sorted by highest frequencies top to bottom. The graph clearly shows a significant jump in number of crashes after 8:00 from roughly 1500 to 2500 crashes. After that the graph fluctuates but there is no significant visible jump between any hours and the number of crashes. Between 8:00 and 20:00, there appears to be the most crashes, ranging from 2500 crashes to 3500 at 17:00. In terms of how dangerous or risky it is to drive at different times, we would expect later hours, such as between 20:00 and 8:00 to be most risky due to it being dark and drivers having less visibility. While it is tempting to say the opposite is true, the increase in crashes between 8:00 and 20:00 is likely due to more drivers being on the road at those times. This reflects a problem with a decent amount of the data and graphs made. For a lot of the variables and any correlations found it is hard to judge that any factor is linked to an increased risk of crashes is impossible without first assuming that the number of cars on the road is constant. If there are more cars on the road at a given time, then obviously there are more chances for crashes to happen, so we would expect more crashes. Without data to reflect traffic levels at different times, it is hard to judge that there is an increased risk of crashes. This works for car type as well, as if lots of sedans are on the road, there will obviously be a high number of sedan crashes. That being said, it is more feasable to judge factors about the actual crash that happened, such as how many injuries there were compared to the number of crashes. In this first graph I also allowed hues to represent the borough just to show the number of crashes for different boroughs along with time. The boroughs all roughly follow the same overall relationship with time, increasing the number of crashes primarily at 8:00 and lowering after 20:00.
  I then decided to analyse the 

### Code:
{% highlight python linenos %}

{% endhighlight %}
