class bagofWords:
    def __init__(self,L):
        self.L=L
    def output(self):
        arr=[]
        for x in range(len(self.L)):
            innerarr=[]
            for y in range(len(self.L)):
                # print("(",x,",",y,")-->",,end="    ")
                F=self.sackofWords(opentxt(L[x]),opentxt(L[y]))
                innerarr.append(F)
            arr.append(innerarr)
        print(tabulate[arr,innerarr])
    def sackofWords(self,txt1,txt2):
        if txt1==txt2:
            return 0
        else:
            ##Making lists
            txt1=txt1.lower()
            txt2=txt2.lower()
            L1=txt1.split()
            L2=txt2.split()
            ## Creating dictionaries for lists with frequency functions
            ##Bag of Words
            d1={}
            d2={}
            UW=UniqueWords((L1+L2))
            vector1=vectorfinder(UW,d1,L1)
            vector2=vectorfinder(UW,d1,L1)
            return euclidean(vector1,vector2,UW)
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
            LCS=len(answer)
            output=(LCS*2)/(len(txt1)+len(txt2))
            return round(100*output,2)
class fingerPrinting:
    def __init__(self,L):
        self.L=L
    def output(self):
            for x in range(len(self.L)):
                for y in range(len(self.L)):
                    print("(",x,",",y,")-->",str(self.fingerPrinting_mini((opentxt(L[x])),(opentxt(L[y])))),end="    ")
                print("\n")
    def fingerPrinting_mini(self,txt1,txt2):
        count_sameword=0
        vector1=hashfun(txt1)
        vector2=hashfun(txt2)
        # print(vector1,vector2)
        for x in vector1:
            for y in vector2:
                count_sameword+=1
        return float(round((200*count_sameword)/(len(vector1)+len(vector2)),2))
# Take user's name
# name=input("What is your name?\n")
# print("Hello",name+"! Lets start checking plagiarized files.")
if __name__=='__main__':
    import glob
    import math
    from usefun import euclidean
    from usefun import opentxt
    from usefun import UniqueWords
    from usefun import vectorfinder
    from usefun import txtfilter
    from usefun import hashfun
    import tabulate
    loc=r'C:\Users\lavot\OneDrive\MSIT\03-CSPP-1\Final Project\plagiarismtest'
    eachfile=loc+'\*.txt'
    L=glob.glob(eachfile)
    f=bagofWords(L)
    f.output()
