banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
names=open("file-question3.txt","w")
# i=0
# while i<len(banks_list):
#     names.write(""+banks_list[i]+"\n")
#     i+=1

for name in banks_list:
    names.write(""+name+"\n")