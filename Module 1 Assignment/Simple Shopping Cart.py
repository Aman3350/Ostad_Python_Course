print("\n==Shopping Cart==\n")

x=False

while x==False:
    name=input("Enter customer name: ")

    print("\nEnter Products,\n")
    p1_n=input("Product: ")
    p1_P=int(input("Price: "))
    print()
    p2_n=input("Product: ")
    p2_P=int(input("Price: "))
    print()
    p3_n=input("Product: ")
    p3_P=int(input("Price: "))

    sub_total=p1_P+p2_P+p3_P
    discount=0.00

    if sub_total>=5000:
        discount=sub_total*(20/100)
    elif sub_total>=3000:
        discount=sub_total*(10/100)
    elif sub_total>=1000:
        discount=sub_total*(5/100)
    else:
        discount=0

    final_total=sub_total-discount

    print(f"\nSub Total: {sub_total}")
    print(f"Discount: {discount:.2f}")
    print(f"Total: {final_total:.2f}\n")

    while True:
           temp=input("Exit (Y/N): ")
           print()
           
           if temp=="Y":
               x=True
               break
           elif temp=="N":
               x=False
               break
           else:
               print("Invalid input, try again.\n")