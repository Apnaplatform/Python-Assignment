# Count vowels in a string

text = input("Enter your string : ")
vowels = "aeiouAEIOU"
count = 0

for i in text:
    if(i in vowels):
        count += 1
print ("Number of vowels :",count)