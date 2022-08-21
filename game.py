
import random
words=["chocolate","pizza","milk","cashew","carrot","banana","onion","chapathi","rasgulla","clove","italy","china","india","belgium","nepal","france","argentina","brazil","canada","finland","tulip","orchid","lily","sunflower","lotus","daisy","hibiscus","marigold","jasmine","rose"] 
word=random.choice(words)
if words.index(word)<10:
    print("Hint:food")
elif words.index(word)<20:
    print("Hint:countries")
else:
    print("Hint:flowers")
for i in range(len(word)):
    print("_",end=" ")
print("\nthe total no of chances are 8")
chances=8
p=[]
while chances>0:
    s=[]
    for i in range(len(word)):
        s.append('!')
    guess=input("Guess letter: ")
    if guess in word:
        p.append(guess)
        for i  in range(len(word)):
            for j in range(len(p)):
                if p[j]==word[i]:
                    s[i]=word[i]
        flag=0
        for i in range(len(word)):
            if(s[i]=='!'):
                s[i]='_'
                flag=1
        print(s)
        if(flag==0):
            print("win")
            break
    else:
        chances-=1
        if chances>0:
            print("chances: ",chances)
        else:
            print("you lose")
        
Hangman Game.txt
Displaying Hangman Game.txt.