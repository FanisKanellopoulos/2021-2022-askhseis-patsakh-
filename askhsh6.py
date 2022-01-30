#ενεργοποιηστε τα 2 αριθμημένα σχόλια και μειώστε τις επαναλήψεις για γραφικη αναπαράσταση

import random

def position(array):    #setting the position
  i=random.randrange(8)
  j=random.randrange(8)
  
  array.append(i)
  array.append(j)

  return array 


def checktower(pos,board):
  
  found=False
  i=0
  
  while i<8 and not found:
    if board[pos[0]][i]==" queen ": #y axis
      found=True
    elif board[i][pos[1]]==" queen ": #x axis
      found=True
    #2πλος έλεγχος για να φαίνεται καλύτερα στο μάτι    
    i+=1
  return found


def checkofficer(pos,board):
 
  #είναι λίγο πολύπλοκη συνάρτηση και δεν μπορώ να την εξηγήσω με σχόλια...
  
  found=False
  i=0

  while i<8 and not found:
    if (pos[0]-i)>-1 and (pos[1]+i)<8:
      if board[pos[0]-i][pos[1]+i]==" queen ":
        found=True
    if (pos[0]+i)<8 and (pos[1]+i)<8:
      if board[pos[0]+i][pos[1]+i]==" queen ":
        found=True
    if (pos[0]-i)>-1 and (pos[1]-i)>-1:
      if board[pos[0]-i][pos[1]-i]==" queen ":
        found=True
    if (pos[0]+i)<8 and (pos[1]-i)>-1:  
      if board[pos[0]+i][pos[1]-i]==" queen ":
        found=True

    i+=1
  return found

def checkqueen(pos,board):
 
  #συνδυάζει την checktower() και την checkofficer()
  
  found=False
  i=0
  counter=0
  while i<8 and not found:
    #for tower
    if board[pos[0]][i]==" tower ": #y axis
        found=True
        counter+=1
    elif board[i][pos[1]]==" tower ": #x axis
        found=True
        counter+=1  
    if (pos[0]-i)>-1 and (pos[1]+i)<8:
      if board[pos[0]-i][pos[1]+i]==" tower ":
        found=True
        counter+=1 
    if (pos[0]+i)<8 and (pos[1]+i)<8:
      if board[pos[0]+i][pos[1]+i]==" tower ":
        found=True
        counter+=1 
    if (pos[0]-i)>-1 and (pos[1]-i)>-1:
      if board[pos[0]-i][pos[1]-i]==" tower ":
        found=True
        counter+=1 
    if (pos[0]+i)<8 and (pos[1]-i)>-1:  
      if board[pos[0]+i][pos[1]-i]==" tower ":
        found=True
        counter+=1 
    i+=1
  
  found=False
  i=0
  while i<8 and not found:  
    #for officer
    if board[pos[0]][i]=="officer": #y axis
        found=True
        counter+=1
    elif board[i][pos[1]]=="officer": #x axis
        found=True
        counter+=1  
    if (pos[0]-i)>-1 and (pos[1]+i)<8:
      if board[pos[0]-i][pos[1]+i]=="officer":
        found=True
        counter+=1 
    if (pos[0]+i)<8 and (pos[1]+i)<8:
      if board[pos[0]+i][pos[1]+i]=="officer":
        found=True
        counter+=1 
    if (pos[0]-i)>-1 and (pos[1]-i)>-1:
      if board[pos[0]-i][pos[1]-i]=="officer":
        found=True
        counter+=1 
    if (pos[0]+i)<8 and (pos[1]-i)>-1:  
      if board[pos[0]+i][pos[1]-i]=="officer":
        found=True
        counter+=1 
    i+=1

  return counter


white_points=0
black_points=0

for i in range(100):

    black_queen=[]
    white_tower=[]
    white_officer=[]


    #ορισμός των θέσεων
    black_queen=position(black_queen)


    white_tower=position(white_tower) 
    while white_tower==black_queen:
      white_tower=[]
      white_tower=position(white_tower) 

    #just in case they have the same position

    white_officer=position(white_officer)
    while white_officer==white_tower or white_officer==black_queen:
      white_officer=[]
      white_officer=position(white_officer)


    """                              
    print("positions:")                
    print("queen:",black_queen,"\nofficer:",white_officer,"\ntower:",white_tower,"\n")                    #---1---
    
    """
    board = [['-------' for x in range(8)] for y in range(8)]

    board[white_tower[0]][white_tower[1]]=" tower "
    board[black_queen[0]][black_queen[1]]=" queen "
    board[white_officer[0]][white_officer[1]]="officer"

    """              
    print("--CHESS--\n")
    for i in range(8):                                                                                    #---2---
      print(board[i],"\n")
    """
    
    points=0

    #Η άσπρη ομάδα παίζει 1η
    if checkofficer(white_officer,board):
      points+=1
      white_points+=1

    if checktower(white_tower,board):
      points+=1
      white_points+=1


    if points==0:  #αν δεν την έχουν σκοτώσει τα άσπρα πιόνια
      c=checkqueen(black_queen,board)
      if c>0:
        points=c
        black_points+=points

print ("βαθμοί άσπρης ομάδας:",white_points)
print ("βαθμοί μαύρης ομάδας:",black_points,)
