#Author: Nikita Dancik
#Purpose:Temperature Converter

# Input 
sName = input("What is you name: ")

print("Good morning", sName, "My name is Nikita.")
print("Here is my Temperature Converter")

sTemp = float( input("What is the temperature:  "))

sTemp1 = input("Is the temperature in F for Fahrenheit or C for Celsius: ")


# Compute and Output
if sTemp1 == "F":
    f_Celsius = float(format((5.0/9)*(sTemp - 32),'.1f'))
    print("The Celsius equivalent is:", f_Celsius)

    if f_Celsius >= 100:
        print("Temp can not be > 100")
    raise SystemExit
    
if sTemp1 == "C":
     f_Fahrenheit = float(format((9.0/5.0)* sTemp + 32,'.1f'))
     print("The Fahrenheit equivalent is:", f_Fahrenheit)

     if f_Fahrenheit >= 212:
         print("Temp can not > 212")
         raise SystemExit

if():
    print("Must enter a F or C")

print("exiting")
raise SystemExit






