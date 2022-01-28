import requests
import json
import urllib

res = requests.get('https://drand.cloudflare.com/public/latest')
data=res.text
temp=json.loads(data)
y=temp['round'] #saves last round

#μετρητές για τα round με τις μεγαλήτερες ακολουθίες
maxmemory_1=0
maxmemory_0=0
maxround_1="" 
maxround_0=""

print("this may take a few seconds...")
for i in range(100):
  url="https://drand.cloudflare.com/public/"
  y=str(y)
  url=url+y #μετατροπή του url 
  
  res = requests.get(url)
  data=res.text
  temp=json.loads(data)
  x=temp['randomness']
  x=bin(int(x,16))
  r=temp['round'] #saves every round temporary
  
  #μετρητές για τις ακολουθίες
  counter_1=0
  memory_0=0
  counter_0=0
  memory_1=0
  for i in range(2,len(x)):
    if x[i]=="1":
      counter_1+=1
    else:
      if counter_1>memory_1:
        memory_1=counter_1
      counter_1=0

    if x[i]=="0":  #είναι λίγο κουτός τρόπος γιατί πραγματοποιεί έλεγχο 2 φορές για το ίδιο πράγμα αλλά εκείνη την στιγμή δεν μπορούσα να σκεφτώ κάτι καλύτερο... 
      counter_0+=1
    else:
      if counter_0>memory_0:
        memory_0=counter_0
      counter_0=0   
  
  #αποθηκεύει την μεγαλήτερη ακολουθία καθώς και το round από το οποίο βρέθηκε
  if memory_1>maxmemory_1:
    maxmemory_1=memory_1
    maxround_1=r
  
  if memory_0>maxmemory_0:
    maxmemory_0=memory_0
    maxround_0=r

  #προετοιμασία για την μετατροπή του επόμενου url
  y=int(y)
  y=y-1   

print("Το μήκος της μεγαλύτερης ακολουθίας με συνεχόμενα μηδενικά είναι:",maxmemory_0,"και εμφανίστηκε στο round:",maxround_0)    
print("Το μήκος της μεγαλύτερης ακολουθίας με συνεχόμενους άσσους είναι:",maxmemory_1,"και εμφανίστηκε στο round:",maxround_1)
