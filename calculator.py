print("""****************
CALCULATOR PROGRAM
 
 Transactions;

1.Add

2.Subtract

3.Multiply

4.Divide
****************
""")

a=int(input("First number :"))
b=int(input("Second number :"))
operation=input("Which Transaction?")


if operation == "1":
    print("The total {} with {} is {}.".format(a,b,a + b))
elif operation == "2":
    print("The substarct {} with {} is {}.".format(a,b,a - b))
elif operation == "3":
    print("The multiply {} with {} is {}.".format(a,b,a * b))
elif operation == "4":
    print("The divide {} with {} is {}.".format(a,b,a / b))
else:
    print("Invalid operation!")
