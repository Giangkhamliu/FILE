import pickle
f=open("student.dat","wb")
pickle.dump([23,"John",12],f)
pickle.dump([24,"Tina",13],f)
f.close()