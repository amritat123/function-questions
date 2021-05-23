#in this question driver ki speed nikalo....
def driver(speed):
    if speed<=70:
        print("ok")
    else:
        speed_1=(speed-70)//5
        if speed_1>12:
            print("licsense suspended ")
        else:
            print("point=",speed_1)
speed=int(input("enter the driver speed "))
driver(speed)


