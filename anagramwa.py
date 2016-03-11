import random
import platform
print("Welcome to the world of Anagram!!")
print("Loading........ might take a few seconds")
os=platform.dist()[0]
if os=='LinuxMint' or os=='Ubuntu':
    loc='/usr/share/dict/cracklib-small'
else:
    loc='/usr/share/dict/words'
with open(loc) as f:
    content=f.read().split('\n')
f.close()
l=len(content)
words=[]
for i in range(0,l):
    if '\'' in content[i] or len(content[i])<5:
        continue
    words.append(content[i])
words=words[1:]
d=len(words)
words=words[:d]
try:
    print("Rules:")
    print("1.You get 5 tries to guess the word right.If length of word is more than 7 you get 7 attempts.")
    print("2.Time alloted equals INFINITY")
    print("3.CTRL+D or CTRL+C to exit.")
    print("Lets begin..............")
    while 1:
        word=words[random.randint(0,d)]
        shuffle=list(word)
        random.shuffle(shuffle)
        print "Your word to guess:"
        print shuffle
        tries=0
        if len(word)>7:
            chances=7
        else:
            chances=5
        while tries<chances:
            tries=tries+1
            userin=raw_input()
            if userin==word:
                print("Yayyyyyy you got it right.Congo :)")
                break
            elif tries!=chances:
                print("Please try again!!")
                print("Hint:")
                t1=random.randint(0,len(word))
                t2=random.randint(0,len(word))
                hint=""
                for i in range(0,len(word)):
                    if i==t1 or i==t2:
                        hint=hint+word[i]
                    else:
                        hint=hint+"."
                print hint
        if tries==chances:
            print "The answer was "+word
            print("Sorry you could not get it right :( Try another word")
except:
    print("Thank You for playing....See you soon :) ")
