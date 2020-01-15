# -*- coding: utf-8 -*-
"""
Query AIShub data and store it locally

It is necessary to have an AIShub API key and store it in a 
text file in order to run it. 

Author: Antoine Peris
"""
import time
import os
import pandas as pd


os.getcwd()

API_KEY = open("API_KEY.txt", "r").read()
FORMAT="1"
OUTPUT="csv"
COMPRESS="0"
XMIN="2.329102"
YMIN="49.389524"
XMAX="7.767334"
YMAX="53.859007"


url="http://data.aishub.net/ws.php?"+"username="+API_KEY+"&format="+FORMAT+"&output="+OUTPUT+"&compress="+COMPRESS+"&latmin="+YMIN+"&latmax="+YMAX+"&lonmin="+XMIN+"&lonmax="+XMAX

def get_ais():
    df = pd.read_csv(url)   
    df=df[['TSTAMP','MMSI','NAVSTAT','SOG','COG','NAME','TYPE','LONGITUDE','LATITUDE']]
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%Y%m%d_%H%M%S", named_tuple)
    print("AIS "+time.strftime("%d/%m/%Y %H:%M:%S", named_tuple)+ " downloaded")
    name="ais_"+time_string+".csv.gz"
    df.to_csv(name, index = None, header=True,  compression='gzip')

    
while True:
    get_ais()
    time.sleep(120)

