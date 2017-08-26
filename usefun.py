# # This function reads text from a directory,filters from special characters and returns the same
def opentxt(dir):
    txt=open(dir).read()
    txt=(txt.replace('!','')).replace('<','')
    txt=(txt.replace('@','')).replace('>','')
    txt=(txt.replace('#','')).replace('.','')
    txt=(txt.replace('$','')).replace('"','')
    txt=(txt.replace('%',''))
    txt=txt.replace('^','')
    txt=txt.replace('&','')
    txt=txt.replace('*','')
    txt=txt.replace('(','')
    txt=txt.replace(')','')
    txt=txt.replace('-','')
    txt=(txt.replace('?','')).replace('/','')
    txt=txt.replace('+','')
    txt=txt.replace('=','')
    txt=txt.replace('`','')
    txt=txt.replace('~','')
    txt=txt.replace(':','')
    txt=txt.replace(';','')
    txt=(txt.replace('[','')).replace(']','')
    txt=(txt.replace('{','')).replace('}','')
    return txt.lower()
# #This function finds the euclidean vector
def vectorfinder(UW,L1):
    d1={}
    for word in UW:
        for char in word:
            d1[word]=L1.count(word)
    return d1
# # This funciton retruns the cosine angle value
def euclidean(d1,d2,UniqueWords):
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
# #This function returns the nearest prime for a given number
def nearestPrime(self,n):
    def ifPrime(num):
        c=0
        for i in range(1,num+1):
            if num%i==0:
                c+=1
        if c==2:
            return True
    for i in range(n,-1,-1):
        if ifPrime(i)==True:
            return i
            break
# #This function returns the dictionary of unique words from a list
def UniqueWords(l):
    d3={}
    UniqueWords=[]
    for c in l:
        if not c in d3:
            d3[c]=None
    for a in d3:
        UniqueWords.append(a)
    return UniqueWords
#This function removes spaces from a sentence
def txtfilter(s):
    L=s.split()
    sentence=""
    for x in L:
        sentence+=x
    return sentence
#This function returns the hash value of a given sentence/string
def hashfun(s):
    L=s.split()
    st=txtfilter(s)
    dic={}
    i=0
    for a in L:
        kgram=len(st)-len(a)
        for b in range(kgram+1):
            sp=st[b:b+kgram]
            for c in range(len(sp)):
                mini_hash=ord(sp[c])*(kgram**c)
                dic[sp]=mini_hash
    return dic
