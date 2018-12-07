#!/usr/bin/python3
# -*- utf-8 -*-

import click
import time
import paho.mqtt.client as mqtt
import datetime
from .counter import *


@click.command()
@click.option("--run", is_flag=True, help="Count down to new year")
@click.option("--countdown", is_flag=True, help="Count down from 9 to 0")

def cli(run, countdown): 

    if countdown:
        countme()

    elif run:
        print("run")
        countnewyear()