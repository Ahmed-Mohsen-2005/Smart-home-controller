import getpass
from time import *
def timer(deviceq): # timer function to close device after specified time
    global program_timer #imported from the time library
    program_timer = 5
    tocontinue = True
    while tocontinue:
        for i in range(5):
            program_timer -= 1
            sleep(1) #wait 1 sec
        q = input("You have been using this device for a long time, are you sure that you are still using it? ") #ask if the user still needs the use of this device
        if q == "no":
            tocontinue = False
    print(deviceq, "is closed")
def security_t(new):  # A function to limit the entered temperature
    while (new < 10) or (new > 30):
        if new < 10:
            print('too low') #if the temperature is less than 10 it will print too low
        if new > 30:
            print('too high') #if the temperature is greater than 30 it will print too high
        new = int(input('please enter temp again'))
    return 'secure', new #it will return the string "secure" and and the new(limited) temperature
def tempr(bedroom, livingroom, sofra, bathroom, kitchen): #function for adjusting temperature
    bedroom = [t[0], l[0], d[0]]
    livingroom = [t[1], l[1], d[1]]
    sofra = [t[2], l[2], d[2]]
    bathroom = [t[3], l[3], w[0], g[0], d[3]]
    kitchen = [t[4], l[4], w[1], g[1], d[4]]
    room = input("which room you want to change in it? (bedroom,livingroom,sofra,bathroom,kitchen): ")
    confirm = input(f"Are you sure that you want to change the temperature of {room}? ")
    if confirm == "yes":
        newtemp = int(input("enter new temperature: "))
        new = security_t(newtemp) #recall the function of security temp to ensure temp between 10 and 30
        if new[0] == "secure":
            if room == "bedroom":
                print("temperature is changed from", bedroom[0], "to", new[1]) #change the random temp into the new one
                t[0] = int(new[1])
                tempfile = open("temperature.txt", "w") #write it in the text file of temperatures
                tempfile.writelines(str(t))
                tempfile.close()
            elif room == "livingroom":
                print("temperature is changed from", livingroom[0], "to", new[1])
                t[1] = int(new[1])
                tempfile = open("temperature.txt", "w")
                tempfile.writelines(str(t))
                tempfile.close()
            elif room == "sofra":
                print("temperature is changed from", sofra[0], "to", new[1])
                t[2] = int(new[1])
                tempfile = open("temperature.txt", "w")
                tempfile.writelines(str(t))
                tempfile.close()
            elif room == "bathroom":
                print("temperature is changed from", bathroom[0], "to", new[1])
                t[3] = int(new[1])
                tempfile = open("temperature.txt", "w")
                tempfile.writelines(str(t))
                tempfile.close()
            elif room == "kitchen":
                print("temperature is changed from", kitchen[0], "to", new[1])
                t[4] = int(new[1])
                tempfile = open("temperature.txt", "w")
                tempfile.writelines(str(t))
                tempfile.close()
            else:
                print("Wrong syntax")
    else:
        print("Ok")
def devices(bedroom, livingroom, sofra, bathroom, kitchen):
    bedroom = [t[0], l[0], d[0]]
    livingroom = [t[1], l[1], d[1]]
    sofra = [t[2], l[2], d[2]]
    bathroom = [t[3], l[3], w[0], g[0], d[3]]
    kitchen = [t[4], l[4], w[1], g[1], d[4]]
    room = input("which room you want to change in it? (bedroom,livingroom,sofra,bathroom,kitchen) ")
    confirm = input(f"Are you sure that you want to change the device status of {room}? ") #confirmation question to ensure that user wants to change really the device
    if confirm =="yes":
        if room == "livingroom":
            deviceq = input("Do you want to change (TV, Air conditioner, Fan, Electric switch,or speakers)? ")
            if deviceq == "TV":
                new = input("Do you want to open or close TV? ")
                if new =="close":
                    print(f"TV is closed")
                    d[1] = livingroom[2] = "closed" #change the value of the lists into the new value
                    devicefile = open("device.txt", "w") #write the new value in files
                    devicefile.writelines(str(d))
                    devicefile.close()
                else:
                    print(f"TV is {new}ed")
                    d[1] = livingroom[2] = "opened" #change the value of the lists into the new value
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
            elif deviceq == "air conditioner":
                new = input("Do you want to open or close Air conditioner? ")
                if new =="close":
                    print(f"Air conditioner is closed")
                    d[1] = livingroom[2] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                if new == "open":
                    d[1] = livingroom[2] = "opened" #opening the device after the user choose to open it
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                    timer(deviceq) #recalling the function of timer
                    d[1] = livingroom[2] = "closed" #closing the device again after the end of the timer
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                print(f"Air conditioner is {new}ed")
            elif deviceq == "fan":
                new = input("Do you want to open or close Fan? ")
                if new =="close":
                    print(f"Fan is closed")
                    d[1] = livingroom[2] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                else:
                    print(f"Fan is {new}ed")
                    d[1] = livingroom[2] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
            elif deviceq == "electric switch":
                new = input("Do you want to open or close Electric switch? ")
                if new =="close":
                    print(f"Electric switch is closed")
                    d[1] = livingroom[2] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                else:
                    print(f"Electric switch is {new}ed")
                    d[1] = livingroom[2] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
            elif deviceq == "speakers":
                new = input("Do you want to open or close speakers? ")
                if new =="close":
                    print(f"Speakers are closed")
                    d[1] = livingroom[2] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                else:
                    print(f"speakers are {new}ed")
                    d[1] = livingroom[2] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
        elif room == "bedroom":
            deviceq = input("Do you want to change (TV, Air conditioner, Fan, Steam iron, curtains, trademill or speakers)? ")
            if deviceq == "TV":
                new = input("Do you want to open or close TV? ")
                if new == "close":
                    print(f"TV is closed")
                    d[0] = bedroom[2] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                else:
                    print(f"TV is {new}ed")
                    d[0] = bedroom[2] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
            elif deviceq == "air conditioner":
                new = input("Do you want to open or close Air conditioner? ")
                if new =="close":
                    print(f"Air conditioner is closed")
                    d[0] = bedroom[2] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                if new == "open":
                    d[0] = bedroom[2] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                    timer(deviceq)
                    d[0] = bedroom[2] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                    print(f"Air conditioner is {new}ed")
            elif deviceq == "fan":
                new = input("Do you want to open or close fan? ")
                if new =="close":
                    print(f"Fan is closed")
                    d[0] = bedroom[2] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                else:
                    print(f"Fan is {new}ed")
                    d[0] = bedroom[2] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
            elif deviceq == "trademill":
                new = input("Do you want to open or close trademill? ")
                if new =="close":
                    print(f"Trademill is closed")
                    d[0] = bedroom[2] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                else:
                    print(f"Trademill is {new}ed")
                    d[0] = bedroom[2] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
            elif deviceq == "speakers":
                new = input("Do you want to open or close speakers? ")
                if new =="close":
                    print(f"Speakers are closed")
                    d[0] = bedroom[2] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                else:
                    print(f"Speakers are {new}ed")
                    d[0] = bedroom[2] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
            elif deviceq == "curtains":
                new = input("Do you want to open or close curtains? ")
                if new =="close":
                    print(f"Curtians are closed")
                    d[0] = bedroom[2] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                else:
                    print(f"Curtians are {new}ed")
                    d[0] = bedroom[2] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
            elif deviceq == "steam iron":
                new = input("Do you want to open or close steam iron? ")
                if new =="close":
                    print(f"Steam iron is closed")
                    d[0] = bedroom[2] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                if new == "open":
                    print(f"Steam iron is {new}ed")
                    d[0] = bedroom[2] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                    timer(deviceq)
                    d[0] = bedroom[2] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()

        elif room == "bathroom":
            deviceq = input("Do you want to change (Air suction or washing machine)? ")
            if deviceq == "air suction":
                new = input("Do you want to open or close air suction? ")
                if new =="close":
                    print(f"Air suction is closed")
                    d[3] = bathroom[4] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                if new == "open":
                    print(f"Air suction is {new}ed")
                    d[3] = bathroom[4] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                    timer(deviceq)
                    d[3] = bathroom[4] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
            elif deviceq == "washing machine":
                new = input("Do you want to open or close washing machine? ")
                if new =="close":
                    print(f"Washing machine is closed")
                    d[3] = bathroom[4] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                else:
                    print(f"Washing machine is {new}ed")
                    d[3] = bathroom[4] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
        elif room == "sofra":
            deviceq = input("Do you want to change (Curtains, self vaccum cleaner or speakers)? ")
            if deviceq == "curtains":
                new = input("Do you want to open or close Curtains? ")
                if new =="close":
                    print(f"Curtains are closed")
                    d[2] = sofra[2] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                else:
                    print(f"Curtains are {new}ed")
                    d[2] = sofra[2] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
            elif deviceq == "self vaccum cleaner":
                new = input("Do you want to open or close vaccum cleaner? ")
                if new =="close":
                    print(f"Vaccum cleaner is closed")
                    d[2] = sofra[2] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                else:
                    print(f"Vaccum cleaner is {new}ed")
                    d[2] = sofra[2] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
            elif deviceq == "speakers":
                new = input("Do you want to open or close speakers? ")
                if new =="close":
                    print(f"Speakers are closed")
                    d[2] = sofra[2] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                else:
                    print(f"Speakers are {new}ed")
                    d[2] = sofra[2] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
        elif room == "kitchen":
            deviceq = input("Do you want to change (Blender, Dish washer, Microwave, Air suction, or Electric switch)? ")
            if deviceq == "blender":
                new = input("Do you want to open or close Blender? ")
                if new =="close":
                    print(f"Blender is closed")
                    d[4] = kitchen[4] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                else:
                    print(f"Blender is {new}ed")
                    d[4] = kitchen[4] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
            elif deviceq == "dish washer":
                new = input("Do you want to open or close dish washer? ")
                if new == "close":
                    print(f"Dish washer is closed")
                    d[4] = kitchen[4] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                else:
                    print(f"Dish washer is {new}ed")
                    d[4] = kitchen[4] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
            elif deviceq == "microwave":
                new = input("Do you want to open or close Microwave? ")
                if new == "close":
                    print(f"Microwave is closed")
                    d[4] = kitchen[4] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                if new == "open":
                    print(f"Microwave is {new}ed")
                    d[4] = kitchen[4] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                    timer(deviceq)
                    d[4] = kitchen[4] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
            elif deviceq == "air suction":
                new = input("Do you want to open or close air suction? ")
                if new =="close":
                    print(f"Air suction is closed")
                    d[4] = kitchen[4] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                if new == "open":
                    print(f"Air suction is {new}ed")
                    d[4] = kitchen[4] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                    timer(deviceq)
                    d[4] = kitchen[4] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
            elif deviceq == "electric switch":
                new = input("Do you want to open or close electric switch? ")
                if new == "close":
                    print(f"Electric switch is closed")
                    d[4] = kitchen[4] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                if new == "open":
                    print(f"Electric switch is {new}ed")
                    d[4] = kitchen[4] = "opened"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
                    timer(deviceq)
                    d[4] = kitchen[4] = "closed"
                    devicefile = open("device.txt", "w")
                    devicefile.writelines(str(d))
                    devicefile.close()
            else:
                print("Wrong syntax")
        else:
            print("Wrong syntax")
    elif confirm == "no":
        print("ok")
    else:
        print("Wrong syntax")
def light(bedroom, livingroom, sofra, bathroom, kitchen):
    bedroom = [t[0], l[0], d[0]]
    livingroom = [t[1], l[1], d[1]]
    sofra = [t[2], l[2], d[2]]
    bathroom = [t[3], l[3], w[0], g[0], d[3]]
    kitchen = [t[4], l[4], w[1], g[1], d[4]]
    room = input("Which room you want to change in it? (bedroom,livingroom,sofra,bathroom,kitchen) : ")
    new = input("Do you want to turn it (on, off)? ")
    if room == "bedroom":
        bedroom[1] = new #changing the old value to the new value
        print(f"light in bedroom is turned", new)
        l[0] = new
        lightfile = open("light.txt", "w")
        lightfile.writelines(str(l)) #writing the new value in files
        lightfile.close()
    elif room == "livingroom":
        livingroom[1] = new
        print(f"light in livingroom is turned", new)
        l[1] = new
        lightfile = open("light.txt", "w")
        lightfile.writelines(str(l))
        lightfile.close()
    elif room == "sofra":
        sofra[1] = new
        print(f"light in sofra is turned", new)
        l[2] = new
        lightfile = open("light.txt", "w")
        lightfile.writelines(str(l))
        lightfile.close()
    elif room == "bathroom":
        bathroom[1] = new
        print(f"light in bathroom is turned", new)
        l[3] = new
        lightfile = open("light.txt", "w")
        lightfile.writelines(str(l))
        lightfile.close()
    elif room == "kitchen":
        kitchen[1] = new
        print(f"light in kitchen is turned", new)
        l[4] = new
        lightfile = open("light.txt", "w")
        lightfile.writelines(str(l))
        lightfile.close()
    else:
        print("Wrong syntax")
def water(bathroom, kitchen):
    bathroom = [t[3], l[3], w[0], g[0], d[3]]
    kitchen = [t[4], l[4], w[1], g[1], d[4]]
    room = input("which room you want to change in it? (bathroom , kitchen or both): ")
    confirm = input(f"Are you sure that you want to change the water status of {room}? ") #confirmation question to ensure that user wants to change really the device
    if confirm == "yes":
        if room == "bathroom":
            bath = input("change (tap or bathtub or washing machine) ")
            if bath == "tap":
                print("tap water is", bathroom[2])
                new = input("do you want to open or close water? : ")
                if new =="close":
                    print(f"tap water is closed")
                    w[0] =bathroom[2]= "closed" #changing the old value to the new value in lists
                    waterfile = open("water.txt", "w") #writing the new value in files
                    waterfile.writelines(str(w))
                    waterfile.close()
                else:
                    print(f"tap water is {new}ed")
                    w[0] = bathroom[2]= "opened"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
            elif bath == "bathtub":
                print("bathtub water is", bathroom[2])
                new = input("do you want to open or close water? : ")
                if new == "close":
                    print(f"bathtub water is closed")
                    w[0] = bathroom[2]= "closed"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
                else:
                    print(f"bathtub water is {new}ed")
                    w[0] = bathroom[2]= "opened"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
            elif bath == "washing machine":
                print("washing machine water is", bathroom[2])
                new = input("do you want to open or close water? : ")
                if new == "close":
                    print(f"Washing machine is closed")
                    w[0] =bathroom[2]= "closed"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
                else:
                    print(f"Washing machine is {new}ed")
                    w[0] = bathroom[2]="opened"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
        elif room == "kitchen":
            bath = input("change (tap or dish washer)")
            if bath == "tap":
                print("tap water is", kitchen[2])
                new = input("do you want to open or close water? : ")
                if new == "close":
                    print(f"tap water is closed")
                    w[1] = kitchen[2] ="closed"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
                else:
                    print(f"tap water is {new}ed")
                    w[1] = kitchen[2] ="opened"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
            elif bath == "dish washer":
                print("dish washer water is", kitchen[2])
                new = input("do you want to open or close water? : ")
                if new == "close":
                    print(f"Dish washer water is closed")
                    w[1] = kitchen[2] = "closed"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
                else:
                    print(f"Dish washer water is {new}ed")
                    w[1] = kitchen[2] = "opened"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
        elif room == "both":
            bath = input("Do you want to change(tap or bathtub or washing machine) in bathroom? ")
            if bath == "tap":
                print("tap water is", bathroom[2])
                new = input("Do you want to open or close water? : ")
                if new == "close":
                    print(f"tap water is closed")
                    w[0] = bathroom[2]= "closed"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
                else:
                    print(f"tap water is {new}ed")
                    w[0] = bathroom[2]= "opened"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
            elif bath == "bathtub":
                print("bathtub water is", bathroom[2])
                new = input("do you want to open or close water? : ")
                if new == "close":
                    print(f"bathtub water is closed")
                    w[0] = bathroom[2]= "closed"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
                else:
                    print(f"bathtub water is {new}ed")
                    w[0] = bathroom[2]= "opened"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
            elif bath == "washing machine":
                print("washing machine water is", bathroom[2])
                new = input("do you want to open or close water? : ")
                if new == "close":
                    print(f"Washing machine water is closed")
                    w[0] = bathroom[2]= "closed"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
                else:
                    print(f"Washing machine water is {new}ed")
                    w[0] = bathroom[2]= "opened"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
            else:
                print("Wrong syntax")
            print("......................")
            bath = input("Do you want to change (tap or dish washer) in kitchen? ")
            if bath == "tap":
                print("tap water is", kitchen[2])
                new = input("do you want to open or close water? : ")
                if new =="close":
                    print(f"tap water is closed")
                    w[1] = kitchen[2] = "closed"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
                else:
                    print(f"tap water is {new}ed")
                    w[1] = kitchen[2] = "opened"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
            elif bath == "dish washer":
                print("dish washer water is", kitchen[2])
                new = input("do you want to open or close water? : ")
                if new == "close":
                    print(f"Dish washer water is closed")
                    w[1] = kitchen[2] = "closed"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
                else:
                    print(f"Dish washer water is {new}ed")
                    w[1] = kitchen[2] = "opened"
                    waterfile = open("water.txt", "w")
                    waterfile.writelines(str(w))
                    waterfile.close()
            else:
                print("Wrong syntax")
        else:
            print("Wrong syntax")
    elif confirm == "no":
        print("ok")
    else:
        print("Wrong syntax")
def gas(bathroom, kitchen):
    bathroom = [t[3], l[3], w[0], g[0], d[3]]
    kitchen = [t[4], l[4], w[1], g[1], d[4]]
    room = input("which room you want to change in it?(bathroom , kitchen): ")
    confirm = input(f"Are you sure that you want to change the gas of {room}? ")  #confirmation question to ensure that user wants to change really the device
    if confirm == "yes":
        if room == "kitchen":
            bath = input("change (butagas only) ")
            if bath == "butagas":
                print("butagas gas is", kitchen[3])
                new = input("do you want to open or close the gas? : ")
                if new == "close":
                    print(f"butagas gas is closed")
                    g[1] = kitchen[3]= "closed" #updating the old value to the new value
                    gasfile = open("gas.txt", "w")
                    gasfile.writelines(str(g))# writing the new values in file
                    gasfile.close()
                if new == "open":
                    print(f"butagas gas is {new}ed")
                    g[1] = kitchen[3]= "opened"
                    gasfile = open("gas.txt", "w")
                    gasfile.writelines(str(g))
                    gasfile.close()
                    timer(bath)
                    g[1] = kitchen[3]= "closed"
                    gasfile = open("gas.txt", "w")
                    gasfile.writelines(str(g))
                    gasfile.close()
        elif room == "bathroom":
            bath = input("change (heater only) ")
            if bath == "heater":
                print("heater gas is", bathroom[3])
                new = input("do you want to open or close the gas? : ")
                if new == "close":
                    print(f"heater gas is closed")
                    g[0] = bathroom[3] ="closed"
                    gasfile = open("gas.txt", "w")
                    gasfile.writelines(str(g))
                    gasfile.close()
                if new == "open":
                    print(f"heater gas is {new}ed")
                    g[0] = bathroom[3] ="opened"
                    gasfile = open("gas.txt", "w")
                    gasfile.writelines(str(g))
                    gasfile.close()
                    timer(bath)
                    g[0] = bathroom[3] ="closed"
                    gasfile = open("gas.txt", "w")
                    gasfile.writelines(str(g))
                    gasfile.close()
    elif confirm == "no":
        print("ok")
    else:
        print("Wrong syntax")
def user_info(p): #checking the validity of the password
    x = 0
    n = 0
    z = 0
    for i in p:
        if i.isupper(): #check if the letter is capatilized
            n += 1
        if i.isdigit(): #check if the letter is digit
            x += 1
        if i == "@" or i == "*" or i == "/" or i == "_": #check if the letter is special character
            z += 1
    while (len(p) < 8) or (n < 1 and x < 1 and z < 1): #putting the password in while loop until the user enters a valid one of 8 digits and with all requirements
        if len(p) < 8:
            print("password must be 8 digit at least!,enter password again")
        if n < 1 and x < 1 and z < 1:
            print("enter stronger password")
        p = pasword_mask()
        for i in p:
            if i.isupper():
                n += 1
            if i.isdigit():
                x += 1
            if i == "@" or i == "*" or i == "/" or i == "_":
                z += 1
    return "strong password"
def pasword_mask():
    password = input("Enter your password ") #encrypting the password after inputing it by getpaas library
    return password
def Save_user(user, password, mode):
    userfile = open('users.txt', 'r')# open the file to read from it
    data = userfile.readline()# put the contents of the text file in data variable
    while user in data:
       print("Username is already found")#if the username is not unique, it refuse to take it
       user = input("Enter username: ")#ask to take another username
       password = pasword_mask()
       pass_check = user_info(password)
       print(pass_check)
    userfile = open('users.txt', 'a')#adding the unique username
    userfile.write("Username: " + user + "\t Password: " + password + "\t" + "Mode: " + mode + " mode" + "\n") #printing the information of the user in the file of users
    print("Signed up successfully")
    userfile.close()

def login():
    print("Welcome back! Please log in.")
    username = input("Enter your username: ")#ask to take the username
    userfile = open("users.txt", "r")#open the file to read it
    data = userfile.read()# put the contents of the text file in data variable
    while username not in data:#check if the username is in the users file or not
        username = input("Username not found. Please check your username or sign up.")
    password = pasword_mask()
    while password not in data:#check if the password is in the users file or not
        password = input("Incorrect password. Please try again.")
    print("Login successful <3")

def Save_info(t, l, w, g, d): # put the lists in separated files
    tempfile.writelines(str(t)) # write the values lists
    waterfile.writelines(str(w))
    gasfile.writelines(str(g))
    lightfile.writelines(str(l))
    devicefile.writelines(str(d))
    tempfile.close() #closing the files
    waterfile.close()
    gasfile.close()
    lightfile.close()
    devicefile.close()
def rand(): #random the status of the rooms
    import random
    home = ["bedroom", "livingroom", "sofra", "bathroom", "kitchen"]
    r = ["on", "off"]
    k = ["opened", "closed"]
    for i in home:
        if i == "kitchen" or i == "bathroom":
            temp = random.randint(10, 30) #randomizing values
            light = r[random.randint(0, 1)]
            water = k[random.randint(0, 1)]
            gas = k[random.randint(0, 1)]
            devices = k[random.randint(0, 1)]
            print(i, "temperature is", temp) #print the random values for the user
            print(i, "light is turned", light)
            print(i, "water is", water)
            print(i, "gas is", gas)
            print(i, "devices are", devices)
            t.append(temp) # append the values in the empty lists
            l.append(light)
            w.append(water)
            g.append(gas)
            d.append(devices)
        else:
            temp = random.randint(10, 30)
            light = r[random.randint(0, 1)]#print the random values for the user
            devices = k[random.randint(0, 1)]
            print(i, "temperature is", temp)
            print(i, "light is turned", light)
            t.append(temp)
            l.append(light) # append the values in the empty lists
            d.append(devices)
    return t, l, w, g, d # return the lists after filling their values
def parent_mode(change): # can control everything
    bedroom = [t[0], l[0], d[0]]
    livingroom = [t[1], l[1], d[1]]
    sofra = [t[2], l[2], d[2]]
    bathroom = [t[3], l[3], w[0], g[0], d[3]]
    kitchen = [t[4], l[4], w[1], g[1], d[4]]
    if change == "yes":
        thing = input("Which thing you want to change? (temperature, water, gas, light, device) : ")
        if thing == "temperature":
            tempr(bedroom, livingroom, sofra, bathroom, kitchen) #recall the function of each feature
        elif thing == "light":
            light(bedroom, livingroom, sofra, bathroom, kitchen)#recall the function of each feature
        elif thing == "water":
            water(bathroom, kitchen)#recall the function of each feature
        elif thing == "gas":
            gas(bathroom, kitchen)#recall the function of each feature
        elif thing == "device":
            devices(bedroom, livingroom, sofra, bathroom, kitchen) #recall the function of each feature
        else:
            print("Wrong syntax")
        again = input("Do you want to change another thing? ")
        if again == "no":
            print("ok,app is closed")
        while again == "yes": # this will be repeted every time the user enter yes
            thing = input("Which thing you want to change? (temperature, water, gas, light, device): ")
            if thing == "temperature":
                tempr(bedroom, livingroom, sofra, bathroom, kitchen)#recall the function of each feature
            elif thing == "light":
                light(bedroom, livingroom, sofra, bathroom, kitchen)#recall the function of each feature
            elif thing == "water":
                water(bathroom, kitchen)#recall the function of each feature
            elif thing == "gas":
                gas(bathroom, kitchen)#recall the function of each feature
            elif thing == "device":
                devices(bedroom, livingroom, sofra, bathroom, kitchen)#recall the function of each feature
            else:
                print("Wrong syntax")# if it is unstuitable response
            again = input("Do you want to change another thing? ")
            if again == "no":
                print("ok,app is closed")#closing the app
                break
    elif change == "no":
        print("home status will not change")  #if the user don't want to change the status of the home
    else:
        print("Wrong syntax")# if it is unstuitable response
def child_mode(change): #can control only light, water and device (not the gas or the temperature)
    bedroom = [t[0], l[0], d[0]]
    livingroom = [t[1], l[1], d[1]]
    sofra = [t[2], l[2], d[2]]
    bathroom = [t[3], l[3], w[0], g[0], d[3]]
    kitchen = [t[4], l[4], w[1], g[1], d[4]]
    if change == "yes":
        thing = input("Which thing you want to change? (water, light, device) : ")# choose thing to change
        if thing == "light":
            light(bedroom, livingroom, sofra, bathroom, kitchen)#recall the function of each feature
        elif thing == "water":
            water(bathroom, kitchen)#recall the function of each feature
        elif thing == "device":
            devices(bedroom, livingroom, sofra, bathroom, kitchen)#recall the function of each feature
        else:
            print("Wrong syntax")
        again = input("Do you want to change another thing? ")
        if again == "no":
            print("ok,app is closed")
        while again == "yes": # choose thing to change again another time
            thing = input("Which thing you want to change? (water, light, device): ")
            if thing == "light":
                light(bedroom, livingroom, sofra, bathroom, kitchen)#recall the function of each feature
            elif thing == "water":
                water(bathroom, kitchen)#recall the function of each feature
            elif thing == "device":
                devices(bedroom, livingroom, sofra, bathroom, kitchen)#recall the function of each feature
            else:
                print("Wrong syntax")# if it is unstuitable response
            again = input("Do you want to change another thing? ")
            if again == "no":
                print("ok,app is closed") #closing the app
                break
    elif change == "no":
        print("home status will not change") #if the user don't want to change the status of the home
    else:
        print("Wrong syntax")# if it is unstuitable response

t = [] #defining the empty lists
l = []#defining the empty lists
w = []#defining the empty lists
g = []#defining the empty lists
d = []#defining the empty lists
tempfile = open("temperature.txt", "w") #opening the features files to fill them
waterfile = open("water.txt", "w")#opening the features files to fill them
gasfile = open("gas.txt", "w")#opening the features files to fill them
lightfile = open("light.txt", "w")#opening the features files to fill them
devicefile = open("device.txt", "w")#opening the features files to fill them
