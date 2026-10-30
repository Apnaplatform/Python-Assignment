# count space

text = "Python is a easy programming language"
count = 0

for i in text:
    if i == " ":
        count+= 1
print ("Number of space :",count)