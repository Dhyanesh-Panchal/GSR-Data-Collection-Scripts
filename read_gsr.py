import serial as se
import numpy as np
import pandas as pd
import time


def read_data(reading_time: int):
    '''
    read_data() function waits for a serial connection.
    after the connection, it records the data for given time interval -> `reading_time (sec)`.
    output is written in `data.txt` file.  
    '''

    # Waiting for serial port
    print("Looking For serial connection ")
    while True:
        try:
            reader = se.Serial('COM3', 2000000)
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

    while (time.time_ns()-start_time < reading_time*10**9):
        serial_data.append(reader.readline().decode('utf-8'))
    print("reading over!")

    # write in intermediate file
    with open('data.txt', 'w') as file:
        for line in serial_data:
            file.write(line)


# todo: Alter the function to accept file path for final .csv output as parameter.
def process_data(data_file_path):
    '''
    This function processes the Data of of intermediate file (by `read_data()`)
    and writes a csv file of processed Data.
    '''
    print("Processing Data!")
    with open(data_file_path, 'r') as file:
        data = file.readlines()

    # .txt file contains Extra '\n' between each reading, so jumping over those.
    # todo: modify the read_data() to record data conveniently
    data = data[::2]

    cleaned_data = []
    for indx, line in enumerate(data):
        cleaned_data.append(line.split('\t'))
        cleaned_data[indx][1] = cleaned_data[indx][1].split('\n')[0]

    cleaned_data = np.array(cleaned_data)
    df = pd.DataFrame(cleaned_data)
    df.columns = ["time(micros)", "GSR"]

    df.to_csv('./sample-data.csv', index=False)

    print("Done!")


# main_call
if __name__ == '__main__':
    reading_time = int(input("Enter the listening duration in seconds:"))
    read_data(reading_time)
    process_data('./data.txt')
