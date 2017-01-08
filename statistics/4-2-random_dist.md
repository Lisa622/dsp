[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> **Yes, the distribution is uniform**

```python
import thinkstats2
import thinkplot
import numpy as np

rando = np.random.random(1000)
pmf = thinkstats2.Pmf(rando)
thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.Show(xlabel = 'Random variate', ylabel = 'PMF')
cdf = thinkstats2.Cdf(rando)
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='Random variate', ylabel='CDF')
```
