import csv


with open('fixMappings.csv') as fm:
    reader = csv.DictReader(fm)
    tagFields ={}
    for row in reader:
        tagFields[row['Tag']] = row['Field']

    print(tagFields['40'])

