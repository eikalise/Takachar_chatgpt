import os
import pandas as pd
import shutil
from dictionary import data_dict

folder_path = '/Users/EIK/Downloads/Takachar-GPT-main/logs_v6_excels'

for file_name, values in data_dict.items():
    file_path = f"{folder_path}/{file_name}.xlsx"
    if os.path.isfile(file_path):
        try:
            df = pd.read_excel(file_path, engine='openpyxl')
            for index, row in df.iterrows():
                if row[1] <= values[0]:
                    df.loc[index, 'State'] = 'initial'
                elif row[1] <= values[1]:
                    df.loc[index, 'State'] = 'rise'
                elif row[1] <= values[2]:
                    df.loc[index, 'State'] = 'steady'
                elif row[1] <= values[3]:
                    df.loc[index, 'State'] = 'end'
                elif row[1] > values[3]:
                    df.loc[index, 'State'] = ''

            df.to_excel(file_path, index=False)
            print(f"Added 'State' column values to {file_name}.")

            # Move the modified file to the destination folder
            modified_file_path = os.path.join('/Users/EIK/Downloads/Takachar-GPT-main/Final_Excels_Alise', f"{file_name}.xlsx")
            shutil.move(file_path, modified_file_path)
            print(f"Moved the modified file to {modified_file_path}.")


        except pd.errors.ParserError:
            print(f"Skipped {file_name} due to corrupt file.")

    else:
        print(f"File {file_name} does not exist.")

