import csv
import urllib.request
import re

url = 'https://raw.githubusercontent.com/Lisa622/dsp/master/python/faculty.csv'
webpage = urllib.request.urlopen(url)
webpage_read = webpage.read().decode('utf-8').splitlines()
datareader = csv.reader(webpage_read)
data = []
for row in datareader:
    data.append(row)
for row in data:
    print(row)
data.pop(0)
emails = [x[3] for x in data]
#for i in emails:
    #print (i)
domains = []
for i in emails:
    domain = re.search("@[\w.]+", i)
    domains.append(domain.group())
uniquedomains = set(domains)
print(uniquedomains)
