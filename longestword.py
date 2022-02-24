def longest(fname):
    with open(fname,"r") as f:
        txt= f.read().split()
        max=0
        max1=""
        i=0
        while i<len(txt):
            if len(txt[i])>max:
               max=len(txt[i])
               max1=txt[i]
            i+=1
        print(max1)
longest("write.txt")
