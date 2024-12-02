import xlsxwriter
import math

print('Enter file name:')
filename = input()

print('Enter number of measurements:')
PM = input()
PM_int = int(PM)
wri = PM_int+3

workbook = xlsxwriter.Workbook(filename+".xlsx")
worksheet = workbook.add_worksheet()
worksheet.set_column(2, 0, 20)

number_format = workbook.add_format({"num_format": "0.000000000"})


worksheet.write("A1", "NH")
worksheet.write("B1", "ODCH")
worksheet.write("C1", "∆l^2")

numbers = []
loops = 1
while loops != PM_int + 1:
    print('Enter number ' + str(loops) + ':')
    num_str = input()
    num = float(num_str.replace(",", "."))
    numbers.append(num)
    loops += 1

row = 1
for number in numbers:
    worksheet.write(row, 0, number)
    row += 1

avg = sum(numbers) / len(numbers)
worksheet.write("A"+str(wri), avg)

row = 1
for number in numbers:
    result1 = number - avg
    worksheet.write(row, 0, number)
    worksheet.write(row, 1, result1)
    row += 1

row = 1
for number in numbers:
    result2 = (number - avg) ** 2  
    worksheet.write(row, 0, number)
    worksheet.write(row, 2, result2, number_format)
    row += 1

row = 1
sum1 = 0
for number in numbers:
    result2 = (number - avg) ** 2  
    sum1 += result2
    row += 1

odh = 2/3*math.sqrt(sum1/(PM_int*(PM_int-1)))

worksheet.write("C"+str(wri), odh)

workbook.close()