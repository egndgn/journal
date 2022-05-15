import csv

for pid in range(1,100):
    name_list_elsevier = []
    name_list_springer = []
    name_list_ieee = []
    name_list_wiley = []
    journals_elsevier = []
    journals_springer = []
    journals_ieee = []
    journals_wiley = []
    finder_list_elsevier = []
    finder_list_springer = []
    finder_list_ieee = []
    finder_list_wiley = []
    venue_list = []
    rec_list = []
    sayac = 0
    sayac_toplam = 0
    
    with open('volume.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                venue_list.append(row[0])
       
    
    #elsevier finder journals
    with open('elsevier.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            paper_id = row[0]
            
            if pid==int(paper_id):
                name_list_elsevier.append(row[1])
    
    with open('elsevier.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            journals_elsevier.append(row[0])
            
    for jname in name_list_elsevier:
        if jname in journals_elsevier:
            jid = journals_elsevier.index(jname)
            finder_list_elsevier.append(venue_list[jid])
               
    
    #springer finder journals
    with open('springer.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            paper_id = row[0]
            
            if pid==int(paper_id):
                name_list_springer.append(row[1])
    
    with open('springer.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            journals_springer.append(row[0])
            
    for jname in name_list_springer:
        if jname in journals_springer:
            jid = journals_springer.index(jname)
            finder_list_springer.append(venue_list[jid+167])
                        
            
    #wiley finder journals     
    with open('wiley.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            paper_id = row[0]
            
            if pid==int(paper_id):
                name_list_wiley.append(row[1])
    
    with open('wiley.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            journals_wiley.append(row[0])
            
    for jname in name_list_wiley:
        if jname in journals_wiley:
            jid = journals_wiley.index(jname)
            finder_list_wiley.append(venue_list[jid+433])


            
    #ieee finder journals        
    with open('ieee.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            paper_id = row[0]
            
            if pid==int(paper_id):
                name_list_ieee.append(row[1])
    
    with open('ieee.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            journals_ieee.append(row[0])
            
    for jname in name_list_ieee:
        if jname in journals_ieee:
            jid = journals_ieee.index(jname)
            finder_list_ieee.append(venue_list[jid+478])
            
                      
            
    #recommendation journals  
    with open('ttlkeyabstref_reclist.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            paper_id = row[0]
            
            if pid==int(paper_id):
                rec_list.append(row[1])
                
                           
    for rec in rec_list[:30]:
        if rec in finder_list_elsevier:
            # print(rec)
            sayac = sayac + 1
            sayac_toplam = sayac_toplam + 1
    print("Elsevier: >> Paper "+str(pid)+" - "+str(sayac))            
    
    sayac = 0       
    for rec in rec_list[:30]:
        if rec in finder_list_springer:
            sayac = sayac + 1
            sayac_toplam = sayac_toplam + 1
    print("Springer: >> Paper "+str(pid)+" - "+str(sayac))
    
    sayac = 0
    for rec in rec_list[:30]:
        if rec in finder_list_wiley:
            # print(rec)
            sayac = sayac + 1
            sayac_toplam = sayac_toplam + 1
    print("Wiley: >> Paper "+str(pid)+" - "+str(sayac))
    
    sayac = 0
    for rec in rec_list[:30]:
        if rec in finder_list_ieee:
            # print(rec)
            sayac = sayac + 1
            sayac_toplam = sayac_toplam + 1
    print("IEEE: >> Paper "+str(pid)+" - "+str(sayac))
    
    print("---------")           
    print("Toplam: >> Paper "+str(pid)+" - "+str(sayac_toplam))
    print("---------")