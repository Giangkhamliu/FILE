def longest_word():
    f=open("write.txt","r")
    words =f.read().split()
    i=0
    max=0
    max1=""
    while i<len(words):
        if len(words[i])>max:
            max=len(words[i])
            max1=words[i] 
        i+=1
    print(max1)
longest_word()
