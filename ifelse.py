old =int(input("How old are you?"))
if old < 18:
    print("GET OUT!")
else:
    print("Welcome!")

process=input("Enter a process:")
if process=="1":
    print("Process 1 selected.")
elif process=="2":
    print("Process 2 selected.")
elif process=="3":
    print("Process 3 selected.")
elif process=="4":
    print("Process 4 selected.")
else:
    print("Invalid process!")

note= float(input("Please enter your note:"))

if(note >= 90):
    print("AA")
elif(note>=85):
    print("BA")
elif(note>=80):
    print("BB")
elif(note>=75):
    print("CB")
elif(note>=70):
    print("CC")
elif(note>=65):
    print("DC")
elif(note>=60):
    print("DD")
else:
    print("You failed!")