def countlines():
    f=open("exercise.txt","r")
    p=(f.readlines())
    print(p)
    count=0
    for i in p:
        count+=1
    print("The numbers of lines are:-",count)
countlines()
