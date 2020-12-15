print("""**************
Users Login
**************
""")

sys_userName ="suleyman61"
sys_passWord ="denverwade"

userName =input("Username :")
passWord =input("Password :")

if (userName == sys_userName and passWord != sys_passWord):
    print("Incorrect username or password!")
elif (userName != sys_userName and passWord == sys_passWord):
    print("Incorrect username or password!")  
elif (userName != sys_userName and passWord != sys_passWord):
    print("Incorrect username or password!")
else:
    print("You have succesfully signed in...")