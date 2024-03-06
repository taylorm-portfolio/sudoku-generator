# this code generate using AI
import pandas as pd

def saveExcel(df, name, sheet):
    # Create a Pandas Excel writer using XlsxWriter as the engine
    writer = pd.ExcelWriter(name+".xlsx", engine='xlsxwriter')

    # Convert the DataFrame to an XlsxWriter Excel object, omitting the header and index
    df.to_excel(writer, sheet_name=sheet, index=False, header=False)

    # Get the xlsxwriter workbook and worksheet objects
    workbook  = writer.book
    worksheet = writer.sheets[sheet]

    # Center-align all cell values
    df_styled = df.style.set_properties(**{"text-align": "center", "vertical-align": "middle"})
    df_styled.to_excel(writer, sheet_name=sheet, index=False, header=False)

    # Create border formats for each kind of cell
    left_border_format = workbook.add_format({'left':2,'align':'center','valign':'vcenter'})
    right_border_format = workbook.add_format({'right':2,'align':'center','valign':'vcenter'})
    top_border_format = workbook.add_format({'top':2,'align':'center','valign':'vcenter'})
    bottom_border_format = workbook.add_format({'bottom':2,'align':'center','valign':'vcenter'})
    nw_corner_border = workbook.add_format({'left':2, 'top':2,'align':'center','valign':'vcenter'})
    ne_corner_border = workbook.add_format({'right':2, 'top':2,'align':'center','valign':'vcenter'})
    sw_corner_border = workbook.add_format({'left':2, 'bottom':2,'align':'center','valign':'vcenter'})
    se_corner_border = workbook.add_format({'right':2, 'bottom':2,'align':'center','valign':'vcenter'})
    # Set the column width and row height to make cells look more square
    worksheet.set_column(0, df.shape[1], 2.5)
    worksheet.set_default_row(18)

    # Iterate over the cells in the dataframe
    for row_num, row_data in enumerate(df.values):
        for col_num, cell_data in enumerate(row_data):
            # Apply left border to columns 1, 4, 7, and set corner formats for the intersections in these columns.
            if col_num in [0, 3, 6]:
                # Check for intersection cells
                if row_num in [0, 3, 6]:
                    worksheet.write(row_num, col_num, cell_data, nw_corner_border)
                elif row_num == 8:
                    worksheet.write(row_num, col_num, cell_data, sw_corner_border)
                else:
                    worksheet.write(row_num, col_num, cell_data, left_border_format)
            # Apply right border to column 9, and set corner formats for the intersections in this column.
            elif col_num == 8:
                # Check for intersection cells
                if row_num in [0, 3, 6]:
                    worksheet.write(row_num, col_num, cell_data, ne_corner_border)
                elif row_num == 8:
                    worksheet.write(row_num, col_num, cell_data, se_corner_border)
                else:
                    worksheet.write(row_num, col_num, cell_data, right_border_format)
            # Apply top border to remaining cells in rows 1, 4, 7
            elif col_num not in [0, 3, 6, 8]: 
                if row_num in [0, 3, 6]:
                    worksheet.write(row_num, col_num, cell_data, top_border_format)
            # Apply bottom border to remaining cells in row 9
                elif row_num == 8:
                    worksheet.write(row_num, col_num, cell_data, bottom_border_format)
            # Write the remaining cells.
            else:
                worksheet.write(row_num, col_num, cell_data)

    # Close the Pandas Excel writer and output the Excel file
    writer.close()
