##Bag of words Function
#Making all words lower case
def bagofWords(txt1,txt2):
    txt1=txt1.lower()
    txt2=txt2.lower()
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
    cos=dot/(euc1*euc2)**0.5
    return "Files match by "+str(round(cos*100,2))+" %"
##String Matching functions
def stringMatch(txt1, txt2):
    answer = ""
    m, n = len(txt1), len(txt2)
    for i in range(m):
        match = ""
        for j in range(n):
            if (i + j < m and txt1[i + j] == txt2[j]):
                match += txt2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    LCS=len(answer[:-1])
    match=(LCS*2)/(len(txt1)+len(txt2))
    return "Files match by "+str(round(100*match,2))+" %"
## Take user's name
# name=input("What is your name?\n")
# print("Hello",name+"! Lets start checking plagiarized files.")
##Take input for first file
txt1=open("txt1.txt").read()
print("First file: ",txt1,"\n")
##Take input for second file
txt2=open("txt2.txt").read()
print("Second file: ",txt2,"\n")
print(bagofWords(txt1,txt2))
print(stringMatch(txt1,txt2))
