import csv

fixMappings=[]

with open('fixMappings.csv') as fm:
    reader = csv.DictReader(fm)
    tagFields ={}
    for row in reader:
        tagfields = {row['Tag']:row['Field']}
        fixMappings.append(tagfields)

print(fixMappings[40])
