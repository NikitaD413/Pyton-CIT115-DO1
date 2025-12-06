#Purpose: Paint Job with Functions and Output Files
#Author: Nikita Dancik (Dickens)

#States with tax rates
CT: .06
MA: .0625
ME: .085
NH: .0
RI: .07
VT: .06

#Define Main Function
def main():

    customer_file = open(sLast,+'_PaintJobOutput.txt','w')
    
    print('Estimate the cost of a paint job.')
    print()
    sFirst = input("What is your first name: ") 
    sLast = input("What is your last name: ")
    sqft_wall()
    paint_price()
    getGallonsofPaint()
    getLaborHours()
    labor_price()
    sState = input('Job located in what state: ')
    sale_tax(sState)
    customer_name(sLast)
    gallons_of_paint()
    hrs_of_labor()                      
    getPaintCost()
    getLaborCost()
    taxes()
    showCostEstimate()

    customer_file.close()

    print('File' ,customer_file,'was created.')

#Define the square feet of the wall
def sqft_wall():
    sWall = input('Enter wall pace in square feet: ')

#Define the paint price per gallon
def paint_price():
    fPaintPrice = float(input('Enter paint price per gallon: $ '))

#Define the feet per gallon of paint
def getGallonsofPaint():
    fGallon = float(input('Enter feet per gallon: '))

#Define Labor hours per gallon
def getLaborHours():
    fLaborHours = float(input('How many hours of labor per gallon: '))

#Define price of labor per hour
def labor_price():
    fLaborCost = float(input('Labor charge per hour: '))

#Define Gallons of paint needed
def gallons_of_paint():
    fPaintGallon = float(input('Gallons of paint: '))

#Enter the state sales tax
def sale_tax(sState):
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
    else :
        fTax = .0
    print('Sale tax is:',fTax)

#Get the customer name
def customer_name(sLast):
    print('Customer Last Name:',sLast)


#Define hours of labor work
def hrs_of_labor():
    GetLaborHours = float(input(labor_per_gallon * gallons_of_paint))
    print(float(input('Hours of labor:',getLaborHours)))

#Define the total cost of paint
def getPaintCost():
    GetPaintCharges = float(input((paint_price * labor_per_gallon) * sale_tax(sState)))
    print(float(input('Paint Charge:',getPaintCharges)))

#Define the Labor charges
def getLaborCost():
    fGetLaborCost = float(input(hrs_of_labor * labor_price))
    print(float(input('Labor Charge:',getLaborCost)))

#Define total taxes
def taxes():
    GetTax = float(input((paint_charge * labor_charge) * sale_tax(sState)))
    print(float(input('Tax:',getTax)))

#Define the estimated cost
def showCostEstimate():
    ShowCostEstimate = float(input(getPaintCharges + getLaborCost + getTax))
    print(float(input('Total cost:',showCostEstimate)))
    
#
def getFloatInput(getGallonsofPaint):
    try:
        if int(getGallonsofPaint) == float(getGallonsofPaint): 
            return int(getGallonsofPaint),'int'

    except:
        try:
            return float(getGallonsofPaint),'float'
        except:
            return getGallonsofPaint, 'str'
            
def getFloatInput(getLaborHours):
    try:
        if int(getLaborHours) == float(getLaborHours): 
            return int(getLaborHours),'int'

    except:
        try:
            return float(getLaborHours),'float'
        except:
            return getLaborHours, 'str'    

def getFloatInput(getLaborCost):
    try:
        if int(getLaborCost) == float(getLaborCost): 
            return int(getLaborCost),'int'

    except:
        try:
            return float(getLaborCost),'float'
        except:
            return getLaborCost, 'str'

def getFloatInput(getPaintCost):
    try:
        if int(getPaintCost ) == float(getPaintCost ): 
            return int(getPaintCost ),'int'

    except:
        try:
            return float(getPaintCost ),'float'
        except:
            return getPaintCost, 'str'

def getFloatInput(showCostEstimate):
    try:
        if int(showCostEstimate) ==  float(showCostEstimate): 
            return int(showCostEstimate),'int'

    except:
        try:
            return float(showCostEstimate),'float'
        except:
            return showCostEstimate, 'str'
main()  
    
    

    
        
    
    



    
    
    
        
    

    

        
    
