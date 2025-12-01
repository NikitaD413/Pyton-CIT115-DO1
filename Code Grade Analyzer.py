#Author: Nikita Dancik
#Purpose: Code Grade Analyzer

#Grades:
#A+: >=97.0 
#A:  >=94.0 
#A-: >=90.0 
#B+: >=87.0 
#B:  >=84.0 
#B-: >=80.0 
#C+: >=77.0 
#C:  >=74.0 
#C-: >=70.0 
#D+: >=67.0 
#D:  >=64.0 
#D-: >=60.0 
#F:  <=59.9

# 1. Input
sName = input("Name of person we are calculating the grades for: ")
fTest1 = float(input("Enter the score for test 1: "))
fTest2 = float(input("Enter the score for test 2: "))
fTest3 = float(input("Enter the score for test 3: "))
fTest4 = float(input("Enter the score for test 4: "))

#Drop lowest score
if fTest1 < 0 or fTest2 < 0 or fTest3 < 0 or fTest4 < 0:
        print("Test scores must be greater than 0")
        raise SystemExit
sTestDrop = input("Do you want to drop your lowest score? {Y} {N}?")

#Finding lowest score and Dropping Lowest score
if sTestDrop == "Y" or sTestDrop == "y" or sTestDrop == "Yes" or sTestDrop == "yes":
        fTest = 3

        if fTest1 < fTest2 and fTest1 < fTest3 and fTest1 < fTest4:
                fLow = fTest1
        elif  fTest2 < fTest3 and fTest2 < fTest4:
                fLow = fTest2
        elif fTest3 < fTest4:
                fLow = fTest3
        else:
                fLow = fTest4

elif sTestDrop == "N" or sTestDrop == "n" or sTestDrop == "NO" or sTestDrop == "no":
        fTest = 4
        fLow = 0

else:
    print ("Enter Y or N to drop score")
    raise SystemExit

# 2. Calculation
fAverage = (fTest1 + fTest2 + fTest3 + fTest4 - fLow)/fTest
# average = (fTest1 + fTest2 + fTest3 + fTest4)/4
# average1 = (fTest1 + fTest2 + fTest3)/3

#Analyze the Letter Grade base on score  
if fAverage >= 97:
        sGrade = "A+"
       
elif fAverage >= 94.0:
        sGrade = "A"

elif fAverage >= 90.0:
        sGrade = "A-"

elif fAverage >= 87.0:
        sGrade = "B+"

elif fAverage >=  84.0:
        sGrade = "B"

elif fAverage >= 80.0:
        sGrade = "B-"

elif fAverage >= 77.0:
        sGrade = "C+"

elif fAverage >= 74.0:
        sGrade = "C"

elif fAverage >= 70.0:
        sGrade = "C-"

elif fAverage >= 67.0:
        sGrade = "D+"

elif fAverage >= 64.0:
        sGrade = "D"

elif fAverage >= 60.0:
        sGrade = "D-"

elif fAverage <= 59.9:
         sGrade = "F"
    
else :
        print("Enter Y or N to Drop the Lowest Grade.")
        raise SystemExit  

# 3. Output
# write print() to print average anmd format and print letter grade
print("Do you wish to drop the Lowest Grade Y for YES or N for NO?: ")
if ():
        print("Enter Y or N to Drop the Lowest Grade.")
        raise SystemExit

elif "N":
        print(sName," test average is: "+ str(fAverage))
        print("Letter Grade for the test is: "+ sGrade)
        raise SystemExit
    
else : 
        print(sName," test average is: "+ str(fAverage))
        print("Letter Grade for the test is: "+ sGrade)
        raise SystemExit 
 
