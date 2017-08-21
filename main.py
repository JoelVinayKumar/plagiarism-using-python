## Take user's name
name=input("What is your name?\n")
print("Hello",name+"! Lets start checking plagiarized files.")
##Take input for first file
txt1=input("Enter first test:\n")
##Take input for second file
txt2=input("Enter second text:\n")
##Making all words lower case
txt1=txt1.lower()
txt2=txt2.lower()
##Making lists
L1=txt1.split(' ')
L2=txt2.split(' ')
print(txt1)
print(txt2)
