#!/usr/bin/env python


import glob
import time
import datetime

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


def read_temp_raw():
    reader = open(device_file, 'r')
    lines = reader.readlines()
    reader.close()
    return lines


def read_temp():
    raw_temp_data = read_temp_raw()
    equals_pos = raw_temp_data[1].find('t=')
    if equals_pos != -1:
        temp_string = raw_temp_data[1][equals_pos + 2:]
        temp = float(temp_string) / 1000.0
        return temp


while True:
    log = open("/var/log/env_temperature.log", "a+")
    log.write(f"""DateTime: {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} Temp: {str(read_temp())} \r\n""")
    log.close()
    time.sleep(1800)
