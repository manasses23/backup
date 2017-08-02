import json
while True:	
 prod= input('Digite o nome do produto seguido de ; e seu preço\n')
 produto= prod.split(';')
 pro= open('datafile.json','w')
 json.dump(produto,pro,indent=4)
 pro.close
 pro=open('datafile.json')
 p=json.load(pro)
 for i in range(0,len(p)-1):
  if i%2==0:
    print(p[i] + '=' + p[i+1])
