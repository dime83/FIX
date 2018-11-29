import csv

with open('fix.csv') as mycsv:
    csv_reader = csv.reader(mycsv, delimiter=",")
    fixDict=[]
    for row in csv_reader:
        my_dict = {}
        for kvpair in row:
            #Split our FIX Value pair to key and value
            k,v = kvpair.split("=")
            my_dict[k] = v    
        fixDict.append(my_dict)

    for element in fixDict:
        print(element)
mycsv.close()

with open('convertedfix.csv', mode='w') as converted_fix:
    fieldnames = ['40','55','38']
    writer = csv.DictWriter(converted_fix,fieldnames=fieldnames,extrasaction='ignore')

    writer.writeheader()
    for i in fixDict:
        writer.writerow(i)
