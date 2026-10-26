size=int(input("Enter an positive size:"))
if size<=0 or size%2==0:
    print("Invalid size. Enter a positive odd number.")
else:
    for width in range(1,size+1,2):
        print(" "*((size-width)//2),end="")
        for number in range(1,width+1):
            print(number,end="")
        print()
    for width in range(size-2,0,-2):
        print(" "*((size-width)//2),end="")
        for number in range(1,width+1):
            print(number, end="")
        print()