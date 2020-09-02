weight = 50
rate = 0.2
y = 5
for i in range(y):
    weight *= (1 + rate)
    print("%d." % (i+1),int(weight))
    
x = input("Weblink:")
if x[0:8] == "http://" or x[0:9] == "https://":
    print("Web link")
else:
    print("Not web link")   