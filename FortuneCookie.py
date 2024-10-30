import random

def quoteGetter(fortuneAmount, fortuneType):
    #maybe edit to pass file to lists o we don't open/clsoe on each
   fortunes = 0
   while fortunes < fortuneAmount: 
    fortunes+=1
    if fortuneType == "g":
            f = open("GoodFortune.txt", "r")
            fortune = random.randrange(0, 50, 1)
            cur = 0
            for line in f:
                # Print chosen line
                cur +=1
                if cur == fortune:
                    print(line.strip())
                else:
                    line.strip()
            f.close()
            print("What kind of fortune do you want? ")
            fortuneType = input("Type G for Good, Type B for Bad:")
    else:
            f = open("BadFortune.txt", "r")
            fortune = random.randrange(0, 50, 1)
            cur = 0
            for line in f:
                # Print chosen line
                cur +=1
                if cur == fortune:
                    print(line.strip())
                else:
                    line.strip()
            f.close()
            print("What kind of fortune do you want? ")
            fortuneType = input("Type G for Good, Type B for Bad:")
   return 

def customFortuneCookie(userQuote) :
    #prints image of fortune cookie with quote
    addQuote(userQuote)
    return 

def fortuneCookie() :
    #prints image of fortune cookie
    return 

def randomFortuneCookie(fortuneAmount) :
    #caps at 5
    return

def addQuote(userQuote): 
    #adds to quote file
    fortuneType = input("Is this fortune good, type g, or bad, type b:")
    if fortuneType == "g":
        f = open("GoodFortune.txt", "a")
        f.write(userQuote)
        f.close()
    else:
        f = open("BadFortune.txt", "a")
        f.write(userQuote)
        f.close()
    return


print("Welcome to Scooby's Fortunes!")
#maybe implement better loop/swicth for multiple options
fortuneCustom = input("Would you like to create your own fortune cookie or purchase some, enter c for create or p for purchase:")
if fortuneCustom == "c":
    userQuote = input("Enter your desired fortune:")
    customFortuneCookie(userQuote)
    #might be too similar to other fortune cookie functions could change to have params be c or p and then do either customCookie or the code below for purchase

else:
    #TODO: code for custom re-indent for purchased
    fortuneAmount = input("You can have up to 50 so how many fortune cookies do you want:")

    if fortuneAmount != 0:
        if fortuneAmount < 0 or fortuneAmount > 50:
            i = 0
            while i == 0:
                print("Inavlid Fortune amount, try again.")
                fortuneAmount = input("You can have up to 50 so how many fortune cookies do you want:")
                if fortuneAmount > -1 and fortuneAmount < 50:
                    i = 1
    else:
        if fortuneAmount == 0:
            print("Sad to see you go.")
        else:
            if fortuneAmount < 6:
                fortuneRandom = input("Would you like a random fortune, yes or no:")
                if fortuneRandom == "yes":
                    randomFortuneCookie(fortuneAmount)
                else:
                    #TODO use quoteGetter
                    print("What kind of fortune do you want? ")
                    fortuneType = input("Type G for Good, Type B for Bad:")
                    quoteGetter(fortuneAmount, fortuneType)
                    fortuneCookie()
                    
            else: 
                #TODO: run functions
                print("What kind of fortune do you want? ")
                fortuneType = input("Type G for Good, Type B for Bad:")
                quoteGetter(fortuneAmount, fortuneType)
                fortuneCookie()
print("Goodbye!")


