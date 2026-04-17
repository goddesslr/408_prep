import os 
import jieba
import pandas as pd

dict_path="/mnt/e/AI&python/homework/射雕英雄传人物.txt"
charater={}

with open(dict_path,'r',encoding='utf-8') as f:
    for i in f:
       name=i.strip()
       if name:
           charater[name]=[] 

folder_path="/mnt/e/AI&python/homework/射雕英雄传"
file_names=os.listdir(folder_path)

chapter_files=[]

for file_name in file_names:
    if file_name.endswith('.txt') and '章' in file_name:
        chapter_files.append(file_name)

chapter_files.sort()

for chapter in chapter_files:
    file_path=os.path.join(folder_path,chapter)
    
    with open(file_path,'r',encoding='utf-8') as f:
        content=f.read()
    
    words=jieba.lcut(content)
    
    for name in charater:
        count=words.count(name)
        charater[name].append(count)

chapter_name=[i.replace('.txt','') for i in chapter_files]
df=pd.DataFrame.from_dict(charater,orient='index',columns=chapter_name)

output_path="/mnt/e/AI&python/homework/人物统计.csv"

df.to_csv(output_path,encoding='utf-8')


    

