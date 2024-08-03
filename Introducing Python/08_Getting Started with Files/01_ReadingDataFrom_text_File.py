fd = open("Introducing Python/08_Getting Started with Files/data.txt","r")
txt = fd.read()
print(txt)
fd.close()