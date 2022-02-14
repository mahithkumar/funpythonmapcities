from contextlib import nullcontext
import csv
import pandas as pd
from bs4 import BeautifulSoup as bs
import json
import requests

header = ['branchname','district','division','region','state','pincode']
citylist=[]
data= pd.read_csv("branches.csv")
#data= pd.read_csv("brdemo.csv")
#print(data.columns)
for i in data.BRANCH:
    webraw=requests.get("https://api.postalpincode.in/postoffice/"+i)
    #webdata = bs(webraw.content,'html.parser')
    webjson=json.loads(webraw.text)
    #webjson2=json.loads(webjson[0])

    if(type(webjson[0]['PostOffice'])!=type(None)):
        for x in webjson[0]['PostOffice']:
            flag=0
            if(x['Name'].lower()==i.lower()):
              # print(x['Name'])
              flag=1
              citylist.append([x['Name'],x['District'],x['Division'],x['Region'],x['State'],x['Pincode']])
              break
    if(flag==0):
                print(i)
                citylist.append([i,"none","none","none","none","none"])   
    if(type(webjson[0]['PostOffice'])==type(None)):

               print(i)
               citylist.append([i,"none","none","none","none","none"])          
               
citylist = pd.DataFrame(citylist, columns=header)
citylist.to_csv('brd2.csv',index=False)
#citylist.to_csv('brd.csv',index=False)               
