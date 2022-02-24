#  Write a program to write Name and Roll no into a binary file,"file.dat"
import pickle
with open("file.dat","wb")as f:
    while True:
        op=int(input("Enter 1 to add data,0 to quit:"))
        if (op==1):
            name=input("Enter name:")
            rollno=int(input("roll number:"))
            pickle.dump((name,rollno),f)
        elif op==0:
            break