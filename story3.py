# Q3. Write a function in python to count the number of lines in 
# a text file ‘ STORY.TXT’ which is starting with an alphabet ‘A’ .
def counta():
    f=open("story3.txt","r")
    c=0
    b=f.readlines()
    for i in b:
        if i[0]=="a" or i[0]=="A":
            c=c+1
    print("Lines starting from A are:-",c)
counta()