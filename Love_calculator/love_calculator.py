print("welcome to the love calculator....")
name1=input("what is your name?  \n").lower()
name2=input("what is your lover's name? \n").lower()
#c=name1.count("i")

#if name1.count("i")!=0:
#    c=c+name1.count("i")

#print(c)

c=0 
if name1.count("t")!=0:
    c=c+name1.count("t")
if name1.count("r")!=0:
    c=c+name1.count("r")
if name1.count("u")!=0:
    c=c+name1.count("u")
if name1.count("e")!=0:
    c=c+name1.count("e")
if name1.count("l")!=0:
    c=c+name1.count("l")
if name1.count("o")!=0:
    c=c+name1.count("o")
if name1.count("v")!=0:
    c=c+name1.count("v")


d=0 
if name2.count("t")!=0:
    d=d+name2.count("t")
if name2.count("r")!=0:
    d=d+name2.count("r")
if name2.count("u")!=0:
    d=d+name2.count("u")
if name2.count("e")!=0:
    d=d+name2.count("e")
if name2.count("l")!=0:
    d=d+name2.count("l")
if name2.count("o")!=0:
    d=d+name2.count("o")
if name2.count("v")!=0:
    d=d+name2.count("v")

d=str(c)+str(d)

p= int(d)
if p<10 or p>90:
    print(f"your score is {p}, you go togather like coke and mentos")
elif p>=40 and p<=50:
    print(f"your score is {p}, you are alright togather")
else:
    print(f"your score is {p}")

