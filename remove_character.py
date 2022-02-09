# f=open("msg.txt","w")
# f.write("my name is grace\n i am in navgurukul banglore campus ")
# f.close()

f=open('test.txt','r')
file=open('write_msg.txt','w')
l=f.readlines()
for i in l:
    if 'a'in i:
        i=i.replace('a','')
        file.write(i)
file.close()
f.close()