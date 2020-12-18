loginpassword = "herepass"
loginpassword=input("Please login your password correctly and push enter :")
if (loginpassword =="herepass"):
    print("""
    Operations:

    1)Balance Inquiry

    2)Deposit Money

    3)Withdraw Money
    Will you for exit press 'x'.
    """)
    balance=2000
    while True:
        operation = input("Please choose your operation what you do :")
        if  (operation == 'x'):
            print("Hope we will see you again!")
            break
        elif (operation == '1'):
            print("Your balance {}".format(balance))
        elif (operation == '2'):
            quantity = int(input("Enter the quantity :"))
            balance += quantity
        elif (operation == '3'):
            quantity = int(input("Enter the quantity :"))
            if (balance - quantity < 0):
                print("Insufficient balance!")
                continue
            balance -= quantity
        else:
            print("Invalid operation!")
else:
    print("Invalid password!")
    