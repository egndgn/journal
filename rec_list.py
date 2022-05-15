import csv

result_csv = open("ttl_reclist.csv", "w", encoding='utf-8')


for pid in range(1,100):
    sim_list = []
    rec_list = []
    with open('result_ttl.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                paper_id = row[0]
                
                if pid==int(paper_id):
                   sim_list.append(row)
    
    sim_list = sorted(sim_list, key = lambda paper: paper[2], reverse=True)
    
    for i in range(100):
        rec_list.append(sim_list[i])
        
    for rec in rec_list:
        result_csv.write(str(rec[0])+","+str(rec[1])+","+str(rec[2])+"\n")
        print(str(rec[0])+","+str(rec[1])+","+str(rec[2]))
                                     
      
    