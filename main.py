#Making all words lower case
def opentxt(dir):
    txt=open(dir).read()
    return txt
class bagofWords:
    def __init__(self,L):
        self.L=L
    def output(self):
        for x in range(len(self.L)):
            for y in range(len(self.L)):
                print("(",x,",",y,")-->",self.sackofWords(opentxt(L[x]),opentxt(L[y])),end="    ")
            print("\n")
    def sackofWords(self,txt1,txt2):
        if txt1==txt2:
            return 0
        if txt1!=txt2:
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
            cos=(dot/(euc1*euc2)**0.5)
            return float(round(cos*100,2))
    def __str__(self):
        return "This function displays the matrix for bag of words"
class stringMatch:
    def __init__(self,L):
        self.L=L
    def output(self):
        for x in range(len(self.L)):
            for y in range(len(self.L)):
                print("(",x,",",y,")-->",str(self.stringMat(self.txtfilter(opentxt(L[x])),self.txtfilter(opentxt(L[y])))),end="    ")
            print("\n")
    def txtfilter(self,s):
        L=s.split()
        sentence=""
        for x in L:
            sentence+=x
        return sentence
    def stringMat(self,txt1, txt2):
        if txt1==txt2:
            return 0
        else:
            answer = ""
            m, n = len(txt1), len(txt2)
            for i in range(m):
                match = ""
                for j in range(n):
                    if (i + j < m and txt1[i + j] == txt2[j]):
                        match += txt2[j]
                    else:
                        if (len(match) > len(answer)):
                            answer = match
                        match = ""
            LCS=len(answer[:-1])
            output=(LCS*2)/(len(txt1)+len(txt2))
            return round(100*output,2)
# def fingerPrinting(txt1,txt2):
#     def hash(string):
#         d={}
#         k=[]
#         v=[]
#         string.lower()
#         k=len(string)
#         for i in range(1,27):
#             d[chr(i+96)]=i
#         for x in string:
#             if ord(x)>=97 and ord(x)<=122:
#                 i=0
#                 sum=0
#                 sum+=d[x]*(k**i)
#                 i+=1
#         return sum
#     L1=txt1.split()
#     L2=txt2.split()
#     L3=[]
#     i=0
#     for a in L1:
#         while i<=len(txt2)-4:
#             L3.append(hash(txt2[i:i+4]))
#             i+=1
#     print(L3)
## Take user's name
# name=input("What is your name?\n")
# print("Hello",name+"! Lets start checking plagiarized files.")
if __name__=='__main__':
    import glob
    import math
    loc=r'C:\Users\lavot\OneDrive\MSIT\03-CSPP-1\Final Project\plagiarismtest'
    eachfile=loc+'\*.txt'
    L=glob.glob(eachfile)
    bag=bagofWords(L)
    bag.output()
    print("\n\n")
    strl=stringMatch(L)
    strl.output()
