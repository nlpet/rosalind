from __future__ import division

k,m,n = 17,23,15
t = float(k+m+n)

def firstLaw(k,m,n):
   N = k+m+n
   return ( k*(k-1+2*(m+n)) + .75*m*(m-1) + m*n ) / ( N*(N-1) )

print 'P (AA v Aa): %.12f' % ( k * (k-1+2*(m+n) + .75*m*(m-1) + m*n) / (t*(t-1)))
#print 'P (AA v Aa): %.12f' % (((k*(k-1))+(k*m)+(k*n)+(m*k)+(0.75*m*(m-1))+(0.5*m*n)+(n*(k-1))+(n*m)+0) / (t* (t-1)))
print firstLaw(k,m,n)