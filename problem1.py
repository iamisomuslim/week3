#Temperature Classifier
temp=int(input("Enter temprature in Celsius:"))
if temp<-60 or temp>60:
    print("Invalid temprature")
elif temp<10:
    print("Cold")
elif temp<20:
    print("Cool")
elif temp<=30:
    print("Warm")
elif temp>30:
    print("Hot")