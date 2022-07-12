def file(fname, n):
   txt=open(fname)
   lines=txt.readlines()
   last_lines=lines[-n::]
   print(last_lines)
n=int(input("Enter the lines:-"))
file('test.txt',n)

