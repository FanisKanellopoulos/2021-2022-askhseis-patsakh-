import requests
import json
import urllib

url="https://api.opap.gr/draws/v3.0/1100/last-result-and-active"

response=urllib.request.urlopen(url)
html=response.read()
dedomena=html.decode()
kino=json.loads(dedomena)
winninglist=kino['last']['winningNumbers']['list']


res = requests.get('https://drand.cloudflare.com/public/latest')
data=res.text
temp=json.loads(data)
x=temp['randomness']
print ("randomness:",x,"\n") #prints the randomness

L=[]
for i in range(0,64,2):
    a=int(x[i:i+2],16)%80
    L.append(a)

L=list(dict.fromkeys(L)) #deletes the duplicates

print("newRandomness:",L,"\n") #prints the edited list of randomness

print("Winning Numbers:",winninglist,"\n")


counter=0
for i in range(len(L)):   #checking...
  if L[i] in winninglist:
    counter+=1
print ("Στην τελευταία κλήρωση του ΚΙΝΟ κληρώθηκαν ",counter," αριθμοί!")

#Έκανα print περισσότερα στοιχεία από αυτά που ζητήσατε για να σας διευκολύνω και για να φαίνεται πιο όμορφο :D
