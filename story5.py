# Q5. Write a function RevText() to read a text file “ Story.txt “ 
# and Print only word starting with ‘I’ in reverse order . 
# Example: If value in text file is: INDIA IS MY COUNTRY
#  Output will be: AIDNI SI MY COUNTRY.
def RevText():
    s=""
    f=open("story5.txt","r")
    a=f.read()
    b=a.split()
    for i in b:
        if i[0]=="I":
           s=s+" "+(i[::-1])
        else:
            s=s+" "+i
    print(s)
RevText()