#Week 5, Program 1 - Kilometer Converter
#Caiden Heinrichs
#02/20/26

def kilometers_to_miles(kilometers):
    #Calculate miles from inputted kilometers
    miles = kilometers * 0.6214
    return miles

def main():
    #Get input in kilometers
    kilometers = float(input("Enter a measurement in kilometers: "))
    #Convert kilometers to miles
    miles = round(kilometers_to_miles(kilometers), 4)
    #Print the final conversion
    print(kilometers, "kilometers is equal to", miles, "miles.")


if __name__ == "__main__":
    main()
