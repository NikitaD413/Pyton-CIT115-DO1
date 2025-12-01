# Author: Nikita Dancik
# Inter Planetary Weights

# What is your weight on different planets?
# Your weight on diferent planets: YourWeight x Surface Gravity

Mercury: 0.38
Venus: 0.19
Moon: 0.165
Mars: 0.38
Jupiter: 2.34
Saturn: 0.93
Uranus: 0.92
Neptune: 1.12
Pluto: 0.066


# 1. Input
sName = input("What is your name?")
sEarthWeight = input("What is your weight?")
print (str(sName) + " here are your weights on different planets in our solar system:")

# 2. Convert Data
fEarthWeight = float(sEarthWeight)

# 3. Perform Calculation
fWtMercury = fEarthWeight * 0.38
fWtVenus =fEarthWeight * 0.19
fWtMoon =fEarthWeight * 0.165
fWtMars = fEarthWeight * 0.38
fWtJupiter = fEarthWeight * 2.34
fWtSaturn =fEarthWeight * 0.93
fWtUranus = fEarthWeight * 0.92
fWtNeptune = fEarthWeight * 1.12
fWtPluto = fEarthWeight * 0.066

# 4. Output
print("Your weight on Mercury is: " + str(fWtMercury))
print("Your weight on Venus is: " + str(fWtVenus))
print("Your weight on Moon is: " + str(fWtMoon))
print("Your weight on Mars is: " + str(fWtMars))
print("Your weight on Jupiter is: " + str(fWtJupiter))
print("Your weight on Saturn is: " + str(fWtSaturn))
print("Your weight on Uranus is: " + str(fWtUranus))
print("Your weight on Neptune is: " + str(fWtNeptune))
print("Your weight on Pluto is: " + str(fWtPluto))
