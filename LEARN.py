cardnumber=input("Enter the cardnumber :")
cardnumber=cardnumber.split(" ")
cardnumber="".join(cardnumber)
cardnumber=cardnumber.split("-")
cardnumber="".join(cardnumber)
ncardnumber=cardnumber
ncard=[]
for n in ncardnumber:
    ncard.append(int(n))
length=len(ncard)
calcard=[]
calcard.append(ncard[-1])
necard=ncard[0:-1]
necard=necard[::-1]
for count,n in enumerate(necard,start=2):
    if count%2 ==0:
        n=n*2
        if(n>9):
            n=n-9
    else:
        n=n
    calcard.append(n)
sum=0
for cal in calcard:
    sum=sum+cal
if sum%10 == 0:
    print(f"{cardnumber} is a valid card")
else:
    print(f'{cardnumber} is not valid card please recheck the card number you entered')