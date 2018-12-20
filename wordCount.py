myFile = open(input('Enter your file name: '), "r")
lines = myFile.readlines()
myFile.close()
print("There are {} lines of text in this file.".format(len(lines)))
for x in lines:
    print(x)
# print(lines[0])
