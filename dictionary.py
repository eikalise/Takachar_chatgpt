import pandas as pd

df = pd.read_excel("/Users/EIK/Downloads/primary_df.xlsx")

# filter so it only display when data usable = 1

data_dict = {}

for index, row in df.iterrows():
    # Check if the data is usable (column AA == 1)
    if row['data usable'] == 1:
        if int(row['combustor temp rise minute']) == 0 | int(row['combustor temp steady state start minute']) == 0 | int(row['combustor temp steady state end minute']) == 0 | int(row['combustor temp end minute']) == 0:
            print("")
        else:
            date_value = row['date'].strftime("%d%m%y")

            # Extract the data values from columns CV, CW, CX, CY
            data_values = [int(row['combustor temp rise minute']),
                           int(row['combustor temp steady state start minute']),
                           int(row['combustor temp steady state end minute']),
                           int(row['combustor temp end minute'])
                           ]
            data_dict[date_value] = data_values

# Print the resulting dictionary
print(data_dict)
