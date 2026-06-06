print("Select your ride: ")
print("1.Bike")
print("2. Car")
choice=int(input("Enter your choice"))
if(choice==1):
    print("what type of bike?")
    print("scooty\n")
    print("scooter\n")
    choice2=int(input("Enter your choice2: "))
    if choice2==1:
     print("You have selected the scooty")
    else:
       print("You have selected scooter")
elif(choice==2):
   print("what type of car?")
   print("1.Sudan")
   print("2.XUV")
   choice3=int(input("enter your choice3:"))
   if choice3==1:
      print("You have selected the Sedan")
   else:
      print("You have selected the XUV")

else:
   print("Wrong choice!")
