# def file_lengthy(fname):
#     with open(fname) as f:
#         for i, l in enumerate(f):
#            pass
#     return i+1
# print("Number of lines in the file: ",file_lengthy("test.txt"))
def file_lengthy(f):
        f=open("test.txt","r")
        a=f.readlines()
        count=0
        i=0
        while i<len(a):
            count+=1
            i+=1
        print("Number of lines in the file: ",count)
file_lengthy("test.txt")