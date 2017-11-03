def fib(n):
    if n <= 1:  
        return 1
    else:
        return (fib(n-1) + fib(n-2))


def gcd(a,b):
    return gcd(b,a%b) if b else abs(a)



def compareTo(s1,s2,index):
    if(len(s1) == index and len(s2) == index):
        return 0
    elif(len(s1) == index and len(s2) > index):
        return -1
    elif(len(s1) > index and len(s2) == index):
        return 1
    elif(s1[index]< s2[index]):
        return -1
    elif(s1[index] > s2[index]):
        return 1
    return compareTo(s1,s2,index+1)



print "\n8th element of Fibonacci sequence is "+str(fib(8))
print"\n--------------------------------------------------\n"
print "GCD of 15 & 18 is "+str(gcd(15,18))
print"\n--------------------------------------------------\n"
string1 = "I love my country"
string2 = "I like to have my own room"
print """\nResult of Comparing strings " """+ string1+""" "  and " """+string2 + """ " is """ +str(compareTo(string1,string2,0))+"\n" 
 