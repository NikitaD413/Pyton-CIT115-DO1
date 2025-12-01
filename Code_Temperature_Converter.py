#Author: Nikita Dancik
#Purpose:Temperature Converter

# Input 
sName = input("What is you name: ")

print("Good morning", sName, "My name is Nikita.")

sTemp = float( input("What is the temperature:  "))

sTemp1 = input("Is the temperature in F for Fahrenheit or C for Celsius: ")

# Compute and Output
if sTemp1 == "F":
    f_Celsius = format((5.0/9)*(sTemp - 32),'.1f')
    print("The Celsius equivalent is:") + f_Celsius 

else:
    print("Must enter a F or C")

raise SystemExit
    
if sTemp1 == "C":
    f_Fahrenheit = format((9.0/5.0)* sTemp + 32,'.1f')
    print("The Fahrenheit equivalent is:") + f_Fahrenheit

else:
 print("Must enter a F or C")
 
raise SystemExit

print("exiting")






