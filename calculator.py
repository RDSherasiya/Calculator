
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplicatioin")
    print("4. Division")
    print("5. Exit")
  
    choice = input("Enter your choice : ")

    

    if choice == "1":
        num1 = float(input("Enter Number 1 : "))
        num2 = float(input("Enter Number 2 : "))
        print("Addition of two Numbers is = ", (num1+num2))
    elif choice == "2":
        num1 = float(input("Enter Number 1 : "))
        num2 = float(input("Enter Number 2 : "))
        print("Subtraction of two Numbers is = ", (num1-num2))
    elif choice == "3":
        num1 = float(input("Enter Number 1 : "))
        num2 = float(input("Enter Number 2 : "))
        print("Multiplication of two Numbers is = ", (num1*num2))
    elif choice == "4":
        num1 = float(input("Enter Number 1 : "))
        num2 = float(input("Enter Number 2 : "))
        if num2 == "0.0":
            print("Divide by 0 Error.")
        else:
            print("Division of two Numbers is = ", (num1/num2))
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
