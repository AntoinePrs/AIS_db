# -*- coding: utf-8 -*-
"""
Query AIShub data and store it locally

It is necessary to have an AIShub API key and store it in a 
text file in order to run it. 

Author: Antoine Peris
"""
import requests
import time
import threading


API_KEY = open("API_KEY.txt", "r").read()
FORMAT="1"
OUTPUT="csv"
COMPRESS="2"

url="http://data.aishub.net/ws.php?"+"username="+API_KEY+"&format="+FORMAT+"&output="+OUTPUT+"&compress="+COMPRESS


def get_ais():
    threading.Timer(800, get_ais).start()
    r = requests.get(url)
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%d%m%y_%H%M%S", named_tuple)
    print("AIS "+time_string+ "downloaded")
    name="ais_"+time_string+".csv.bz2"
    open(name, 'wb').write(r.content)

get_ais()