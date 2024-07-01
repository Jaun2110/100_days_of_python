year = int(input("enter the year:\n"))

isLeap = "Leap year"
isNotLeap = "Not  leap year"


if year % 4 == 0:
    if year % 100 == 0:
        print(isNotLeap)
        if year % 400 == 0:
            print(isLeap)
        else:
            print(isNotLeap)
    else:
        print(isLeap)
else:

    print(isNotLeap)


