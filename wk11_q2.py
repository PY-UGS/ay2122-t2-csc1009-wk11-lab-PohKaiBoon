class clockTime: # new class of clockTime
    hours= 0
    minutes= 0
    seconds= 0
    
    def setHours(self, h): #setter for hours
        self.hours=h
    def setMinutes(self, m): #setter for minutes
        self.minutes=m
    def setSeconds(self, s): #setter for seconds
        self.seconds=s
    def setTime(self,h, m, s): #setter for whole time
        self.hours=h
        self.minutes=m
        self.seconds=s
    
    def displayTime(self): # print time set, singular digit will add 0 in the front for accuracy
        
        if (self.hours <10):
            hours= str(self.hours).zfill(2) #set hours with 0 at the front if hours is singular
        else:
            hours= str(self.hours)
        if (self.minutes <10):
            mins= str(self.minutes).zfill(2) #set minutes with 0 at the front if hours is singular
        else:
            mins= str(self.minutes)
            
        if (self.seconds <10):
            secs= str(self.seconds).zfill(2) #set seconds with 0 at the front if hours is singular
        else:
            secs= str(self.seconds)

        print(hours,":", mins, ":", secs) # print the time

time= clockTime() # create new time object

while True:
    try:
        hours= int(input("Enter hours: "))
        if hours >= 0 and hours <= 23:
            break
        print("Please enter a valid hour in 24h format (00-23)")
    except Exception as e:
        print(e)

time.setHours(hours) # set the hours in time

while True:
    try:
        minutes= int(input("Enter minutes: "))
        if minutes >= 0 and minutes <= 59:
            break
        print("Please enter a valid minute in 24h format (00-59)")
    except Exception as e:
        print(e)

time.setMinutes(minutes) # set the minutes in time

while True:
    try:
        seconds= int(input("Enter seconds: "))
        if seconds >= 0 and seconds <= 59:
            break
        print("Please enter a valid second in 24h format (00-59)")
    except Exception as e:
        print(e)

time.setSeconds(seconds) # set the seconds in time
time.displayTime() # display the time






