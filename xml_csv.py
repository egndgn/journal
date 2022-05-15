import xml.etree.ElementTree as Xet
import pandas as pd
  
cols = ["venue", "year", "volume", "title"]
rows = []

xmlparse = Xet.parse('api.xml')
root = xmlparse.getroot()
for i in root.findall('hits'):
    venue = i.find("venue").text
    year = i.find("year").text
    volume = i.find("volume").text
    title = i.find("title").text
  
    rows.append({"venue": venue,
                 "year": year,
                 "volume": volume,
                 "title": title})
  
df = pd.DataFrame(rows, columns=cols)

df.to_csv('output.csv')