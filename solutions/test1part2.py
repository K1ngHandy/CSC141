##num=int(input("what is the number?"))
##if( num %2 ==0) and (num %5 ==0):
##    print("It is both")
##else:
##    print("not")


##num=int(input("what is the number?"))
##if( num %2 ==0) or (num %5 ==0):
##    print("It is div. by at least one")
##else:
##    print("none")


##year=int(input("what is the year?"))
##
##if (year%400==0) or (year %4==0 and year %100 !=0):
##    print("Leap year")
##else:
##    print("Common year")


##num=int(input("what is the number?1-2"))
##
##if(num ==1):
##    print("I")
##else:
##    print("II")

##
##word=input("what is the word?")
##print(word[0])
##print(word[-1])
##
##if(word[0]==word[-1]):
##    print("the 1st and last symbols are the same")
##else:
##    print("the 1st and last symbols are NOT the same")


# to get a name, if it begins by an "A", replace it by "*" redisplay the name
##
##name=input("what is the name (length is 4)?")
##if(name[0]=="A"):
##    print("*",name[1],name[2],name[3],sep="")
##else:
##    print(name)


#Get a name if its length is even display the 1st symbol o.w. display the last symbol.

##name=input("what is the name?")
##d=len(name)
##if(d %2 ==0):
##    print(name[0])
##else:
##    print(name[d-1])
# get a name(length is 4) if the 1st and last symbols are the same reverse it,
# o.w. replace the 1st and last symbols by "*" redisplay the name
# ABCA---> ACBA
# ABCD---> *BC*

#the last symbol is at length-1

##word=input("what is the name?")
##
##if(word[0]==word[3]):
##    print(word[3],word[2],word[1],word[0],sep="")
##else:
##    print("*",word[1],word[2],"*",sep="")



#Get a name if it begins by "A" replace it by "a"
##word=input("what is the name?")
##if(word[0]=="A"):
##    print("a",word[1],word[2])
##else:
##    print(word)


###if the name begins by a/A, display ****
##word=input("what is the name?")
##if(word[0]=="A" or word[0]=="a"):
##    print("********")
##else:
##    print(word)



name=input("what is the word?(length=4)")
if(name[0]==name[3]   and name[1]==name[2]):
    print("a palindrome")
else:
    print("! a palindrome")


























































