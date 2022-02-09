# Q4. Write a method/function DISPLAYWORDS() in python to read lines
#  from a text file STORY.TXT, and display those words, which are 
# less than 4 characters.
def displaywords():
    f=open("story3.txt","r")
    a=f.read()
    b=a.split()
    for i in b:
        if len(i)>4:
            print(i)
displaywords()