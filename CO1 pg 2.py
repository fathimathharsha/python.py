#Display future leap years from current year to a final year entered by user. 

start=int(input("Enter start year :"))
end=int(input("Enter final year :"))
if(start<end):
    print("Leap years are:")
    for i in range(start, end):
        if (i % 4 == 0 and i % 100 != 0):
            print(i)
else:
    print("Invalid Year")



