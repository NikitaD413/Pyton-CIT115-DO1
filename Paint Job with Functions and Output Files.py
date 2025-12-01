# Purpose: Paint Job with Functions and Output Files
# Author: Nikita Dancik (Dickens)

# States and their tax rate
CT: .06
MA: .0625
ME: .085
NH: .0
RI: .07
VT: .06


## Main Function
def main():
    #Get  name
    get_name()

    # Display Square Feet of the Wall
    sqft_wall()

    # Display
    paint_price()

     # Display
    feet_per_gallon()
    paint_used
    
    # Display
    hour_of_labor()

    # Display
    price_labor()

    # Display
    cost_paint()

    # Display
    sales_tax()

    # Display
    total_cost()


## Get name
def get_name():
    sFirst = input("What is your first name: ") 
    sLast = input("What is your last name: ")
    print('Hello', sFirst, sLast)
    ## Program start-up message explaining what we are doing
    print('Today we will estimate the cost of a paint job.')
    print()
    sState = input('What State is job located: ')

    ## Create a output file
    #customer_file = sLast,+'_PaintJobOutput.txt','w'
    #print('File: ',customer_file, 'was created')
    
    
    ## Find the Square Feet of the Wall
def sqft_wall():
        fWall =float(input('Enter wall space in square feet:'))

## Find the Feet per Gallon of Paint
def feet_per_gallon():
        fGallon = float(input('Enter feet per gallon:'))
    
## Find the Paint Price
def paint_price():
        fPaintPrice = float(input('Enter paint price per gallon:'))

## Amount of paint used
def paint_used():
    fGallon = float(input('How many gallons of paint: '))

## Find the total cost of paint
def cost_paint():    
        fPaintCharges = float(input('Paint charges:', paint_price() * paint_used()))

## Find the Hours of Labor per Gallon
def hour_of_labor():
        fLabor = float(input('How many hours of labor per gallon: '))

## Find the Painting Labor charge per hour
def price_labor():
        fPaintLabor = float(input('Charge of labor:', hour_of_labor() * feet_per_gallon()))
   
## Find the sales tax 
def sales_tax():
        fTaxes = float(input('Tax:'))

## Find the total cost of job
def total_cost():
        fCost = float(input('Total Cost:', price_labor() + cost_paint() + sales_tax()))
    

## Call the main function.
main()
