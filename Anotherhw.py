x = input("Weblink:")
if x[0:8] == "http://" or x[0:9] == "https://":
    print("Web link")
else:
    print("Not web link")   
