import serial as se
import numpy as np
import pandas as pd
import time

reading_time = int(input("Enter the listening duration in seconds:"))


def read_data(reading_time):
    # Waiting for serial port
    print("Looking For serial connection ")
    while True:
        try:
            reader = se.Serial('COM3',2000000)
        except BaseException:
            # print(BaseException)
            continue
        else:
            break

    # after connection established
    print("Connection established")


    start_time = time.time_ns()
    serial_data = []


    print("Reading Sensor data !")
    # listen for 5 secs
    while (time.time_ns()-start_time<reading_time*10**9):  
        serial_data.append(reader.readline().decode('utf-8'))
    print("reading over!")

    # write in intermediate file
    with open('data.txt','w') as file:
        for line in serial_data: 
            file.write(line)


def process_data(data_file_path):

    print("Processing Data!")
    with open(data_file_path,'r') as file:
        data = file.readlines()

    data = data[::2]

    cleaned_data = []
    for indx,line in enumerate(data):
        cleaned_data.append(line.split('\t'))
        cleaned_data[indx][1] = cleaned_data[indx][1].split('\n')[0]

    cleaned_data = np.array(cleaned_data)
    df = pd.DataFrame(cleaned_data)
    df.columns = ["time(micros)","GSR"]

    df.to_csv('./sample-data.csv',index=False)

    print("Done!")

# main_call
read_data(reading_time)
process_data('./data.txt')