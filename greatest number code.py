def largestNumber():
    greatestNum = 0
    num1 = int (input("type a number"))
    num2 = int (input("type another number"))
    num3 = int (input("type one last number"))
    if num1 > num2:
        greatestNum = num1
    else:
        greatestNum = num2



    if num3 > greatestNum: 
        greatestNum = num3
    else:
        greatestNum = greatestNum



    print("the greatest number is")
    print(greatestNum)



largestNumber()
