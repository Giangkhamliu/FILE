def countlines():
    f=open("exercise.txt","r")
    a=f.read()
    b=a.split()
    print(a)
    for i in b:
        if i=="delhi":
            f=open("delhi.txt","w")
            f.write("imtiyaz - delhi\n ayishah - delhi\n karthikeyan - delhi\n pankaj - delhi\n brijesh - delhi\n govind - delhi\n siddhi - delhi\n mohinder - delhi\n neela - delhi\n sarika - delhi\n harshad - delhi\n sekhar - delhi\n nand - delhi\n anoop - delhi")
            f.close()
        elif i=="shimla":
            f=open("shimla.txt","w")
            f.write("rati - shimla\n raghu - shimla\n puneet - shimla\n rajeev - shimla\n priyanka - shimla\n deepti - shimla")
        else:
            f=open("other.txt","w")
            f.write("balwinder - tokyo\n trishna - raipur\n pradeep - jaipur\n sashi - jaipur\n rajendra - jaipur\n suman - jaipur\n salma - jaipur\n naseer - kanpur\n nilima - cochin\n rishabh - meerut")
countlines()
