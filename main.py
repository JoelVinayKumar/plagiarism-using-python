## Take user's name
# name=input("What is your name?\n")
# print("Hello",name+"! Lets start checking plagiarized files.")
##Take input for first filewith open("txt1.txt","r") as myfile:
txt1=open("txt1.txt").read()
print("First file: ",txt1,"\n")
##Take input for second file
txt2=open("txt2.txt").read()
print("Second file: ",txt2,"\n")
##Making all words lower case
# txt1=txt1.lower()
# txt2=txt2.lower()
##Making lists
L1=txt1.split()
L2=txt2.split()
## Creating dictionaries for lists with frequency functions
##Bag of Words
d1={}
d2={}
d3={}
L3=L1+L2
for c in L3:
    if not c in d3:
        d3[c]=None
UniqueWords=[]
for a in d3:
    UniqueWords.append(a)
for word in UniqueWords:
    for char in word:
        if (ord(char)>=65 and ord(char)<=90) or (ord(char)>=97 and ord(char)<=122) or ord(char)==95:
            d1[word]=L1.count(word)
for word in UniqueWords:
    for char in word:
        if (ord(char)>=65 and ord(char)<=90) or (ord(char)>=97 and ord(char)<=122) or ord(char)==95:
            d2[word]=L2.count(word)
euc1=0
euc2=0
dot=0
for num in d1.values():
    euc1+=num**2
for num in d2.values():
    euc2+=num**2
for a in UniqueWords:
    dot+= d1[a]*d2[a]
cos=dot/(euc1*euc2)
print("Percentage of bag words:",cos*100,"%")
