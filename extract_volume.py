import csv

volume_csv = open("volume.csv", "w", encoding='utf-8')
liste_volume = []
liste_venue = []

with open('venue.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        liste_venue.append(row[0])
        
for venue_name in liste_venue:
    with open('journal_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # print(row[1])
            venue = row[0]
            volume = row[1]
            
            if (venue_name == venue) and (volume not in liste_volume):
                liste_volume.append(int(volume))
    
    max_volume = 0
    for i in liste_volume:
        if i>max_volume:
            max_volume = i
    
    volume_csv.write(str(venue_name)+","+str(max_volume)+"\n")
    
    liste_volume = []
