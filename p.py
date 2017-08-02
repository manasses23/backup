prod='produto1;10;produto2;20;produto3;30'
produto= prod.split(';')
for p in produto:
 if p % 2==0:
   print (produto[p] + "=" + produto[p+1])
