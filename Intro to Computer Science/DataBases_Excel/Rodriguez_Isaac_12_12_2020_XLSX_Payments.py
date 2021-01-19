import xlsxwriter

workbook = xlsxwriter.Workbook('Payments.xlsx')
worksheet = workbook.add_worksheet('Payments')


worksheet.set_column(0, 0, 26)


bold = workbook.add_format({'bold' : 1})
bold.set_align('center')

money_format = workbook.add_format({'num_format' : '$#,##0.00'})
money_format.set_align('center')

Highlight = workbook.add_format({'bold' : 1, 'bg_color' : 'yellow'})
Highlight.set_align('center')

Center = workbook.add_format()
Center.set_align('center')

worksheet.write('A1', 'Dates', bold)
worksheet.write('B1', '# of Days', bold)
worksheet.write('C1', 'Total', bold)
worksheet.write('D1', 'Paid', bold)
worksheet.write('E1', 'Check #', bold)


Data = (
    ['January 3 through January 6', 4, 160.00, 'Paid', 102],
    ['January 9-10 & January 12-13', 4, 160.00, 'Paid', 106],
    ['January 17-20', 4, 160.00, 'Paid', 108],
    ['January 23-27', 5, 198.00, 'Paid', 112]
)


row = 2
col = 0


for Date, Days, Amount, Paid, Check in Data:
    worksheet.write(row, col, Date, Center)
    worksheet.write(row, col + 1, Days, Center)
    worksheet.write(row, col + 2, Amount, money_format)
    worksheet.write(row, col + 3, Paid, Center)
    worksheet.write(row, col + 4, Check, Center)
    row += 1


worksheet.write(row + 3, col, 'TOTAL', Highlight)

money = workbook.add_format({'num_format' : '$#,##0.00', 'bold' : True, 'bg_color' : ('yellow')})
money.set_align('center')

worksheet.write(row + 3, col + 2, '=SUM(C3:C6)', money)

worksheet.write('B10', '', Highlight)

workbook.close()
