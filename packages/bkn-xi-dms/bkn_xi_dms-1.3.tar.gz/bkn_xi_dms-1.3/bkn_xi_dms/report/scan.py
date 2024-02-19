import os
import pandas as pd

# Set the path to the folder containing the Excel files
folder_path = '/path/to/folder'

# Create an empty DataFrame to store the combined data
combined_data = pd.DataFrame()
# Loop through all the Excel files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.xlsx'):  # Check if the file is an Excel file
        file_path = os.path.join(folder_path, file_name)
        data = pd.read_excel(file_path)
        combined_data = combined_data.append(data)

# Save the combined data to a new Excel file
combined_data.to_excel('combined_data.xlsx', index=False)
