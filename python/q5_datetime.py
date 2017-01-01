# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'
import datetime
d1 = datetime.datetime.strptime(date_start, "%m-%d-%Y")
d2 = datetime.datetime.strptime(date_stop, "%m-%d-%Y")
days = (d2 - d1).days
print (days)

####b)  
date_start = '12312013'  
date_stop = '05282015'  
import datetime
d1 = datetime.datetime.strptime(date_start, "%m%d%Y")
d2 = datetime.datetime.strptime(date_stop, "%m%d%Y")
days = (d2 - d1).days
print (days)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

import datetime
d1 = datetime.datetime.strptime(date_start, "%d-%b-%Y")
d2 = datetime.datetime.strptime(date_stop, "%d-%b-%Y")
days = (d2 - d1).days
print (days)
