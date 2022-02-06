import requests
import json
import urllib

res = requests.get('https://drand.cloudflare.com/public/latest')
data=res.text
temp=json.loads(data)
y=temp['round'] #saves last round

sum=""

print("Please wait, this may take a few seconds...")
for i in range(100):
  url="https://drand.cloudflare.com/public/"
  y=str(y)
  url=url+y #μετατροπή του url
  #print (url) 
  
  res = requests.get(url)
  data=res.text
  temp=json.loads(data)
  x=temp['randomness']
  x=bin(int(x,16))
  x=str(x)
  
  #print(x,"\n")
  sum+=x[2:]      #ενώνει τα randomness
  
  #προετοιμασία για την μετατροπή του επόμενου url
  y=int(y)
  y=y-1   

#print (sum)


#μετρητές για τις ακολουθίες
counter_1=0
memory_0=0
counter_0=0
memory_1=0

for i in range(len(sum)):
    if sum[i]=="1":
      counter_1+=1
    else:
      if counter_1>memory_1:
        memory_1=counter_1
      counter_1=0

    if sum[i]=="0":  #είναι λίγο κουτός τρόπος γιατί πραγματοποιεί έλεγχο 2 φορές για το ίδιο πράγμα αλλά εκείνη την στιγμή δεν μπορούσα να σκεφτώ κάτι καλύτερο... 
      counter_0+=1
    else:
      if counter_0>memory_0:
        memory_0=counter_0
      counter_0=0 

print("Το μήκος της μεγαλύτερης ακολουθίας με συνεχόμενα μηδενικά είναι:",memory_0)
print("Το μήκος της μεγαλύτερης ακολουθίας με συνεχόμενους άσσους είναι:",memory_1)
