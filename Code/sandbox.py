from re import X

def add(x, y):
    return x + y

def larger(x, y):
    if x > y:
        return x
    else:
        return y

def xor(x, y):
    if (x and not y) or (y and not x):
        return True
    else:
        return False

def hello(n):
    for i in range(n + 1):
        print("hello")

def fraction(n):
    return float(n)

def factorial(n):
    if n <= 1:
        return 1
    return (n * factorial(n - 1))

#print(factorial(4))
#print(factorial(9))

def makePyramid(x):
    for i in range (x):
        for j in range(i):
            print("#", end = '')
        print("")
    #return None

#makePyramid(5)

#book = ["Minor","Feelings","by","Cathy", "Park", "Hong"]
#print(book[0])
#story = { 
# "title": "Invisible Planets", 
# "author": "Hao Jingfang", 
# "published": 2013 
#} 

#story["words"] = 6359
#story["title"] = "Folding Beijing"
#print(story)
#for x in story: 
# print(x) 

def count(strArray):
    dic = {
        
    }
    for x in strArray:
        if not x in dic:
            dic[x]= 1
        else:
            dic[x]=dic[x] + 1
    return dic

print(count(["hello", "hello", "world", "hello"]))