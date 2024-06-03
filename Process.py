import pandas as pd
import os
from neurokit2 import eda_process


# conversion equation
def convert_eq(x):
    resistance = (1400 + 2 * x) * 10000 / (700 - x)
    # resistance = (x*(5.0/1023.0))*0.2
    if not resistance:
        print(x)
    return (1 / resistance) * 10**6


def preprocess_sensor_data(source_data_fp: str, destination_folder: str):
    file_name = os.path.basename(source_data_fp)
    print(file_name)
    data = pd.read_csv(source_data_fp)
    # Filter Shorted Conditions(Values >600)
    data = data[data["GSR"] < 600]
    data = data[::100]
    data["skin_resistance"] = data["GSR"].apply(convert_eq)
    # data.to_csv(os.path.join(destination_folder, file_name), index=False)

    processed_data = eda_process(
        data["skin_resistance"], sampling_rate=20, method="neurokit"
    )[0]
    processed_data.to_csv(os.path.join(destination_folder, file_name), index=False)


preprocess_sensor_data(
    "./Collected_Data/Calm_Tirth.csv", "./Preprocessed_Data/Features/"
)
