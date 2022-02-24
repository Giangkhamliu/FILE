# 4. Write a Python function that takes a list of strings as an argument and
# displays the strings which starts with “S” or “s”. Also write a program to 
# invoke this function.
def display():
    f=open("test.txt","r")
    a=f.read().split()
    for  i in a:
        if i[0]=="S" or i[0]=="s":
            print(i)
display()