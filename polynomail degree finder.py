import random
import time
import numpy as np
# import psutil as ps

class math1(object):
    
    def init__(self,randomlist):
       self.data=randomlist
    def polynomial(self,degree):
        randomlist=[]
        for i in range(degree+1):
            n=random.randint(1,10)
            randomlist.append(n)
            # print(randomlist)
        pg=self.poly_generator(degree,randomlist)
        result=self.pg_solver(pg)
        return result
    def poly_generator(self,degree,randomlist):
        pg=np.poly1d(randomlist)
        mypg=pg
        print(pg)     
        return mypg
    def pg_solver(self,mypg):
        factors=np.roots(mypg)
        print("these are the roots")
              
         
        return(factors)

if __name__=="__main__":
    a=math1()
    st=time.time()
    factors=a.polynomial(9)
    
    print(factors)
    
    et=time.time()
    elp_time=et-st
    print("extuation time is =",elp_time)
    # print("memory usage",ps.cpu_percent())
    
    print("finished")
    

