def greet(name, time):
    if time == "Morning":
        print("Good Morning", name)
    elif time == "afternoon":
        print("Good Afternoon", name)
    elif time == "evening":
        print("Good Evening", name)
    else:
        print("Hello",name)

name = input ("Enter your name: ")
time = input("Enter time (morning/afternoon/evening): ")

greet(name, time)