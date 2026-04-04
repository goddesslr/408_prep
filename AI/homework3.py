import os
import jieba

folder_path= "../../Desktop/AI&python/homework/射雕英雄传"
dict_path= "../../Desktop/AI&python/homework/小作业3-4-射雕英雄传词典.txt"
full_text=" "
file_names=os.listdir(folder_path)
for file_name in file_names:
    if file_name.endswith(".txt"):
        file_path=os.path.join(folder_path,file_name)
        text = open(file_path,'r',encoding="utf-8").read()
        full_text = full_text + text

jieba.load_userdict(dict_path)

words=jieba.lcut(full_text)

word_counts={}

for word in words :
    if len(word)==1:
        continue
    else:
        word_counts[word]=word_counts.get(word,0) + 1

items=list(word_counts.items())
items.sort(key=lambda x :x[1],reverse=True)

for i in range(30):
    word,count=items[i]
    print("{0:<15}{1:>10}".format(word,count))

