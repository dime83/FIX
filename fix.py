import csv

# Open FIX mappings and add them to the dictionary
with open('fixMappings.csv') as fm:
    reader = csv.DictReader(fm)
    tagFields ={}
    for row in reader:
        tagFields[row['Tag']] = row['Field']

# Open your FIX messages put each row into a dictionary and each dictionary into a list of all rows
with open('fix.csv') as mycsv:
    csv_reader = csv.reader(mycsv, delimiter=",")
    fixDict=[]
    for row in csv_reader:
        my_dict = {}
        for kvpair in row:
            #Split our FIX Value pair to key and value
            k,v = kvpair.split("=")
            my_dict[tagFields[k]] = v    
        fixDict.append(my_dict)

    for element in fixDict:
        print(element)
mycsv.close()

with open('convertedfix.csv', mode='w') as converted_fix:
    fieldnames = ['MsgType','Symbol','OrdType']
    writer = csv.DictWriter(converted_fix,fieldnames=fieldnames,extrasaction='ignore')

    writer.writeheader()
    for i in fixDict:
        writer.writerow(i)
