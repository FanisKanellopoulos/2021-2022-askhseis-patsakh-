def bubblesort(countList,charList):
    N=len(countList)-1
    for i in range(N):
      for j in range(N,i,-1):
        if countList[j]>countList[j-1]:
          countList[j],countList[j-1]=countList[j-1],countList[j]
          charList[j],charList[j-1]=charList[j-1],charList[j]

    return charList


def first_letters(words,used_words,x):
    count_chars=[] #αριθμός εμφανήσεων
    used_chars=[] #λίστα με τα 2 ή 3 πρώτα γράμματα

    for i in range(len(used_words)):
      if used_words[i][:x] not in used_chars and len(used_words[i])>(x-1):
        used_chars.append(used_words[i][:x])

    for i in range(len(used_chars)):
      counter=0
      for j in range(len(words)):
          if used_chars[i]==words[j][:x]:
            counter+=1
      count_chars.append(counter)

    List=bubblesort(count_chars,used_chars) #κλήση της bubblesort()

    if x==2:
        print("Οι τρεις πρώτοι συνδυασμοί ,των δύο πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις είναι:\n")
        for i in range(3):
            print(List[i])
    else:
        print("Οι τρεις πρώτοι συνδυασμοί ,των τριών πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις είναι:\n")
        for i in range(3):
            print(List[i])
    print("\n")



allowed_chars="abcdefghijklmnopqrstuvwxyz "

with open("(FILE NAME).txt") as f: #για την συγκεκριμένη άσκηση χρησιμοποίησα το tales of two cities,αλλά επειδή η άσκηση δεν αναφέρεται σε κάποιο συγκεκριμένο αρχείο μπορείτε να βάλετε όποιο θέλετε.
    data=f.read()

f.close()

filtered_text=""
data=data.lower()

#print(data)
for c in data:
    if ord(c) in range(97,123) or ord(c)==10 or c==" ": #δεν έβλεπε το enter σαν κενό και μου ένωνε τις λέξεις... επομένως χρησημοποίησα το ord(c)==10
        filtered_text=filtered_text+c

words=filtered_text.split(" ")

temp = []
for c in words:
    temp.append(c.replace("\n", " "))  #αντικατέστησα το /n με κενο αλλά και πάλι ειχα πρόβλημα...


for i in range(1,len(temp)):     
    temp[i]=" "+temp[i]         #μετά απο αρκετή ώρα παρατήρησης και δοκιμών βρήκα την λύση ;)

text=""
for c in temp:  
    text+=c

words=text.split(" ")  

counter=0
for i in range(len(words)):
    if words[i-counter]=="":        #αφαιρώ τα κενά στοιχεία που έχουν μείνει στην λίστα!
        words.pop(i-counter)          
        counter+=1

#print(words)       #έτοιμη η λίστα!!!



#Για τις 10 δημοφιλέστερες λέξεις...

times_showed=[]#λίστα για τους μετρητές
used_words=[] #λίστα για τις ήδη υπολογισμένες λέξεις

for i in range(len(words)):
  if words[i] not in used_words:
    c=words.count(words[i])
    used_words.append(words[i])
    times_showed.append(c)


charArray=bubblesort(times_showed,used_words) #κλήση της bubblesort()

print("Οι 10 δημοφιλέστερες λέξεις είναι:\n")
for i in range(10):
  print(charArray[i]) #εμφάνιση του αποτελέσματος
print("\n")


#2 πρώτα γράμματα
first_letters(words,used_words,2)

#3 πρώτα γράμματα
first_letters(words,used_words,3)
