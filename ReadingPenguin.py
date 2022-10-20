import csv 

penguinDic = {

    }

with open("penguins.csv", "r") as f:  
    data = csv.DictReader(f)

    def sumCount(string):
        if not row[string] == '':
            if string not in penguinDic[row['species']]:
                penguinDic[row['species']][string] = {'sum':float(row[string]), 'count':1}
            else:
                penguinDic[row['species']][string]['sum'] += float(row[string])
                penguinDic[row['species']][string]['count'] += 1

    def count(string):
        if not row[string] == '':
            if string not in penguinDic[row['species']]:
                penguinDic[row['species']][string] = {row[string]:1}
            elif row[string] not in penguinDic[row['species']][string]:
                penguinDic[row['species']][string][row[string]] = 1
            else:
                penguinDic[row['species']][string][row[string]] += 1

    #next(data)
    for row in data:
        #temp = {}
        if row['species'] not in penguinDic:
            penguinDic[row['species']] = {'count':1}
        else:
            penguinDic[row['species']]['count'] += 1

        """
        if not row['island'] == '':
            if 'island' not in penguinDic[row['species']]:
                penguinDic[row['species']]['island'] = {row['island']:1}
            elif row['island'] not in penguinDic[row['species']]['island']:
                penguinDic[row['species']]['island'][row['island']] = 1
            else:
                penguinDic[row['species']]['island'][row['island']] += 1
        """
        """
        if not row['bill_length_mm'] == '':
            if 'bill_length_mm' not in penguinDic[row['species']]:
                penguinDic[row['species']]['bill_length_mm'] = {'sum':float(row['bill_length_mm']), 'count':1}
            else:
                penguinDic[row['species']]['bill_length_mm']['sum'] += float(row['bill_length_mm'])
                penguinDic[row['species']]['bill_length_mm']['count'] += 1
        
        if not row['bill_depth_mm'] == '':
            if 'bill_depth_mm' not in penguinDic[row['species']]:
                penguinDic[row['species']]['bill_depth_mm'] = {'sum':float(row['bill_depth_mm']), 'count':1}
            else:
                penguinDic[row['species']]['bill_depth_mm']['sum'] += float(row['bill_depth_mm'])
                penguinDic[row['species']]['bill_depth_mm']['count'] += 1
        
        if not row['flipper_length_mm'] == '':
            if 'flipper_length_mm' not in penguinDic[row['species']]:
                penguinDic[row['species']]['flipper_length_mm'] = {'sum':float(row['flipper_length_mm']), 'count':1}
            else:
                penguinDic[row['species']]['flipper_length_mm']['sum'] += float(row['flipper_length_mm'])
                penguinDic[row['species']]['flipper_length_mm']['count'] += 1
        
        if not row['body_mass_g'] == '':
            if 'body_mass_g' not in penguinDic[row['species']]:
                penguinDic[row['species']]['body_mass_g'] = {'sum':float(row['body_mass_g']), 'count':1}
            else:
                penguinDic[row['species']]['body_mass_g']['sum'] += float(row['body_mass_g'])
                penguinDic[row['species']]['body_mass_g']['count'] += 1
        """
        """
        if not row['sex'] == '':
            if 'sex' not in penguinDic[row['species']]:
                penguinDic[row['species']]['sex'] = {row['sex']:1}
            elif row['sex'] not in penguinDic[row['species']]['sex']:
                penguinDic[row['species']]['sex'][row['sex']] = 1
            else:
                penguinDic[row['species']]['sex'][row['sex']] += 1

        if not row['year'] == '':
            if 'year' not in penguinDic[row['species']]:
                penguinDic[row['species']]['year'] = {row['year']:1}
            elif row['year'] not in penguinDic[row['species']]['year']:
                penguinDic[row['species']]['year'][row['year']] = 1
            else:
                penguinDic[row['species']]['year'][row['year']] += 1
        """

        count('island')
        sumCount('bill_length_mm')
        sumCount('bill_depth_mm')
        sumCount('flipper_length_mm')
        sumCount('body_mass_g')
        count('sex')
        count('year')

print(penguinDic)

#    w = open("color_page.txt", "w", encoding="utf8")

#    for dic in penguinDic:
#        w.write("\n" + dic + " : {")
#        for dic2 in penguinDic[dic]:
#            w.write("\n" + dic2 + " : " + str(penguinDic[dic][dic2]))
#        w.write("\n}\n")