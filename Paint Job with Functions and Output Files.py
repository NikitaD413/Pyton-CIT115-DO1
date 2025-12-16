#Purpose: Paint Job with Functions and Output Files
#Author: Nikita Dancik (Dickens)

import math

#States with tax rates
CT: .06
MA: .0625
ME: .085
NH: .0
RI: .07
VT: .06

## def getFloatInput
def getFloatInput(sInput):
    while True:
        try:
            fValue = float(input(sInput))
            if fValue <= 0:
                print("Input must be a positive numeric value")
            else:
                return fValue
        except ValueError:
                print("Input must be a positive numeric value")

#Define Gallons of paint 
def getGallonsOfPaint(fWallSize,fFeetPerGallon):
    fGallonsNeeded = fWallSize/ fFeetPerGallon
    iGallonsOfPaint = math.ceil(fGallonsNeeded)
    return iGallonsOfPaint

#Define Labor Cost
def getLaborCost(fLaborHours, fLaborChargePerHour):
    return fLaborHours * fLaborChargePerHour

#Define Labor Hours
def getLaborHours (fLaborHoursPerGallon, iGallonsOfPaint):
    return fLaborHoursPerGallon * iGallonsOfPaint

#Define Paint Cost
def getPaintCost (iGallonsOfPaint, fPaintPrice):
    return iGallonsOfPaint * fPaintPrice

#Enter the state sales tax
def getSaleTax(sState):
    if sState == "Ma" or "MA":
        fTax = .0625
    elif sState == "Ct" or "CT":
        fTax = .06
    elif sState =="Me" or "ME":
        fTax = .085
    elif sState =="Nh" or "NH":
        fTax = .0
    elif sState == "Ri" or "RI":
        fTax  = .07
    elif sState == "Vt" or "VT":
        fTax = .06
    else:
        fTax = .0
    return fTax

#Define the estimated cost
def showCostEstimate(iGallonsOfPaint, fLaborHours, fPaintCost, fLaborCost, fTaxAmount, fTotalCost,sCustomerLastName):
    sFileName = sCustomerLastName + "_PaintJobOut.txt"
    fOutFile = open(sFileName, "w")

    def print_and_write (sLine):
        print (sLine)
        fOutFile.write (sLine + "\n")

    print_and_write ('Gallons of Paint: ' + str(iGallonsOfPaint))
    print_and_write ('Hours of Labor: ' + format(fLaborHours, '.1f'))
    print_and_write ('Paint Charges: ' + format(fPaintCost, '.2f'))
    print_and_write ('Labor Charges: ' + format(fLaborCost, '.2f'))
    print_and_write ('Taxes: ' + format(fTaxAmount, '.2f'))
    print_and_write ('Total Cost: ' + format(fTotalCost, '.2f'))

    fOutFile.close()
    print("File:",sFileName, 'was created.')

#Define Main Function
def main():
    #User input
    #Define the square feet of the wall
    fWallSize = getFloatInput('Enter wall pace in square feet: ')
    #Define the paint price per gallon
    fPaintPrice = getFloatInput('Enter paint price per gallon: $')
    #Define the feet per gallon of paint
    fFeetPerGallon = getFloatInput('Enter feet per gallon: ')
   #Define Labor hours per gallon
    fLaborHoursPerGallon = getFloatInput('How many labor hours per gallon: ')
    #Define price of labor per hour
    fLaborChargePerHour = getFloatInput('Labor charge per hour: ') 
    sCustomerLastName = input("What is your last name: ")
    sState = input('Job located in what state: ')

    #Calculate
    iGallonsOfPaint = getGallonsOfPaint(fWallSize,fFeetPerGallon)
    fLaborHours = getLaborHours (fLaborHoursPerGallon, iGallonsOfPaint)
    fPaintCost = getPaintCost (iGallonsOfPaint, fPaintPrice)
    fLaborCost = getLaborCost(fLaborHours, fLaborChargePerHour)

    #Tax Total
    fTaxRate = getSaleTax(sState)
    fTaxAmount = (fLaborCost + fPaintCost) * fTaxRate
    fTotalCost = fLaborCost + fPaintCost + fTaxAmount

    #Output
    showCostEstimate(iGallonsOfPaint, fLaborHours, fPaintCost, fLaborCost, fTaxAmount, fTotalCost, sCustomerLastName)
   
main()  
    
    

    
        
    
    



    
    
    
        
    

    

        
    
