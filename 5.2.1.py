import csv

csvFile = open("C:\\Python3.5.2_64\\example\\text1.csv", 'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number','number plus 1', 'number times 1'))
    for i in range(0, 10):
        writer.writerow((i, i+2, i*2))
finally:
    csvFile.close()