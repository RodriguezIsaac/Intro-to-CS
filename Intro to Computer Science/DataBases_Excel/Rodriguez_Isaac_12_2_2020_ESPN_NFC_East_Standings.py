import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('NFC East Standings.xlsx')
worksheet = workbook.add_worksheet("Standings")

# Adjust the column width.
worksheet.set_column(0, 0, 17)


# Add a Format format to use to highlight cells.
NYG = workbook.add_format({'bold': 1, 'font_color': 'white', 'bg_color': 'blue'})
Washington = workbook.add_format({'bold': 1, 'font_color': 'white', 'bg_color': 'red'})
PE = workbook.add_format({'bold': 1, 'font_color': 'white', 'bg_color': 'green'})
DC = workbook.add_format({'bold': 1, 'font_color': 'navy', 'bg_color': 'gray'})

Bold = workbook.add_format({'bold': 1})


worksheet.write("A1", "Team", Bold)
worksheet.write("B1", "Wins", Bold)
worksheet.write("C1", "Losses", Bold)
worksheet.write("D1", "Ties", Bold)
worksheet.write("E1", "WinRate", Bold)


# Some data we want to write to the worksheet.
Standings = (
    ['NewYork Giants', 4, 7, 0, NYG],
    ['Washington',   4, 7, 0, Washington],
    ['Philadelphia Eagles',  3, 7, 1, PE],
    ['Dallas Cowboys',    3, 8, 0, DC]
)

# Start from the first cell. Rows and columns are zero indexed.
row = 1
col = 0

# Iterate over the data and write it out row by row.
for Team, Wins, Losses, Ties, Coloring in Standings:
    worksheet.write(row, col, Team, Coloring)
    worksheet.write(row, col + 1, Wins)
    worksheet.write(row, col + 2, Losses)
    worksheet.write(row, col + 3, Ties)
    worksheet.write(row, col + 4, f"=ROUND({Wins}/({Losses}+{Wins}+{Ties}), 2)", Bold)
    if Ties > 0:
        worksheet.write(row, col + 4, f"=ROUND(({Wins}+{0.5 * Ties})/({Losses}+{Wins}+{Ties}), 2)", Bold)
    row += 1


workbook.close()
