#Author: Nikita Dancik
#Purpose: Compound Interest w/Loops

#Constants
#Deposit(sPV)
#Interest Rate(sR)
#Number of Months(sM)
#Monthly interest rate (sT)
#Goals(FV)
#iFV =float(input(sPV*(1+(sR/sM))**sM*sT),'.2f')

#Input
sPV=int(input("Enter your deposit: "))
sR=float(input("Enter your annual rate: "))
sT=float(sR/100)
sM=int(input("How many months per year is the interst compound: "))


#Output
iNumber = 1

           
for iNumber in range (1,13):
    
    print("Month",iNumber,'\t\t',"Acount Balance is: $") 

print("It will take months to reach the goal of $",iFV= float(input(sPV*(1+(sR/sM))**sM*sT)))
 
    





