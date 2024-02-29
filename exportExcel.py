import pandas as pd
# this code generate using AI
def saveExcel(df,name,sheet):
    # Create a Pandas Excel writer using XlsxWriter as the engine
    writer = pd.ExcelWriter(name+".xlsx", engine='xlsxwriter')

    # Convert the DataFrame to an XlsxWriter Excel object, omitting the header and index
    df.to_excel(writer, sheet_name=sheet, index=False, header=False)

    # Get the xlsxwriter workbook and worksheet objects
    workbook  = writer.book
    worksheet = writer.sheets[sheet]

    # Create a border format
    border_format = workbook.add_format({'border':2,'align':'center','valign':'vcenter'})

    # Set the column width and row height to make cells look more square
    worksheet.set_column(0, df.shape[1], 2.5)
    worksheet.set_default_row(18)

    # Iterate over the cells in the dataframe
    for row_num, row_data in enumerate(df.values):
        for col_num, cell_data in enumerate(row_data):
            # Use the border format
            worksheet.write(row_num, col_num, cell_data, border_format)

    # Close the Pandas Excel writer and output the Excel file
    writer.close()


import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame()  # Replace this with your DataFrame

# Create a Pandas Excel writer using XlsxWriter as the engine
writer = pd.ExcelWriter('your_file.xlsx', engine='xlsxwriter')

# Convert the DataFrame to an XlsxWriter Excel object, omitting the header
df.to_excel(writer, sheet_name='Sheet1', index=False, header=False)

# Get the xlsxwriter workbook and worksheet objects
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

# Create a border format
border_format = workbook.add_format({'border':1})

# Set the column width to match the row height (approximately)
worksheet.set_column(0, df.shape[1], 15)

# Iterate over the cells in the dataframe
for row_num, row_data in enumerate(df.values):
    for col_num, cell_data in enumerate(row_data):
        # Use the border format
        worksheet.write(row_num, col_num, cell_data, border_format)

# Close the Pandas Excel writer and output the Excel file
writer.close()
