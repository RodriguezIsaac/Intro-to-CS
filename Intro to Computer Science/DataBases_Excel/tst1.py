import xlsxwriter

workbook = xlsxwriter.Workbook('Gym Progression1.xlsx')
worksheet = workbook.add_worksheet('Personal_Records')


column = 0


worksheet.set_column(0, 0, 26)


for i in range(9):
    worksheet.set_column(0, column + i, 32)


bold = workbook.add_format({'bold': 1})
bold.set_align('center')

bold1 = workbook.add_format({'bold': 1, 'font_color': 'red', 'bg_color': 'silver'})
bold1.set_align('center')

bold2 = workbook.add_format({'bold': 1, 'bg_color': 'silver'})
bold2.set_align('center')


worksheet.write("A1", "Timeline", bold1)
worksheet.write("B1", "Deadlift (lbs)", bold1)
worksheet.write("D1", "Bench (lbs)", bold1)
worksheet.write("F1", "Squat (lbs)", bold1)


PR = ['Week 2', 'Week 4', 'Week 6', 'Week 8', 'Week 10', 'Week 12', 'Week 15', 'Week 20', 'Week 25',
      'Week 28', 'Week 30', 'Week 31', 'Week 32', 'Week 34', 'Week 35', 'Week 41']

DL = [175, 195, 210, 215, 220, 225, 245, 275, 285, 285, 295, 295, 300, 315, 325, 325]

Bench = [105, 110, 110, 115, 115, 115, 115, 130, 135, 145, 145, 145, 145, 145, 165, 165]

Squat = ['Did Not Do', 155, 155, 165, 165, 165, 185, 185, 185, 225, 225, 235, 235, 235, 235, 245]


row = 1
row1 = 1
row2 = 1
row3 = 1

col = 0


for week in PR:
    worksheet.write(row, col, week, bold)
    row += 1


for deadlift in DL:
    worksheet.write(row1, col + 1, deadlift, bold)
    row1 += 1


for press in Bench:
    worksheet.write(row2, col + 3, press, bold)
    row2 += 1


for leg in Squat:
    worksheet.write(row3, col + 5, leg, bold)
    row3 += 1


worksheet.write('C1', 'Weight Increase from Previous (lbs)', bold2)
worksheet.write('E1', 'Weight Increase from Previous (lbs)', bold2)
worksheet.write('G1', 'Weight Increase from Previous (lbs)', bold2)
worksheet.write('I1', 'Weight Increase from Previous (lbs)', bold2)


for p in range(16):
    worksheet.write('C' + str(3 + p), '=B' + str(3 + p) + '-B' + str(2 + p), bold)
    worksheet.write('E' + str(3 + p), '=D' + str(3 + p) + '-D' + str(2 + p), bold)


for s in range(15):
    worksheet.write('G' + str(4 + s), '=F' + str(4 + s) + '-F' + str(3 + s), bold)


for t in range(15):
    worksheet.write('I' + str(4 + t), '=H' + str(4 + t) + '-H' + str(3 + t), bold)


worksheet.write('A18', 'N/A', bold)
worksheet.write('B18', 345, bold)
worksheet.write('D18', 185, bold)
worksheet.write('F18', 265, bold)


worksheet.write('H1', 'TOTAL WEIGHT (lbs)', bold1)

for t in range(16):
    worksheet.write('H' + str(3 + t), '=B' + str(3 + t) + '+D' + str(3 + t) + '+F' + str(3 + t), bold)


Exercise = ['Deadlift (x More than BW)', 'Bench (x More than BW)', 'Squat (x More than BW)', 'Total Weight (x More than BW)']

row4 = 24
col1 = 1



worksheet.write('A22', 'Current Bodyweight (BW)', bold1)
worksheet.write_number('A23', 134.8, bold)
worksheet.write('A25', 'Weight Lifted Compared to BW:', bold1)

for lift in Exercise:
    worksheet.write(row4, col1, lift, bold2)
    col1 += 1

worksheet.write('B26', '=ROUND((B18/A23), 2)', bold)
worksheet.write('C26', '=ROUND((D18/A23), 2)', bold)
worksheet.write('D26', '=ROUND((F18/A23), 2)', bold)
worksheet.write('E26', '=ROUND((H18/A23), 2)', bold)


DL_Graph = workbook.add_chart({'type': 'line'})
DL_Graph.set_title({'name': 'Deadlift'})
DL_Graph.set_size({'width': 700, 'height': 340})

DL_Graph.set_y_axis({'name': 'Weight (lbs)'})
DL_Graph.set_x_axis({'visible': False})

DL_Graph.add_series({'values': '=Personal_Records!$B$2:$B$18', 'marker': {'type': 'circle', 'size': 10},
                     'data_labels': {'value': True, 'position': 'above'}})

worksheet.insert_chart('A30', DL_Graph)


Bench_Graph = workbook.add_chart({'type': 'line'})
Bench_Graph.set_title({'name': 'Bench'})
Bench_Graph.set_size({'width': 700, 'height': 340})

Bench_Graph.set_y_axis({'name': 'Weight (lbs)'})
Bench_Graph.set_x_axis({'visible': False})

Bench_Graph.add_series({'values': '=Personal_Records!$D$2:$D$18', 'marker': {'type': 'circle', 'size': 10},
                        'data_labels': {'value': True, 'position': 'above'}})

worksheet.insert_chart('D30', Bench_Graph)


Squat_Graph = workbook.add_chart({'type': 'line'})
Squat_Graph.set_title({'name': 'Squat'})
Squat_Graph.set_size({'width': 690, 'height': 340})

Squat_Graph.set_y_axis({'name': 'Weight (lbs)'})
Squat_Graph.set_x_axis({'visible': False})

Squat_Graph.add_series({'values': '=Personal_Records!$F$3:$F$18', 'marker': {'type': 'circle', 'size': 10},
                        'data_labels': {'value': True, 'position': 'above'}})

worksheet.insert_chart('G30', Squat_Graph)


Total_Graph = workbook.add_chart({'type': 'line'})
Total_Graph.set_title({'name': 'Total Weight'})
Total_Graph.set_size({'width': 700, 'height': 340})

Total_Graph.set_y_axis({'name': 'Weight (lbs)'})
Total_Graph.set_x_axis({'visible': False})

Total_Graph.add_series({'values': '=Personal_Records!$H$3:$H$18', 'marker': {'type': 'circle', 'size': 10},
                        'data_labels': {'value': True, 'position': 'above'}})

worksheet.insert_chart('J30', Total_Graph)


workbook.close()
