
def file(fname):
        with open(fname,"w") as f:
                f.write("my little heart \n")
                f.write("You are my sunshine")
        txt=open(fname)
        print(txt.read())
file("tiny heart")