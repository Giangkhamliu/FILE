# Q1. Write a function in Python that counts the number of “Me” or “My”(in smaller
#  case also) words present in a text file “STORY.TXT”. If the “STORY.TXT” 
# contents are as follows:

def countmemy():
    f=open("story.txt","r")
    d=f.read()
    m=d.split()
    c=0
    print(d)
    for i in m:
        if i=="me" or i=="my" or i=="My" or i=="Me":
            c+=1
    print("Count of me/my",c)
countmemy()
    
