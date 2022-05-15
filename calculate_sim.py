import pandas as pd
import numpy as np
import math
from numpy import nan
import csv

input_file = "2021_title.csv"
dataset = pd.read_csv(input_file,error_bad_lines=False)

dataset.columns = ['venue','title']

dataset['title'] = dataset['title'].str.replace(';;;;', '')

journal_title_list = dataset["title"].tolist()

journal_venue_list = dataset["venue"].tolist()

sentences = journal_title_list

paper_id = 1
for test_title in sentences:

    journal_title_list.insert(0, test_title)
    
    new_journal_title_list = [x for x in journal_title_list if not(pd.isnull(x))==True]
    
    from sentence_transformers import SentenceTransformer
    
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    
    sentence_embeddings = model.encode(new_journal_title_list)
    
    sentence_embeddings.shape
    
    from sklearn.metrics.pairwise import cosine_similarity
    
    sonuclar = cosine_similarity(
        [sentence_embeddings[0]],
        sentence_embeddings[1:]
    ) 
    
    sonuclar_df = pd.DataFrame(sonuclar)
    
    sonuclar_df = sonuclar_df.transpose()
    
    journal_title_df = pd.DataFrame(new_journal_title_list)
    
    journal_title_df.columns = ['title']
    
    similar_journal_title = dataset["title"].tolist()
    
    similar_journal_title = [x for x in similar_journal_title if not(pd.isnull(x))==True]
    
    similar_journal_title_df = pd.DataFrame(similar_journal_title)
    
    similar_journal_title_df.columns = ['title']

    dat1 = pd.concat([sonuclar_df,similar_journal_title_df], axis=1)
    dat1.columns = ['similarity_score','title']
    results = dat1   
    venue_list=[]
    for i in results.index:
        venue_list.append(journal_venue_list[i])    
    venue_df = pd.DataFrame(venue_list)
    dat2 = pd.concat([sonuclar_df,similar_journal_title_df,venue_df], axis=1)
    dat2.columns = ['similarity_score','title','venue']    
    result_list = dat2.values.tolist()    
    result_csv = open("result2021_sim.csv", "a+", encoding='utf-8')
    journal_sim = []
    with open('volume.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            venue = row[0]
    
            for ix in result_list:
                if ix[2] == venue:
                    journal_sim.append(ix[0])
            average_sim = np.mean(journal_sim)
            print(str(paper_id)+","+venue+","+str(average_sim))
            result_csv.write(str(paper_id)+","+venue+","+str(average_sim)+","+"2021\n")
            journal_sim = []
            
    paper_id = paper_id + 1
    journal_title_list.pop(0)