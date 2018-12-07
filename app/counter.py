import time
import paho.mqtt.client as mqtt
import datetime

client = mqtt.Client("client-001")
client.connect("localhost")

def countnewyear():
    nowminute = 0

    client.connect("localhost")
    while True:
            while str(time.localtime()).split(",")[5].split("=")[1] != nowminute:
                    now = int(time.time())
                    now_year = int(str(time.localtime()).split(",")[0].split("=")[1])
                    newyear = (time.mktime((datetime.datetime(now_year+1, 1, 1, 0, 0)).timetuple()))
                    nowminute = str(time.localtime()).split(",")[5].split("=")[1]
                    howmanydays = (newyear-now)/3600/24
                    howmanyhours = (newyear-now)/3600
                    howmanyseconds = (newyear-now)

                    if howmanyseconds > 0:

                            if howmanyhours <= 1:
                                    send(int(howmanyseconds))
                                    print(int(howmanyseconds))

                            elif howmanydays <= 1:
                                    send(int(howmanyhours))
                                    print(int(howmanyhours))

                            else:
                                    send(int(howmanydays))
                                    print(int(howmanydays))

                    else:
                            send("happynewyear")
                            print("happynewyear")
                        
            time.sleep(1)

def countme():
        number = 9
        while True:
                while number <= 9 and number != 0:
                        print(number)
                        number-=1
                        time.sleep(1)
                        send(number)

                while number == 0:
                        print(number)
                        number += 9
                        time.sleep(1)
                        send(number)

def send(message):
        digits = str(message)
        i = 0

        while i != len(digits):
                client.publish("bigsegment/%i/set" % (i), "'%s'" % (digits[i]))
                i+=1