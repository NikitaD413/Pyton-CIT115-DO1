#Author: Nikita Dancik
#Purpose: Compound Interest

#Constants
#Principal Investment(PV)
#Interest Rate(R)
#Number of Periods(T)
#Compounding(M)
#Future Value(FV)

#Input
sPV=int(input("Enter your principle: "))
sR=float(input("Enter your annual rate: "))
r=float(sR/100)
sM=int(input("How many times per year is the interst compound: "))
sT=int(input("How many years will the account earn interest: "))


#Output

print("A the end of ",sM," years you will have $") 
FV=format(float(input(sPV*(1+(r/sM))**sM*sT)),'.2f')
