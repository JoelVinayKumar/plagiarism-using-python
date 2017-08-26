#Class for bag of Words
class bagofWords:
    def __init__(self,L):
        self.L=L
    def output(self):
        print("\nDisplaying Bag of Words Matrix......\n")
        time.sleep(1)
        arr=[]
        fileName=[]
        for i in range(len(self.L)):
            title="File"+str(i+1)
            fileName.append(title)
        for x in range(len(self.L)):
            innerarr=[]
            for y in range(len(self.L)):
                #print("(",x,",",y,")-->",(self.sackofWords((opentxt(L[x])),(opentxt(L[y])))),end="    ")
                innerarr.append(self.sackofWords((opentxt(L[x])),(opentxt(L[y]))))
            rowTitle=["File"+str(x+1)]
            arr.append(rowTitle+innerarr)
        return tabulate(arr,headers=fileName,tablefmt="orgtbl")
    def sackofWords(self,txt1,txt2):
        if txt1==txt2:
            return 0
        else:
            ##Making lists
            L1=txt1.split()
            L2=txt2.split()
            ## Creating dictionaries for lists with frequency functions
            ##Bag of Words
            CombinedList=L1+L2
            UW=UniqueWords(CombinedList)
            vector1=vectorfinder(UW,L1)
            vector2=vectorfinder(UW,L2)
            return euclidean(vector1,vector2,UW)
    def __str__(self):
        return "This function displays the matrix for bag of words"
# Class for string match
class stringMatch:
    def __init__(self,L):
        self.L=L
    def output(self):
        print("\nDisplaying String Match Matrix......\n")
        time.sleep(1)
        arr=[]
        fileName=[]
        for i in range(len(self.L)):
            title="File"+str(i+1)
            fileName.append(title)
        for x in range(len(self.L)):
            innerarr=[]
            for y in range(len(self.L)):
                #print("(",x,",",y,")-->",(self.sackofWords((opentxt(L[x])),(opentxt(L[y])))),end="    ")
                innerarr.append(self.stringMat((opentxt(L[x])),(opentxt(L[y]))))
            rowTitle=["File"+str(x+1)]
            arr.append(rowTitle+innerarr)
        return tabulate(arr,headers=fileName,tablefmt="orgtbl")
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
# class fingerPrinting:
#     def __init__(self,L):
#         self.L=L
#     def output(self):
#             for x in range(len(self.L)):
#                 for y in range(len(self.L)):
#                     print("(",x,",",y,")-->",str(self.fingerPrinting_mini((opentxt(L[x])),(opentxt(L[y])))),end="    ")
#                 print("\n")
#     def fingerPrinting_mini(self,txt1,txt2):
#         count_sameword=0
#         vector1=hashfun(txt1)
#         vector2=hashfun(txt2)
#         # print(vector1,vector2)
#         for x in vector1:
#             for y in vector2:
#                 count_sameword+=1
#         return float(round((200*count_sameword)/(len(vector1)+len(vector2)),2))
# Take user's name
# name=input("What is your name?\n")
# print("Hello",name+"! Lets start checking plagiarized files.")
if __name__=='__main__':
    #importing all necessary libraries
    import glob
    import math
    import time
    from usefun import euclidean
    from usefun import opentxt
    from usefun import UniqueWords
    from usefun import vectorfinder
    from usefun import txtfilter
    from usefun import hashfun
    from tabulate import tabulate
    #Reading location of directory
    loc=r'C:\Users\lavot\OneDrive\MSIT\03-CSPP-1\Final Project\plagiarismtest'
    eachfile=loc+'\*.txt'
    #Appending all text files in directory to a list
    L=glob.glob(eachfile)
    b=bagofWords(L)
    s=stringMatch(L)
    op=True
    while op:
        x=int(input("\nPress\n1---> Bag of Words  2--->String Match: "))
        if x==1:
            print(b.output())
            print("\n")
        elif x==2:
            print(s.output())
            print("\n")
        else:
            print("Uh Oh! Wrong option.....Try again !")
        y=input("\nDo you want to continue? Press y (or) n: ")
        if y=='y':
            op=True
        elif y=='n':
            print("\nThanks for using our tool !\n")
            op=False
