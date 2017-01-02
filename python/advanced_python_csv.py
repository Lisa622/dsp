import csv
import urllib.request

url = 'https://raw.githubusercontent.com/Lisa622/dsp/master/python/faculty.csv'
webpage = urllib.request.urlopen(url)
webpage_read = webpage.read().decode('utf-8').splitlines()
datareader = csv.reader(webpage_read)
data = []
for row in datareader:
    data.append(row)
data.pop(0)
emails = [x[3] for x in data]
outputfile = open('emails.csv', 'w', newline ='')
outputwriter = csv.writer(outputfile)
for i in emails:
    outputwriter.writerow([i])
