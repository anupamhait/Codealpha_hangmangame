import random
word = ["apple","banana","cheery","mango","orange","computer"]
key = random.choice(word)
attem = 6
display = ["_"]*len(key)
print("====HANGMAN GAME======\n")
while(attem>0):
    print("\n")
    print("Word is :"," ".join(display))

    print("Attems left :",attem)
    x = input("Guess a letter : ").lower()
    
    if x in key :
        print("Correct")
        for i in range(len(key)):
            if key[i]==x:
                display[i]=x           
    else:
        print("Wrong")
        attem = attem-1
    if "_" not in display:
        print("\nWord is :",key)
        print("Congratulation you won ")
        break
    if(attem==0):
        print("\nThe word was :",key)
        print("You loose\nTry next time")



  