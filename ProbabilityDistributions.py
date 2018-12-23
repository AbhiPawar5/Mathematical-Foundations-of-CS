import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom
from scipy.stats import poisson
from scipy.stats import norm
from scipy.stats import hypergeom
from scipy.stats import bernoulli
from tkinter import *

def calcHyper():
    typecasted = list(map(float,textHyper.get().split(',')))
    M = np.float_(typecasted[0])
    n = np.float_(typecasted[1])
    N = np.float_(typecasted[2])
        
    hpd = hypergeom(M,n,N)
    x = np.arange(0,n+1)
    pmf = hpd.pmf(x)
    
    plt.plot(x,pmf,'r-')
    plt.xlabel("N values")
    plt.ylabel("Hypergenom PMF")
    plt.title("Hypergeometric Distribution")
    plt.show()
    
    
def calcUnif():
    typecasted = list(map(float,textUnif.get().split(',')))
    low = np.float_(typecasted[0])
    high = np.float_(typecasted[1])
    size = np.float_(typecasted[2])
    
    values = np.random.uniform(int(low),int(high),int(size))
    _,bins,_ = plt.hist(values,15)
    plt.plot(bins,np.ones_like(bins),color='r')
    plt.xlabel("Values")
    #plt.xlim(0,int(high))
    plt.ylabel("Frequency")
    plt.title("Uniform Distribution")
    plt.show()
    

def calcBern():
    typecasted = list(map(float,textBern.get().split(',')))
    x = np.float_(typecasted[0])
    p = np.float_(typecasted[1])
    np.random.seed(123)
    
    Y = np.random.binomial(1,float(p),int(x))
    plt.hist(Y,50)
    plt.xlabel("Sucess(1) and Failure(0)")
    plt.ylabel("Number of trails")
    plt.title("Bernoulli Distribution")
    plt.show()
    
def calcBino():
    typecasted = list(map(float,textBino.get().split(',')))
    n = np.float_(typecasted[0])
    p = np.float_(typecasted[1])
    x = np.float_(typecasted[2])
    
    x = np.arange(x)
    value = binom(n,p)
    plt.plot(x,value.pmf(x),'ro')
    plt.xlabel("Number of sucess")
    plt.ylabel("Probability of sucess")
    plt.title("Binomial Distribution")
    plt.show()
    
def calcPoiss():
    typecasted = list(map(float,textPoiss.get().split(',')))
    k = np.float_(typecasted[0])
    meanval = np.float_(typecasted[1])
    
    k = np.arange(k)
    poiss = poisson.pmf(k,meanval)
    plt.title("Poisson Distribution")
    plt.xlabel("Number of events")
    plt.ylabel("Probability of events")
    plt.plot(k,poiss,'ro')
    plt.show()

def calcNormal():
    typecasted = list(map(float,textNormal.get().split(',')))
    x1 = np.float_(typecasted[0])
    x2 = np.float_(typecasted[1])
    meanval = np.float_(typecasted[2])
    std = np.float_(typecasted[3])
    
    x = np.arange(x1,x2,1)
    normal = norm.pdf(x,meanval,std)
    plt.plot(x,normal)
    plt.title("Normal Distribution")
    plt.ylabel("Probability Density")
    plt.show()
    
#GUI CODE Starts here.
root = Tk()
root.title("MFCS Assignment 1")
Label(root,text="Simple Probaility Distribution Application by Abhishek Pawar(009)").grid(row=0,column=0,sticky=W,pady=10)

#GUI CODE for Binomial Starts here.
#Probab of getting 2 heads out of 10 flips is 0.3...using pmf to calculate probab for each observation

Label(root,text="Enter N , P , X: ").grid(row=1,column=0,sticky=W)
textBino = StringVar()
Entry(root,textvariable=textBino).grid(row=1,column=1,sticky=W)
Button(root,text="Calculate Binomial Distribution",command=calcBino).grid(row=2,column=0,sticky=W)

#GUI CODE for Poisson Starts here.
#probab of having 5 or fewer typos.
#so k =6 and mean=6 where in 400 page textbook
Label(root,text="Enter K and Mean : ").grid(row=3,column=0,sticky=W)
textPoiss = StringVar()
Entry(root,textvariable=textPoiss).grid(row=3,column=1,sticky=W)
Button(root,text="Calculate Poisson Distribution",command=calcPoiss).grid(row=4,column=0,sticky=W)

#GUI CODE for Normal Starts here.
Label(root,text="Enter -X , X , Mean , SD : ").grid(row=5,column=0,sticky=W)
textNormal = StringVar()
Entry(root,textvariable=textNormal).grid(row=5,column=1,sticky=W)
Button(root,text="Calculate Normal Distribution",command=calcNormal).grid(row=6,column=0,sticky=W)

#GUI CODE for Bernoulli starts here.
Label(root,text="Enter X and P :").grid(row=7,column=0,sticky=W)
textBern = StringVar()
Entry(root,textvariable=textBern).grid(row=7,column=1,sticky=W)
Button(root,text="Calculate Bernoulli Distribution",command=calcBern).grid(row=8,column=0,sticky=W)

#GUI CODE for Uniform starts here.
Label(root,text="Enter Low , High and Size :").grid(row=9,column=0,sticky=W)
textUnif = StringVar()
Entry(root,textvariable=textUnif).grid(row=9,column=1,sticky=W)
Button(root,text="Calculate Uniform Distribution",command=calcUnif).grid(row=10,column=0,sticky=W)

#GUI CODE for HyperGeometric starts here.
#We have 20 animals,where 7 are dogs.probab of finding x dogs if we choose 12 out of 20.
# so M = 20,n = 7,N = 12
Label(root,text="Enter M , n , N  :").grid(row=11,column=0,sticky=W)
textHyper = StringVar()
Entry(root,textvariable=textHyper).grid(row=11,column=1,sticky=W)
Button(root,text="Calculate HyperGeom Distribution",command=calcHyper).grid(row=12,column=0,sticky=W)

root.mainloop()
