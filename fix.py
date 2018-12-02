import csv
FIXVer=''
def validFIXVersion(allfixVersions):
    fixFiles={}
    fixFiles['FIX.4.2'] = 'fixMappings_42.csv'
    fixFiles['FIX.4.4'] = 'fixMappings_44.csv'
   
    for i in allfixVersions:
        if i in fixFiles:
            next
        else:
            return -1
        if len(set(allfixVersions)) == 1:
            return 1
        else:
            return 0

with open('fix.csv') as mycsv:
    csv_reader = csv.reader(mycsv, delimiter=",")

    fixVersions=[]
    #Create the list to store all rows as a dictionary
    for row in csv_reader:
        my_dict = {}
        for kvpair in row:
            #Split our FIX Value pair to key and value
            k,v = kvpair.split("=")
            
            # Proceed to assign all other tags
            my_dict[k] = v    

        # Determine the correct FIX version map to use
        fixVersions.append(my_dict['8'])
    fixOK = validFIXVersion(fixVersions)
    if(fixOK==-1):
        print("Unsupported FIX Version")
    elif(fixOK==0):
        print("Not all lines are the same FIX version, please correct")
    else:
        print("Can proceed")
        
mycsv.close()

# Open FIX mappings and add them to the dictionary
with open('fixMappings_42.csv') as fm:
    reader = csv.DictReader(fm)
    tagFields ={}
    for row in reader:
        tagFields[row['Tag']] = row['Field']

# Open your FIX messages put each row into a dictionary and each dictionary into a list of all rows
with open('fix.csv') as mycsv:
    csv_reader = csv.reader(mycsv, delimiter=",")

    #Create the list to store all rows as a dictionary
    fixDict=[]
    for row in csv_reader:
        my_dict = {}
        for kvpair in row:
            #Split our FIX Value pair to key and value
            k,v = kvpair.split("=")
            
            # Proceed to assign all other tags
            my_dict[tagFields[k]] = v    

        # Determine the correct FIX version map to use
        firstFIXVer = my_dict['8']
        validFixVersion(firstFIXVer)
        
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
