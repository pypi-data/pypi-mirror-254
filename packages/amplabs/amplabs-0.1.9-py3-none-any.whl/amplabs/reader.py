import pandas as pd
import re
from nptdms import TdmsFile
import numpy as np



def readCSV(file_path):
    df = pd.read_csv(file_path)
    return df



def readDAT(file_path):
    try:
        dat_data = []

        regex_patterns = [                                                          # Define the regex patterns and replacements
            (re.compile(r"^(?!1).*.[\r\n|\n]", re.MULTILINE), ""),                  # Remove lines not starting with '1'
            (re.compile(r"^(1\t*ALIAS\t)", re.MULTILINE), ""),                      # Remove lines starting with '1 ALIAS'
            (re.compile(r"^(1.*DATA\t)", re.MULTILINE), ""),                        # Remove lines starting with '1 DATA'
            (re.compile(r"^(1.*PARAMS).*.[\r\n|\n]", re.MULTILINE), ""),            # Remove lines starting with '1 PARAMS'
            (re.compile(r"^(1.*UNITS).*.[\r\n|\n]", re.MULTILINE), ""),             # Remove lines starting with '1 UNITS'
            (re.compile(r"\t+", re.MULTILINE), ","),                                # Replace tabs with commas
        ]

        with open(file_path, 'r', encoding='ISO-8859-1') as file:               # Load the data from the file
            for line in file:
                if not line.startswith("#"):                                        # Apply regex replacements
                    for pattern, replacement in regex_patterns:
                        line = pattern.sub(replacement, line)
                    if line:
                        dat_data.append(line.strip())

        df = pd.DataFrame({'Data': dat_data})                                       # Create a DataFrame from the extracted data
        df = df['Data'].str.split(',',expand=True)
        df.columns = df.iloc[0]                                                     # Adjust the headers of the data
        df = df[1:]
        df.reset_index(drop=True, inplace=True)

        return df       
    except Exception as e:
        print(f"Error: {e}")



def readTDMS(file_path):
    try:
        tdms_file = TdmsFile.read(file_path, True)                                 # Read TDMS file
        df = tdms_file.as_dataframe(True)
        channel_data_dict = {}
        max_length = 0

        for group in tdms_file.groups():                                         # Get group, channel and channel data from the file
            for channel in group.channels():
                channel_data = channel[:]
                if len(channel_data) > max_length:
                    max_length = len(channel_data)
                channel_data_dict[channel.name] = channel_data

        for channel_name, channel_data in channel_data_dict.items():             # Pad the channel data with NaN to match the maximum length
            if len(channel_data) < max_length:
                channel_data_dict[channel_name] = np.concatenate((channel_data, [np.nan] * (max_length - len(channel_data))))

        df = pd.DataFrame(channel_data_dict)                                     # Create a dataframe from the channel data
        df.columns = [col.replace('\n', ' ') for col in df.columns]

        return df                                                                # Return the final dataframe
    except Exception as e:
        print(f"Error: {e}")