#!/usr/bin/python3
# -*- utf-8 -*-

import click
import time
import paho.mqtt.client as mqtt

client = mqtt.Client("client-001")


@click.command()
@click.option("--run", is_flag=True, help="Run it!")

def cli(run):
    if run:
        client.connect("localhost")
        getnumber()

def getnumber():
        countdown()

def countdown():
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