# Write a program that reads a text file and count the number of words 
# ending with "ing".
def search():
    f=open("test.txt","r")
    count_ing=0
    a=f.read().split()
    i=0
    while i<len(a):
        if "ing"in a[i]:
            count_ing+=1
            b= a[i]
            print(b) 
        i+=1
    print(count_ing)   
search()

