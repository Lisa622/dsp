# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
import urllib.request

url = 'https://raw.githubusercontent.com/Lisa622/dsp/master/python/football.csv'
webpage = urllib.request.urlopen(url)
webpage_read = webpage.read().decode('utf-8').splitlines()
datareader = csv.reader(webpage_read)
data = []
for row in datareader:
    data.append(row)
for row in data:
    print(row)

data.pop(0)
goals = [x[5] for x in data]
againsts = [x[6]for x in data]
teams = [x[0] for x in data]
diffs = []
for i in range(0,len(goals)):
    goaldiff = float(goals[i]) - float(againsts[i])
    diffs.append(goaldiff)
min_team = teams[diffs.index(min(diffs))]
print(min_team)
