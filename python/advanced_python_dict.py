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
names = [x[0] for x in data]
info = [x[1:] for x in data]
surnames = []
surnamesdict = {}
counter = 0
for i in names:
    j = i.split()
    fullname = (j[0]+' '+' '.join(j[1:-1]),j[-1])
    surnamesdict.setdefault(fullname,[])
    surnamesdict[fullname].extend(info[counter])
    counter += 1
for k in sorted(surnamesdict.keys(),key=lambda t: t[1]):
    print (k,':',surnamesdict[k])
