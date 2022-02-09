def AMcount():
    f=open("story1.txt","r")
    d=f.read()
    cA=0
    cM=0
    print(d)
    for i in d:
        if i=="A" or i=="a":
            cA+=1
        elif i=="M" or i=="m":
            cM+=1
    print("Count of A or a=",cA," Count of M or m=",cM)
AMcount()
    