#asking user to input the number of households they use-
num = input("Enter the number of households: ")
#initializing the count of low, medium and high consumption households, total consumption and a list for storing the consumption values for each households-
lowcount = 0
mediumcount = 0
highcount = 0
totalconsumption = 0
consumption_list = []
for a in range(int(num)) :
    #asking user to input the daily consumption of each household and categorizing them into low, medium and high usage based on the input value of consumption-
    m  = int(input("Enter the daily consumption of household"+str(a+1)+": "))
    totalconsumption += m
    #listing the consumption values for each household  to find out the highest consumption- 
    consumption_list.append(m)
    if m < 5 :
        print("Household"+str(a+1)+": Low Consumption")
        lowcount += 1 #counting the number of low consumption households
    elif m >= 5 and m <= 15 :
        print("Household"+str(a+1)+": Medium Consumption")
        mediumcount += 1 #counting the number of medium consumption households
    else :
        print("Household"+str(a+1)+": High Consumption")
        highcount += 1 #counting the number of high consumption households
print("\nSummary:\n")
print("Low usage households:", lowcount)
print("Medium usage households:", mediumcount)
print("High usage households:", highcount)
print("Average consumption :",totalconsumption/int(num),"kWh")
print("Highest consumption :",max(consumption_list),"kWh")
print("Household with highest consumption:",consumption_list.index(max(consumption_list))+1) #finding the index of the household with the highest consumption and adding 1 to it to get the