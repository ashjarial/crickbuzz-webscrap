import requests
from bs4 import BeautifulSoup
url = "https://www.cricbuzz.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    matches = soup.find_all('ul', class_='cb-col cb-col-100 video-carousel-wrapper cb-match-crd-rt-itm')
else:
    print("Failed to retrieve data from the website.")


import pandas as pd
team_1=[]
team_2=[]
score_1=[]
score_2=[]

list=soup.find_all('li',class_='cb-view-all-ga cb-match-card cb-bg-white')

for i in range(0,len(list)):
    container=list[i].find_all('div')
    sub_container=container[3].find_all('div')
    k=0;
    if(len(sub_container)==8):
        k=1;
    if(k==0 and len(sub_container)>8):
        team_1.append(sub_container[2].text)
        score_1.append(sub_container[4].text)
        team_2.append(sub_container[7].text)
        score_2.append(sub_container[9].text)
    else:
        team_1.append(sub_container[1].text)
        score_2.append("Not Started")
        score_1.append("Not Started")
        team_2.append(sub_container[3].text)
        
data={
    'Team-1':team_1,
    'Team_1_score':score_1,
    'Team-2':team_2,
    'Team_2_score':score_2
}

df=pd.DataFrame(data)
print(df)