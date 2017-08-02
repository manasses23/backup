import json	
prod='produto1;10;produto2;20;produto3;30'
produto= prod.split(';')
pro= open('datafile.json','w')
json.dump(produto,pro,indent=4)
pro.close
pro=open('datafile.json')
p=json.load(pro)
for i in produto:
  if i%2==0:
    print(p[i] + '=' + p[i+1])
