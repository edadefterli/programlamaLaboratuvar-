import random
import pylab

def variance(x):
    mean=sum(x)/len(x)
    tot=0.0
    for i in x:
        tot+=(i-mean)**2
    return tot/len(x)

def stdDev(x):
    return variance(x)**0.5

def plotMeans(numDicePerTrial,numDiceThrown,numBins,legend,color,style):
    means=[]
    numTrials=numDiceThrown//numDicePerTrial
    for i in range(numTrials):
        vals=0
        for j in range(numDicePerTrial):
            vals+=5*random.random()
        means.append(vals/numDicePerTrial)
        pylab.hist(means,numBins,color=color,label=legend,weights=pylab.array(len(means)*[1])/len(means),hatch=style)
    return sum(means)/len(means),variance(means)

mean,var=plotMeans(10,100,50,'1 die','w','*')
print("Mean of rolling 1 die=",round(mean,4),"Varience=",round(var,4))

