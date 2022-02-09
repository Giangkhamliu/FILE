with open("write.txt", "r") as f:
  for line in f:
    stripped_line = line.strip()
    print(stripped_line)