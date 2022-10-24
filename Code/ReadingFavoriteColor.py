import csv 
gradeDic = {
    "total":{

    }
    }
with open("datasets/favorite_colors.csv", "r") as f:  
    data = csv.reader(f) 

    next(data)
    for row in data:
        temp = {}
        if not row[0] in gradeDic:
            gradeDic[row[0]] = {row[1]:1}
        elif not row[1] in gradeDic[row[0]]:
            gradeDic[row[0]][row[1]] = 1
        else:
            gradeDic[row[0]][row[1]] += 1
        
        if not row[1] in gradeDic["total"]:
            gradeDic["total"][row[1]] = 1
        else:
            gradeDic["total"][row[1]] += 1
        if not row[0] in gradeDic["total"]:
            gradeDic["total"][row[0]] = 1
        else:
            gradeDic["total"][row[0]] += 1
        #print(row)

    w = open("color_page.txt", "w", encoding="utf8")

    for dic in gradeDic:
        w.write("\n" + dic + " : {")
        for dic2 in gradeDic[dic]:
            w.write("\n" + dic2 + " : " + str(gradeDic[dic][dic2]))
        w.write("\n}\n")

    #print(gradeDic)