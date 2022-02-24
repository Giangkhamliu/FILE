# def file_read(fname):
#         with open(fname) as f:    
#                 content_list = f.readlines()
#                 print(content_list)
# file_read('test.txt')

# def file_read(fname):
#         with open (fname, "r") as myfile:
#                 data=myfile.readlines()
#                 print(data)
# file_read('test.txt')

def file_read(fname):
        content_array = []
        f=open(fname)  
        for line in f:
             content_array.append(line)
        print(content_array)
file_read('test.txt')