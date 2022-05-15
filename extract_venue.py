import csv

venue_csv = open("venue.csv", "w", encoding='utf-8')
liste = []

with open('journal_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        venue = row[0]
        
        if venue not in liste:
            liste.append(venue)
            venue_csv.write(venue + "\n")
            print(venue)
        