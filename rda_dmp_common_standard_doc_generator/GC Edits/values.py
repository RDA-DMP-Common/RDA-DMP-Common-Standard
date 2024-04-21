import pandas as pd

# Read the Excel file
xls = pd.ExcelFile('Values.xlsx')

# Get the 'Sheet1' and 'Controlled Vocabulary' sheets
df1 = xls.parse('Sheet1')
df2 = xls.parse('Controlled Vocabulary')
print(df2.iloc[3].values)
# Get the list of IDs from 'Sheet1'
ids = df1['ID'].tolist()

# Initialize a list to store the DataFrames
dfs = []

# For each ID in the list
for id in ids:
    # Find the ID in row 5 of the 'Controlled Vocabulary' sheet
    if id in df2.iloc[3].values:
        # Get the column where the ID is found
        column = df2.columns[df2.iloc[3] == id][0]

        # Initialize an empty list to store the values
        values = []

        # Start from the row below the found ID
        for i in range(4, len(df2)):
            # If the cell is not empty, append the value to the list
            if pd.notna(df2.at[i, column]):
                values.append(df2.at[i, column])
            # If the cell is empty, break the loop
            else:
                break

        # Create a new DataFrame with the values
        df_new = pd.DataFrame(values, columns=[column])

        # Add the five columns to the new DataFrame
        df_new['ID'] = id + "_" + df_new.iloc[:, 0]
        df_new['vocabulary'] = id
        df_new['Property'] = id
        df_new['Label'] = df_new.iloc[:, 0]
        df_new['list_order'] = df_new.index + 1

        # Drop the original column
        df_new = df_new.drop(df_new.columns[0], axis=1)

        # Append the new DataFrame to the list
        dfs.append(df_new)

# Concatenate all DataFrames in the list into a single DataFrame
df_final = pd.concat(dfs, ignore_index=True)

# Write the final DataFrame to a new sheet in the Excel file
with pd.ExcelWriter('Values.xlsx', mode='a', if_sheet_exists='replace') as writer:
    df_final.to_excel(writer, sheet_name='Output')