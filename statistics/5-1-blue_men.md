[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 


```python
import scipy.stats

averageht = 178
standarddev = 7.7
distribution = scipy.stats.norm(loc=averageht, scale=standarddev)
blueht1 = 177.8
blueht2 = 185.4
print (distribution.cdf(blueht2)-distribution.cdf(blueht1))
```
