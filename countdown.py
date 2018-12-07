#!/usr/bin/python3
# -*- utf-8 -*-

import click
import time
import paho.mqtt.client as mqtt

client = mqtt.Client("client-001")


@click.command()
@click.option("--newyear", is_flag=True, help="Count down to new year")
@click.option("--countdown", is_flag=True, help="Count down from 9 to 0")

def cli(newyear, countdown):
    
    if countdown:
        countme()

    elif newyear:
        client.connect("localhost")
        countnewyear()

def countnewyear():
        nowminute = 0

        while True:
                while str(time.localtime()).split(",")[5].split("=")[1] != nowminute:
                        now = int(time.time())
                        newyear = 1546297200
                        nowminute = str(time.localtime()).split(",")[5].split("=")[1]
                        howmanydays = (newyear-now)/3600/24
                        howmanyhours = (newyear-now)/3600
                        howmanyminutes = (newyear-now)/60
                        howmanyseconds = (newyear-now)

                        if howmanyseconds > 0:

                                if howmanyminutes <= 1:
                                        send(howmanyseconds)
                                        print(howmanyseconds)

                                elif howmanyhours <= 1:
                                        send(howmanyminutes)
                                        print(howmanyminutes)

                                elif howmanydays <= 1:
                                        send(howmanyhours)
                                        print(howmanyhours)

                                else:
                                        send(howmanydays)
                                        print(howmanydays)

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

def send(number):
        client.publish("bigsegment/0/set", number)