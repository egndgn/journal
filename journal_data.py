import csv
import requests
import xml.etree.ElementTree as ET

liste = []
liste_csv = open("journal_data.csv", "w", encoding='utf-8')

with open('journal_csv.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        j = row[1]
        j_link = "https://dblp.org/search/publ/api?q=stream%3Astreams%2Fjournals%2F"+j+"%3A&h=1000&format=xml"

        response = requests.get(j_link)
        with open('api.xml', 'wb') as file:
            file.write(response.content)
        
        tree = ET.parse('api.xml')
        root = tree.getroot()
        
        for child in root.findall('hits'):
            for childd in child.findall('hit'):
                for childdd in childd.findall('info'):
                    if (childdd.find('venue') is not None) and (childdd.find('volume') is not None) and (childdd.find('year') is not None) and (childdd.find('title') is not None):
                        venue = childdd.find('venue').text
                        volume = childdd.find('volume').text
                        year = int(childdd.find('year').text)
                        title = childdd.find('title').text
            
            
                    if year>=2019:
                        liste.append(venue)
                        liste.append(volume)
                        liste.append(year)
                        liste.append(title)   
            
                    if len(liste)>0:
                        liste_csv.write(str(liste) + "\n")
                liste = []
        
           
