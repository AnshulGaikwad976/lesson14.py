firstfile = input("Enter thenam of the first file")
secondfile= input("Enter the name of the scond file:")

f2 = open(secondfile, 'r')
data = f2.read()
f2.close

f1= open(firstfile, 'a')
f1.write(data)
f1.close()

print("contentof", secondfile, "has been added to", firstfile)