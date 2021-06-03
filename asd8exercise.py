Weight = float(input("What's your weight? "))
Measure = input("(K)g or (L)bs? ")
if Measure == "k" or "K":
    Lbs = Weight * 2.20462
    print("Your weight in Lbs is: " + str(Lbs))
elif Measure == "l" or "L":
    Kgs = Weight * 0.453592
    print("Your weight in Kgs is: " + str(Kgs))
print("Done")
