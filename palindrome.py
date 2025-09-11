wrd=input("enter the word")
word=wrd.lower()
k,l=0,(int)(len(word)/2)
for i in range(l):
    n1=i
    n2=(int)(len(word))-i-1
    if word[n1]!=word[n2]:
        print("not palindrome")
        break
    else:
        k+=1
if(k==l):
    print("palindrome")

